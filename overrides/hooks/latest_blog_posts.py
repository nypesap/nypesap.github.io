"""MkDocs hook that inserts latest blog posts on a page

Currently limited to the homepage.

MIT Licence 2024 Kamil Krzyśków (HRY) for Nype (npe.cm)
"""

import logging

from material.plugins.blog.plugin import BlogPlugin
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.plugins import PrefixedLogger
from mkdocs.structure.pages import Page


def on_config(config: MkDocsConfig):
    BLOG_INSTANCE_MAP.clear()

    for name, instance in config.plugins.items():
        instance: BlogPlugin
        if name.startswith("material/blog"):
            if instance.config.enabled:
                root = instance.config.blog_dir.rstrip("/") + "/"
                BLOG_INSTANCE_MAP[root] = instance


def on_page_markdown(markdown: str, page: Page, config: MkDocsConfig, files):

    if page.file.src_uri != "index.md":
        return

    lines = markdown.split("\n")

    for i, line in enumerate(lines):
        if f"ext:{HOOK_NAME}" in line:
            lines[i] = insert_latest_posts(line, config)

    return "\n".join(lines)


def insert_latest_posts(line, config: MkDocsConfig):

    raw_options = line.split("|")[-1].replace("-->", "").strip()
    options_pairs = [option.split("=") for option in raw_options.split(";") if option.strip()]
    options = {name.strip(): value.strip() for name, value in options_pairs}

    all_good = True

    for name in REQUIRED_OPTIONS:
        if name not in options:
            LOG.warning(f"Missing option {name}")
            all_good = False

    if not all_good:
        return line

    root = options["root"].rstrip("/") + "/"
    amount = int(options["amount"])
    markdown = True if str(options.get("markdown")).lower() == "true" else False

    if root not in BLOG_INSTANCE_MAP:
        LOG.warning(f"Blog root {root} does not match any blog instance")
        return line

    instance: BlogPlugin = BLOG_INSTANCE_MAP[root]
    posts = instance.blog.posts[:amount]

    # Hack: extract title from nav, as the blog index file was not loaded yet
    blog_title = ""
    for entry in config.nav:
        for value in entry.values():
            if not isinstance(value, list):
                continue
            if root in value[0]:
                blog_title = list(entry.keys())[0]
        if blog_title:
            break

    li_entries = ""
    icon_shortcode = ""
    icon_shortcodes = {"exp/": ":ext-sap-ui5:", "blog/": ":ext-nype-logo:"}

    if markdown:
        insert_body = MARKDOWN_GRID_TEMPLATE
        blog_index_url = instance.blog.file.src_uri
        icon_shortcode = icon_shortcodes[root]
        for post in posts:
            href = post.file.src_uri
            text = post.title
            li_entries += f"    - [{text}]({href})\n"
    else:
        insert_body = HTML_TEMPLATE
        blog_index_url = instance.blog.file.url
        for post in posts:
            href = post.file.url
            text = post.title
            li_entries += f'<li><a href="{href}">{text}</a></li>\n'

    return insert_body.format(
        blog_title=blog_title,
        li_entries=li_entries,
        blog_index_url=blog_index_url,
        icon_shortcode=icon_shortcode,
    )


HOOK_NAME: str = "latest_blog_posts"
"""Name of the hook"""

LOG: PrefixedLogger = PrefixedLogger(HOOK_NAME, logging.getLogger(f"mkdocs.hooks.{HOOK_NAME}"))
"""Logger instance for this hook."""

BLOG_INSTANCE_MAP: dict[str, BlogPlugin] = {}
"""Mapping of active blog instances. Set in on_config"""

REQUIRED_OPTIONS: list[str] = ["root", "amount"]
"""List of lowercase required options to validate the input"""

HTML_TEMPLATE: str = (
    """
<p>
<div>Latest {blog_title} posts:</div>
<ul>
{li_entries}
</ul>
<div><a href="{blog_index_url}">Read more {blog_title} posts</a></div>
</p>
""".strip()
)

MARKDOWN_GRID_TEMPLATE: str = (
    """
- {icon_shortcode} Latest {blog_title} posts:

    ---

{li_entries}

    ---

    [Read more {blog_title} posts]({blog_index_url})

""".lstrip()
)