"""MkDocs hook, which patches the Blog plugin to fix the `post_date_format` option.
Works only with the Material theme, and requires the "theme_overrides_manager" hook.

By default when using multiple blog instance the `post_date_format` option of the last instance
modifies the date format for all instances. The patch makes it so every instance has their own
date format.

The hook dynamically on the fly modifies the "partials/post.html" and "blog-post.html" templates
of the Material theme / in the users overrides before the build.
It uses the theme_overrides_manager hook to assure original file preservation after the build ends.

MIT Licence 2024 Kamil Krzyśków (HRY)
"""

import inspect
import logging
from pathlib import Path
from typing import Callable, Dict, List, Optional, Tuple, Union

from jinja2 import Environment
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.plugins import PrefixedLogger
from pymdownx import twemoji_db, util
from pymdownx.emoji import TWEMOJI_SVG_CDN

# region Core Logic Events

_SUPPORTS_BLOG_PATCH = True
"""If the patch is not supported it will be set to False"""


def on_config(config: MkDocsConfig) -> Optional[MkDocsConfig]:
    """Posts are resolved in on_files, so the patch has to be applied before that"""

    global _SUPPORTS_BLOG_PATCH

    func_signature: str = "(file: 'File', config: 'MkDocsConfig')"

    def resolve_post_wrapper(func):
        self = func.__self__

        def wrapper(file, config):
            post = func(file, config)
            post.generator = self
            return post

        return wrapper

    for name, plugin in config.plugins.items():
        if name.startswith("material/blog"):
            if not hasattr(plugin, "_resolve_post"):
                _SUPPORTS_BLOG_PATCH = False
                break

            if str(inspect.signature(plugin._resolve_post)) != func_signature:
                _SUPPORTS_BLOG_PATCH = False
                break

            setattr(plugin, "_resolve_post", resolve_post_wrapper(plugin._resolve_post))

    return None


def on_env(env: Environment, *, config: MkDocsConfig, **__) -> Optional[Environment]:
    """Main function. Triggers just before the build begins."""

    LOG.debug('Running "on_env"')

    if not _is_runnable(config=config):
        return None

    import material

    paths_to_fix_date: List[str] = ["partials/post.html", "blog-post.html"]
    paths_with_processors: List[Tuple[Path, Callable]] = []

    overrides_templates: Path = Path(config.theme.custom_dir)
    material_templates: Path = Path(material.__file__).parent / "templates"

    for path in paths_to_fix_date:
        if path.startswith("blog"):
            processor = _fix_blog_post
        else:
            processor = _fix_partials_post

        current = overrides_templates / path
        if current.exists():
            paths_with_processors.append((current, processor))
            continue

        current = material_templates / path
        if current.exists():
            paths_with_processors.append((current, processor))

    if len(paths_to_fix_date) != len(paths_with_processors):
        LOG.warning("Mismatch in defined paths and processed paths")
        return None

    if not _is_patched_blog(config=config, env=env):
        LOG.warning("The blog plugin version doesn't support patching")
        return None

    for pair in paths_with_processors:
        config.extra[HOOK_MANAGER].paths_with_processors.append(pair)

    LOG.info(f"Registered processors")

    return None


def _is_runnable(*, config: MkDocsConfig) -> bool:
    """Make sure the hook should run."""

    if HOOK_MANAGER not in config["extra"]:
        LOG.info(f'"{HOOK_MANAGER}" not detected')
        return False

    if config.theme["name"] != "material":
        LOG.info('Only the "material" theme is supported')
        return False

    return True


def _is_patched_blog(*, config: MkDocsConfig, env: Environment) -> bool:
    """Patch the BlogPlugin class to include the attach a reference to each created Post class"""

    global _SUPPORTS_BLOG_PATCH

    if not _SUPPORTS_BLOG_PATCH:
        return False

    def get_creation_date(post):
        if not hasattr(post, "generator"):
            post.generator = post.post.generator
        format = post.generator.config.post_date_format
        return post.generator._format_date(post.config.date.created, format, config)

    def get_update_date(post):
        if not hasattr(post, "generator"):
            post.generator = post.post.generator
        format = post.generator.config.post_date_format
        return post.generator._format_date(post.config.date.updated, format, config)

    env.filters["post_date_created"] = get_creation_date
    env.filters["post_date_updated"] = get_update_date

    return True


def _fix_blog_post(*, partial: Path, config: MkDocsConfig, **__) -> None:

    # Configure the tokens
    tokens: Dict[str, str] = {
        "START": "{% block container %}",
        "CREATED": ".config.date.created | date",
        "UPDATED": ".config.date.updated | date",
        "END": "{% endblock %}",
    }

    # A negative number means the same level as the START token.
    end_indent_level: int = -1

    override_manager = config.extra[HOOK_MANAGER]

    loaded_section: str = override_manager.load_section(
        partial=partial, tokens=tokens, end_level=end_indent_level
    )

    # Do not continue when section is not loaded
    if not loaded_section:
        return

    # Configure replacements
    replacements: Dict[str, str] = {
        "CREATED": " | post_date_created",
        "UPDATED": " | post_date_updated",
    }

    modified_section: str = loaded_section.replace(
        tokens["CREATED"], replacements["CREATED"]
    ).replace(tokens["UPDATED"], replacements["UPDATED"])

    # Modify the partial
    override_manager.save_section(
        partial=partial, original_section=loaded_section, modified_section=modified_section
    )

    LOG.debug(f'Processed "{partial.name}".')


def _fix_partials_post(*, partial: Path, config: MkDocsConfig, **__) -> None:

    # Configure the tokens
    tokens: Dict[str, str] = {
        "START": "<article",
        "CREATED": ".config.date.created | date",
        "END": "</article>",
    }

    # A negative number means the same level as the START token.
    end_indent_level: int = -1

    override_manager = config.extra[HOOK_MANAGER]

    loaded_section: str = override_manager.load_section(
        partial=partial, tokens=tokens, end_level=end_indent_level
    )

    # Do not continue when section is not loaded
    if not loaded_section:
        return

    # Configure replacements
    replacements: Dict[str, str] = {"CREATED": " | post_date_created"}

    modified_section: str = loaded_section.replace(tokens["CREATED"], replacements["CREATED"])

    # Modify the partial
    override_manager.save_section(
        partial=partial, original_section=loaded_section, modified_section=modified_section
    )

    LOG.debug(f'Processed "{partial.name}".')


# endregion


# region Constants

HOOK_NAME: str = "fix_blog_date"
"""Name of this hook. Used in logging."""

HOOK_MANAGER: str = "theme_overrides_manager"
"""Name of the hook manager. Used to access it in `config.extra`."""

LOG: PrefixedLogger = PrefixedLogger(
    HOOK_NAME, logging.getLogger(f"mkdocs.hooks.theme_overrides.{HOOK_NAME}")
)
"""Logger instance for this hook."""

# endregion
