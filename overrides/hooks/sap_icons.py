"""MkDocs hook to add SAP icons

The icons are taken from the https://github.com/SAP/ui5-webcomponents/ repository.
ICON_JSONS_URLS at the bottom of the file store URLs to fetch that contain JSON file with SVG paths.
Those paths are injected into a <svg> tag with a viewBox of 0 0 512 512

MIT Licence 2024 Kamil Krzyśków (HRY) for Nype (npe.cm)
"""

import datetime as dt
import json
import logging
from pathlib import Path
from xml.etree.ElementTree import Element  # This is expected to be added by mkdocs-material

import requests  # This is expected to be added by mkdocs-material
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.plugins import PrefixedLogger


def on_config(config: MkDocsConfig):

    config_dir = Path(config.config_file_path).parent

    global CACHE_DIR, ICON_INDEXES
    CACHE_DIR = config_dir / ".cache" / "hooks" / HOOK_NAME

    if not config.mdx_configs.get("pymdownx.emoji"):
        return

    CACHE_DIR.mkdir(parents=True, exist_ok=True)

    if not ICON_INDEXES:
        download_icons()
        load_indexes()
    else:
        LOG.info("Reuse already loaded indexes (restart MkDocs to reload)")

    index_func = config.mdx_configs["pymdownx.emoji"]["emoji_index"]
    config.mdx_configs["pymdownx.emoji"]["emoji_index"] = emoji_decorator(index_func)

    generator_func = config.mdx_configs["pymdownx.emoji"]["emoji_generator"]
    config.mdx_configs["pymdownx.emoji"]["emoji_generator"] = emoji_decorator(generator_func)


def emoji_decorator(func):

    if func.__name__.endswith("wrapper"):
        return func

    def index_wrapper(options, md):
        emoji_index = func(options, md)

        global MATERIAL_INDEX_UPDATED

        if not MATERIAL_INDEX_UPDATED:
            for index in ICON_INDEXES:
                emoji_index["emoji"].update(index)
            MATERIAL_INDEX_UPDATED = True
            LOG.info("Updated icon index with new icons")

        return emoji_index

    def generator_wrapper(index, shortname, alias, uc, alt, title, category, options, md):
        if shortname.startswith(NEW_ICON_PREFIX):
            icons = md.inlinePatterns["emoji"].emoji_index["emoji"]
            el = Element("span", {"class": options.get("classes", index)})
            el.text = md.htmlStash.store(
                '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">'
                + f'<path d="{icons[shortname]["svg_path"]}"></path>'
                + "</svg>"
            )
            return el

        return func(index, shortname, alias, uc, alt, title, category, options, md)

    if func.__name__ == "twemoji":
        return index_wrapper
    else:
        return generator_wrapper


def load_indexes():
    for url in ICON_JSONS_URLS:
        filename = url.rsplit("/", 1)[-1]

        if DOWNLOAD_NEW_PER_WEEK:
            filename = f"{WEEK}-{filename}"

        filepath = CACHE_DIR / filename

        if not filepath.exists():
            LOG.error(f"File should exist at this point: {filepath}")
            continue

        with open(filepath, encoding="utf-8") as file:
            loaded = json.load(file)

        # we expect there to be a data structure with key -> dict pairs
        # skip if incompatible
        data = loaded.get("data")
        if not data:
            LOG.error(f"sap-icon pack has incompatible structure: {filepath}")
            continue

        new_data = {}

        # modify the data to prepare it for index merging
        for key in list(data.keys()):
            name = f"{NEW_ICON_PREFIX}{key.lower().strip()}:"
            new_data[name] = {"name": name, "svg_path": data[key]["path"]}
            del data[key]

        ICON_INDEXES.append(new_data)


def download_icons():
    for url in ICON_JSONS_URLS:
        filename = url.rsplit("/", 1)[-1]

        if DOWNLOAD_NEW_PER_WEEK:
            filename = f"{WEEK}-{filename}"

        filepath = CACHE_DIR / filename

        if filepath.exists():
            continue

        try:
            response = requests.get(url)
        except Exception as err:
            LOG.error(f"Failed to download {url}\n{err}")
            continue

        if response.status_code != 200:
            LOG.error(f"Failed to download {url}\nCode{response.status_code}")
            continue

        if not response.content:
            LOG.error(f"Despite a valid download, byte contents are empty\n{url}")

        filepath.write_bytes(response.content)

        LOG.info(f"Downloaded {filepath}")


HOOK_NAME: str = "sap_icons"
"""Name of the hook"""

CACHE_DIR: Path = None
"""Cache directory to put downloaded files, set later in event"""

DOWNLOAD_NEW_PER_WEEK: bool = True
"""Boolean to decide if the files should update after a week"""

WEEK: int = dt.datetime.now(dt.timezone.utc).isocalendar().week
"""Integer with the week value from ISO calendar"""

ICON_JSONS_URLS: list[str] = [
    "https://raw.githubusercontent.com/SAP/ui5-webcomponents/main/packages/icons/src/v5/SAP-icons.json"
]
"""List with links to JOSN files that contain SVG icon paths"""

ICON_INDEXES: list[dict[str, dict]] = []
"""Global list to store the indexes, filled later in event"""

LOG: PrefixedLogger = PrefixedLogger(HOOK_NAME, logging.getLogger(f"mkdocs.hooks.{HOOK_NAME}"))
"""Logger instance for this hook."""

MATERIAL_INDEX_UPDATED: bool = False
"""Boolean flag to keep track of index modification"""

NEW_ICON_PREFIX: str = ":ext-"
"""Prefix for the added icons to avoid overrides"""
