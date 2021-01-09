# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import contextlib
import math
from functools import lru_cache

from configo import CACHE_SMALL
from utila import from_raw_or_path
from utila import should_skip
from yaml import FullLoader
from yaml import dump
from yaml import load

import iamraw
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
        if not font['flags']:
            del font['flags']

    result = []
    for item in fonts:
        raw = {
            'font': {
                'name': item.name,
                'scale': item.scale,
                'stretch': item.stretch.name if item.stretch else 'NONE',
                'style': item.style.name if item.style else 'NONE',
                'weight': item.weight.name if item.weight else 'NONE',
                'flags': toflag(item.flags) if item.flags else '',
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
    content = from_raw_or_path(
        content,
        fname='rawmaker__fonts_header',
        ftype='yaml',
    )
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
        flags = None
        with contextlib.suppress(KeyError):
            if fontraw['flags'] != 'NONE':
                flags = convert_flags(fontraw['flags'])

        font = Font(
            name=fontraw['name'],
            scale=fontraw['scale'],
            stretch=stretch,
            style=style,
            weight=weight,
            flags=flags,
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
def load_font_content(content, pages=None):
    content = from_raw_or_path(
        content,
        fname='rawmaker__fonts_content',
        ftype='yaml',
    )
    loaded = load(content, Loader=FullLoader)
    result = []
    for page in loaded:
        pagenumber = int(page['page'])
        if should_skip(pagenumber, pages):
            continue

        def parse_font(pagefonts):
            item = []
            for fontraw in pagefonts:
                item.append(tuple([int(item) for item in fontraw.split()]))
            return item

        pagefonts = page['fonts']
        fonts = parse_font(pagefonts)
        result.append(PageFontContent(content=fonts, page=pagenumber))
    return result


def convert_flags(flag: int) -> iamraw.FontFlags:
    """Parse font flag according to adobe pdf specification.

    >>> convert_flags(3)
    (<FontFlag.FixedPitch: 1>, <FontFlag.Serif: 2>)
    >>> convert_flags(70)
    (<FontFlag.Serif: 2>, <FontFlag.Symbolic: 3>, <FontFlag.Italic: 7>)
    >>> convert_flags(35)
    (<FontFlag.FixedPitch: 1>, <FontFlag.Serif: 2>, <FontFlag.Nonsymbolic: 6>)
    >>> convert_flags(262176)
    (<FontFlag.Nonsymbolic: 6>, <FontFlag.ForceBold: 19>)
    """
    assert flag >= 0, f'negative flag {flag}'
    binary = format(flag, 'b')[::-1]  # reverse binary
    result = []
    for key in iamraw.FontFlag:
        try:
            index = key.value - 1
            value = binary[index]
        except IndexError:
            continue
        else:
            if value == '1':
                result.append(key)
    result = sorted(result, key=lambda x: x.value)
    if not result:
        return None
    return tuple(result)


def toflag(items: iamraw.FontFlags) -> int:
    """Convert tuple of `FontFlag`s to single flag.

    >>> toflag((iamraw.FontFlag.Nonsymbolic, iamraw.FontFlag.ForceBold))
    262176
    """
    result = 0
    for item in items:
        result += math.pow(2, item.value - 1)
    result = int(result)
    return result
