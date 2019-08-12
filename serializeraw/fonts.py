# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

from functools import lru_cache

from configo import CACHE_SMALL
from utila import from_raw_or_path
from yaml import FullLoader
from yaml import dump
from yaml import load

from iamraw import DEFAULT_STRETCH
from iamraw import DEFAULT_STYLE
from iamraw import DEFAULT_WEIGHT
from iamraw import Font
from iamraw import PageFontContent
from iamraw import PageFontContents
from iamraw import Stretch
from iamraw import Style
from iamraw import Weight


def dump_font_header(fonts) -> str:
    """Write font header to raw string representation"""

    def remove_default_value(font):
        if font['stretch'] == DEFAULT_STRETCH.name:
            del font['stretch']
        if font['style'] == DEFAULT_STYLE.name:
            del font['style']
        if font['weight'] == DEFAULT_WEIGHT.name:
            del font['weight']

    result = []
    for index, item in enumerate(fonts):
        raw = {
            'index': index,
            'font': {
                'name': item.name,
                'scale': item.scale,
                'stretch': item.stretch.name if item.stretch else 'NONE',
                'style': item.style.name if item.style else 'NONE',
                'weight': item.weight.name if item.weight else 'NONE',
            },
        }
        # do not store default value in yaml representation
        remove_default_value(raw['font'])
        result.append(raw)
    dumped = dump(result)
    return dumped


@lru_cache(CACHE_SMALL)
def load_font_header(content):
    """Load font header from raw string representation.

    There are 3 different states to load. If the key is not defined, the
    `default` value is used. If the value is `NONE` is it replaced by `None`.
    Third, if the state is defined the state is loaded.
    """
    content = from_raw_or_path(content, ftype='yaml')
    loaded = load(content, Loader=FullLoader)

    fonts = []
    for item in loaded:
        fontraw = item['font']

        def parse(raw, ctor, default):
            key = str(default.__class__.__name__.lower())
            try:
                if raw[key] == 'NONE':
                    return None
                return ctor[raw[key]]
            except KeyError:
                return default

        weight = parse(fontraw, Weight, DEFAULT_WEIGHT)
        stretch = parse(fontraw, Stretch, DEFAULT_STRETCH)
        style = parse(fontraw, Style, DEFAULT_STYLE)

        font = Font(
            name=fontraw['name'],
            scale=fontraw['scale'],
            stretch=stretch,
            style=style,
            weight=weight,
        )
        fonts.append(font)
    return fonts


def dump_font_content(pages: PageFontContents) -> str:
    assert pages
    result = []
    for page in pages:
        items = []
        for item in page.content:
            raw = '%d %d %d %d' % item  #  (container, line, char, fontkey)
            items.append(raw)
        result.append({
            'page': page.page,
            'fonts': items,
        })
    dumped = dump(result)
    return dumped


@lru_cache(CACHE_SMALL)
def load_font_content(content):
    content = from_raw_or_path(content, ftype='yaml')
    loaded = load(content, Loader=FullLoader)
    result = []
    for page in loaded:
        number = int(page['page'])
        item = []
        for fontraw in page['fonts']:
            item.append(tuple([int(item) for item in fontraw.split()]))
        result.append(PageFontContent(content=item, page=number))
    return result
