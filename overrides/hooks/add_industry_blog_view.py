"""MkDocs hook, which adds a custom view to the blog plugin.

By default the blog plugin only allows to use Archive and Category views.
This plugin adds another for an Industry view.

A lot of the code is based from the plugin as those instructions aren't in 
importable functions.

MIT Licence 2024 Kamil Krzyśków (HRY) for Nype (npe.cm)
"""

import inspect
import logging
import os
import posixpath
from typing import Optional

from material.plugins.blog.plugin import BlogPlugin
from material.plugins.blog.structure import View
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.exceptions import PluginError
from mkdocs.plugins import PrefixedLogger, event_priority
from mkdocs.structure.files import Files, InclusionLevel
from mkdocs.structure.nav import Section
from pymdownx.slugs import slugify

# region Custom Data and Custom Settings


class Industry(View):
    pass


class IndustryConfig:
    """
    Instead of using default values and overriding them in mkdocs.yml in extra,
    the only place to store the config values is here
    """

    # Based on the categories settings
    industries = True
    industries_name = "Industries"
    industries_url_format = "industry/{slug}"
    industries_slugify = slugify(case="lower")
    industries_slugify_separator = "-"
    industries_allowed = []
    industries_toc = None
    
    # Settings for posts, currently have no visible effect, see template
    post_url_max_industries = 1
    post_excerpt_max_industries = 5

    # Custom settings
    industries_meta_key = "industries"
    blog_dir = "exp"


# endregion

# region Core Logic Events


def on_config(config):
    """Load the Experience blog instance, override BlogPlugin._render_post"""

    global PLUGIN
    PLUGIN = _get_exp_blog_instance(config)

    if PLUGIN is None:
        LOG.warning("Blog instance with the given exp path was not found")
        return

    if not PLUGIN.config.enabled:
        PLUGIN = None
        LOG.info("Blog instance is not enabled")
        return

    if not isinstance(IndustryConfig.industries_toc, bool):
        IndustryConfig.industries_toc = PLUGIN.config.blog_toc

    PLUGIN._render_post = decorate_render_post(PLUGIN._render_post)

    if PLUGIN._render_post.__name__ != "wrapper":
        LOG.warning("_render_post toc override was not applied")


def decorate_render_post(func):
    """The industries_toc isn't taken into account when rendering, so adjust the view afterwards"""

    if func.__name__ == "wrapper":
        return func

    signature = "(excerpt: 'Excerpt', view: 'View')"

    if str(inspect.signature(func)) != signature:
        return func

    def wrapper(excerpt, view):
        excerpt = func(excerpt, view)

        if isinstance(view, Industry):
            if IndustryConfig.industries_toc and not PLUGIN.config.blog_toc:
                if excerpt.toc.items and view.toc.items:
                    view.toc.items[0].children.append(excerpt.toc.items[0])
            elif IndustryConfig.industries_toc is False and PLUGIN.config.blog_toc:
                if view.toc.items:
                    view.toc.items[0].children = []

        return excerpt

    return wrapper


# Run after the blog plugin
@event_priority(-75)
def on_files(files, *, config: MkDocsConfig):
    """Add the custom views to the blog"""
    if PLUGIN is None:
        return

    if IndustryConfig.industries:
        PLUGIN.blog.views.extend(
            sorted(
                _generate_industries(PLUGIN, config, files),
                key=lambda view: view.name,
                reverse=False,
            )
        )

    if PLUGIN.config.pagination:
        for view in PLUGIN._resolve_views(PLUGIN.blog):
            if not isinstance(view, Industry):
                continue
            for page in PLUGIN._generate_pages(view, config, files):
                view.pages.append(page)


# Changing the priority can move position of the Industries from the bottom to the top
@event_priority(-25)
def on_nav(nav, *, config, files):
    """Attach views to navigation"""
    if PLUGIN is None:
        return

    # Attach views for industries
    if IndustryConfig.industries:
        title = PLUGIN._translate(IndustryConfig.industries_name, config)
        views = [_ for _ in PLUGIN.blog.views if isinstance(_, Industry)]

        # Attach and link views for industries, if any
        if PLUGIN.blog.file.inclusion.is_in_nav() and views:
            PLUGIN._attach_to(PLUGIN.blog, Section(title, views), nav)

    # Attach pages for views
    if PLUGIN.config.pagination:
        for view in PLUGIN._resolve_views(PLUGIN.blog):
            if not isinstance(view, Industry):
                continue
            for at in range(1, len(view.pages)):
                PLUGIN._attach_at(view.parent, view, view.pages[at])


@event_priority(-75)
def on_page_markdown(markdown, *, page, config, files):
    """Add industries to the excerpt"""

    if page not in PLUGIN.blog.posts:
        return

    max_industries = IndustryConfig.post_excerpt_max_industries

    if not hasattr(page, "industries"):
        return

    if not hasattr(page.excerpt, "industries"):
        page.excerpt.industries = []

    page.excerpt.industries = page.industries[:max_industries]


def _get_exp_blog_instance(config: MkDocsConfig) -> Optional[BlogPlugin]:
    """Find the blog with the Experience URL"""

    for name, plugin in config.plugins.items():
        if not name.startswith("material/blog"):
            continue
        if plugin.config.blog_dir == IndustryConfig.blog_dir:
            return plugin

    return None


def _generate_industries(plugin: BlogPlugin, config: MkDocsConfig, files: Files):
    """Generate views for industries. Based on BlogPlugin._generate_categories"""
    for post in plugin.blog.posts:
        for name in post.meta.get(IndustryConfig.industries_meta_key, []):
            path = _format_path_for_industry(plugin, name)

            # Ensure industry is in non-empty allow list
            industries = IndustryConfig.industries_allowed or [name]
            if name not in industries:
                docs = os.path.relpath(config.docs_dir)
                path = os.path.relpath(post.file.abs_src_path, docs)
                raise PluginError(
                    f"Error reading industries of post '{path}' in "
                    f"'{docs}': industry '{name}' not in allow list"
                )

            # Create file for view, if it does not exist
            file = files.get_file_from_path(path)
            if not file or plugin.temp_dir not in file.abs_src_path:
                file = plugin._path_to_file(path, config)
                files.append(file)

                # Create file in temporary directory and temporarily remove
                # from navigation, as we'll add it at a specific location
                plugin._save_to_file(file.abs_src_path, f"# {name}")
                file.inclusion = InclusionLevel.EXCLUDED

            # Create and yield view
            if not isinstance(file.page, Industry):
                yield Industry(name, file, config)

            # Assign post to industry and vice versa
            assert isinstance(file.page, Industry)
            file.page.posts.append(post)

            # Add custom list for our custom view type
            if not hasattr(post, "industries"):
                post.industries = []

            post.industries.append(file.page)


def _format_path_for_industry(plugin: BlogPlugin, name: str):
    """
    Format path for industry
    Based on BlogPlugin._format_path_for_category
    """
    path = IndustryConfig.industries_url_format.format(slug=_slugify_industry(name))

    # Normalize path and strip slashes at the beginning and end
    path = posixpath.normpath(path.strip("/"))
    return posixpath.join(plugin.config.blog_dir, f"{path}.md")


def _slugify_industry(name: str):
    """Based on BlogPlugin._slugify_category"""
    separator = IndustryConfig.industries_slugify_separator
    return IndustryConfig.industries_slugify(name, separator)


# endregion


# region Constants

PLUGIN: BlogPlugin = None
"""Set in on_config"""

HOOK_NAME: str = "add_custom_blog_view"
"""Name of this hook. Used in logging."""

LOG: PrefixedLogger = PrefixedLogger(HOOK_NAME, logging.getLogger(f"mkdocs.hooks.{HOOK_NAME}"))
"""Logger instance for this hook."""

# endregion
