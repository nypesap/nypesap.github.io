"""MkDocs hook that inserts latest blog posts on a page

Currently limited to the homepage.

MIT Licence 2024 Kamil Krzyśków (HRY) for Nype (npe.cm)
"""

import logging

from material.plugins.blog.plugin import BlogPlugin
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.exceptions import PluginError
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

    ext_body = ""
    ext_line = -1

    for i, line in enumerate(lines):
        if f"ext:{HOOK_NAME}" in line and ext_line < 0:
            if "-->" in line:
                lines[i] = insert_latest_posts(line, config)
            else:
                # TODO consider parsing this as the start tag, instead of fishing for it
                if "<!--" in lines[i - 1]:
                    lines[i - 1] = ""
                ext_body += line
                ext_line = i
                continue
        if ext_body:
            ext_body += " " + line.lstrip()
            lines[i] = ""
            if "-->" in line:
                lines[ext_line] = insert_latest_posts(ext_body, config)
                ext_body = ""
                ext_line = -1

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
    display = options.get("display", "markdown").lower()
    title = options["title"]
    read_more = options["read_more"]
    strftime = options.get("strftime")
    if not strftime:
        strftime = "/timeago"

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

    if display == "markdown":
        insert_body = MARKDOWN_GRID_TEMPLATE
        blog_index_url = instance.blog.file.src_uri
        for post in posts:
            href = post.file.src_uri
            text = post.title
            if strftime.startswith("/timeago"):
                date = post.config.date["created"]
                placeholder = post.config.date["created"].strftime("%Y-%m-%d")
                date_span = f'<span class="extPostDate" markdown>:material-clock-plus-outline: <span class="timeago" datetime="{date}" locale="en">{placeholder}</span></span>'
            else:
                date = post.config.date["created"].strftime(strftime)
                date_span = f'<span class="extPostDate">{date}</span>'
            li_entries += f'    - {date_span}\n    [{text}]({href})\n'
    elif display == "html_simple":
        insert_body = HTML_SIMPLE_TEMPLATE
        blog_index_url = instance.blog.file.url
        for post in posts:
            href = post.file.url
            text = post.title
            li_entries += f'<li><a href="{href}">{text}</a></li>\n'
    elif display == "html_grid":
        insert_body = HTML_GRID_TEMPLATE
        blog_index_url = instance.blog.file.url
        for post in posts:
            li_entries += render_html_grid_li(post, strftime)
    else:
        raise PluginError(f"display setting not supported: {display}")

    return insert_body.format(
        blog_title=blog_title,
        li_entries=li_entries,
        blog_index_url=blog_index_url,
        read_more=read_more,
        title=title,
    )


def render_html_grid_li(post, strftime):
    href = post.file.url
    text = post.title
    date = post.config.date["created"].strftime(strftime)
    return f"""
<li class="mdx-expect__item md-typeset" markdown>
<div class="mdx-expect__icon" markdown>
:material-feather:
</div>
<div class="mdx-expect__description" markdown>
<div class="extEntryTitle" markdown><a href="{href}" markdown>{text}</a></div>
<p markdown>{", ".join(post.config.categories)}</p>
<p markdown><span class="extPostDate">{date}</span></p>
</div>
</li>\n
""".lstrip()


HOOK_NAME: str = "latest_blog_posts"
"""Name of the hook"""

LOG: PrefixedLogger = PrefixedLogger(HOOK_NAME, logging.getLogger(f"mkdocs.hooks.{HOOK_NAME}"))
"""Logger instance for this hook."""

BLOG_INSTANCE_MAP: dict[str, BlogPlugin] = {}
"""Mapping of active blog instances. Set in on_config"""

REQUIRED_OPTIONS: list[str] = ["root", "amount", "title", "read_more"]
"""List of lowercase required options to validate the input"""

HTML_SIMPLE_TEMPLATE: str = (
    """
<p>
<div>{title}</div>
<ul>
{li_entries}
</ul>
<div><a href="{blog_index_url}">{read_more}</a></div>
</p>
""".strip()
)

MARKDOWN_GRID_TEMPLATE: str = (
    """
- {title}

    ---

{li_entries}

    ---

    [{read_more}]({blog_index_url})

""".lstrip()
)

HTML_GRID_TEMPLATE: str = (
    """
<div class="md-grid" markdown>
<header class="md-typeset" markdown>
<h1 markdown>{title}</h1>
</header>
<div class="mdx-expect" markdown>
<ul class="mdx-expect__list" markdown>
{li_entries}
</ul>
</div>
<footer class="md-typeset" markdown>
<div class="extReadMore" markdown><a href="{blog_index_url}" markdown>{read_more}</a></div>
</footer>
</div>
""".strip()
)
