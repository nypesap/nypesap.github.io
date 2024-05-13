"""One-off script to permanently patch blog plugin's files.

This can be run also as a hook, but then exits MkDocs early to reload the patch files.
The blog plugin's post_date_format option is fixed for all instances.
The blog plugin's post.more handling for the Continue Reading link is blocked.

To restore the files run:
    pip install mkdocs-material --force-reinstall

MIT Licence 2024 Kamil Krzyśków (HRY) for Nype (npe.cm)
"""

import os
from pathlib import Path


def main() -> bool:
    """Entry point, has to return boolean about the patch to the MkDocs hook"""

    import material

    current_path = Path(os.getcwd())
    material_root = Path(material.__file__).parent
    templates = material_root / "templates"
    blog_root = material_root / "plugins" / "blog"
    blog_plugin = blog_root / "plugin.py"

    assert blog_plugin.exists(), "blog plugin wasn't found?"

    # Track patch states
    applied_patches = []

    # 1. To each Post we need to add a reference to the Blog instance that processed it
    applied_patches.append(add_blog_reference(blog_plugin))

    # 2. We need to add a modified date formatter function that is Blog instance aware
    applied_patches.append(add_date_formatter(blog_plugin))

    # 3. We need to modify the templates to use the new modified date formatter
    partials_post = templates / "partials" / "post.html"
    blog_post = templates / "blog-post.html"

    assert partials_post.exists() and blog_post.exists(), "at least one partial wasn't found?"

    applied_patches.append(modify_data_filter_in_template(partials_post, blog_post))

    # 4. Hide the "Continue reading" part from the page
    # This was previously done with normal overrides, but this approach was blocked with
    # 1., 2., and 3. modifying the Python code that is used in the template
    applied_patches.append(hide_continue_reading_prompt(partials_post))

    return any(applied_patches)


def add_blog_reference(filepath: Path) -> bool:
    """
    1. Posts are created only in the _resolve_post function in the plugin.py file
    1. Skip if the file already contains the patch
    Returns a boolean to track the patch injection
    """

    content = filepath.read_text(encoding="utf-8")
    patch = "post.generator = self"

    if patch in content:
        return False

    token_1 = "def _resolve_post(self"
    token_2 = "post ="

    lines = content.split("\n")
    previous = ""

    for i, line in enumerate(lines):
        line = line.rstrip()

        if token_1 in previous and token_2 in line:
            depth = len(line) - len(line.lstrip())
            lines[i] = f"{line}\n{' ' * depth}{patch}"
            token_1 = True
            token_2 = True
            break

        previous = line

    assert token_1 is True and token_2 is True, "patch wasn't applied, new blog plugin version?"

    filepath.write_text("\n".join(lines), encoding="utf-8")

    return True


def add_date_formatter(filepath: Path) -> bool:
    """
    2. The date formatter has to be injected into the env.filters in the plugin.py file
    2. Skip if the file already contains the patch
    Returns a boolean to track the patch injection
    """

    content = filepath.read_text(encoding="utf-8")
    patch = """
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
    """.lstrip().split(
        "\n"
    )

    # Clear 4 indent spaces for lines above, except the first one
    for i, line in enumerate(patch):
        if i == 0:
            continue
        patch[i] = line[4:]

    if patch[0] in content:
        return False

    token_1 = "def on_env("
    token_2 = "def date_filter("

    lines = content.split("\n")
    previous = ""

    for i, line in enumerate(lines):
        line = line.rstrip()

        if token_1 is not True and token_1 in line:
            token_1 = True
            continue

        if token_1 is True and token_2 in line:
            depth = len(line) - len(line.lstrip())
            patch_with_depth = "\n".join(map(lambda x: f"{' ' * depth}{x}", patch))
            lines[i] = f"{patch_with_depth}\n{line}"
            token_2 = True
            break

        previous = line

    assert token_1 is True and token_2 is True, "patch wasn't applied, new blog plugin version?"

    filepath.write_text("\n".join(lines), encoding="utf-8")

    return True


def modify_data_filter_in_template(*filepaths) -> bool:
    """
    3. Skip if the files already contain the patch
    Returns a boolean to track the patch injection
    """

    patched = False

    for filepath in filepaths:

        content = filepath.read_text(encoding="utf-8")
        patch_1 = " | post_date_created"
        patch_2 = " | post_date_updated"

        # patch_2 doesn't have to be present
        if patch_1 in content:
            continue

        token_1 = ".config.date.created | date"
        token_2 = ".config.date.updated | date"

        assert token_1 in content, f"{token_1} not found in the templates, mkdocs-material update?"

        content = content.replace(token_1, patch_1).replace(token_2, patch_2)

        filepath.write_text(content, encoding="utf-8")

        patched = True

    return patched


def hide_continue_reading_prompt(filepath) -> bool:
    """
    4. Skip if the files already contain the patch
    Returns a boolean to track the patch injection
    """

    content = filepath.read_text(encoding="utf-8")
    patch = "if post.more and false"

    if patch in content:
        return False

    token = "if post.more"

    assert token in content, f"{token} not found in the templates, mkdocs-material update?"

    content = content.replace(token, patch)

    filepath.write_text(content, encoding="utf-8")

    return True


if __name__ == "__main__":
    main()
else:
    from mkdocs.plugins import event_priority

    @event_priority(100)
    def on_config(config):
        patched_now = main()
        how_to_restore = """
        Blog plugin is patched.
        If you need to restore mkdocs-material run:
            pip install mkdocs-material --force-reinstall
        """
        print(how_to_restore.lstrip("\n"))
        if patched_now:
            exit("To load the patch MkDocs needs to be restarted...")
