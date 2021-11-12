# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import contextlib
import functools
import math

import configo
import utila
import yaml

import iamraw


def dump_font_header(fonts) -> str:
    """Write font header to raw string representation"""

    def remove_default_value(font):
        if font['stretch'] == iamraw.DEFAULT_STRETCH.name:
            del font['stretch']
        if font['style'] == iamraw.DEFAULT_STYLE.name:
            del font['style']
        if font['weight'] == iamraw.DEFAULT_WEIGHT.name:
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
                'pdfref': item.pdfref,
            },
        }
        # do not store default value in yaml representation
        remove_default_value(raw['font'])
        result.append(raw)
    dumped = yaml.dump(result)
    return dumped


@functools.lru_cache(configo.CACHE_SMALL)
def load_font_header(content):
    """Load font header from raw string representation.

    There are 3 different states to load. If the key is not defined, the
    `default` value is used. If the value is `NONE` is it replaced by `None`.
    Third, if the state is defined the state is loaded.
    """
    loaded = utila.yaml_load(
        content,
        fname='rawmaker__fonts_header',
    )
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

        weight = parse(fontraw, iamraw.Weight, iamraw.DEFAULT_WEIGHT)
        stretch = parse(fontraw, iamraw.Stretch, iamraw.DEFAULT_STRETCH)
        style = parse(fontraw, iamraw.Style, iamraw.DEFAULT_STYLE)
        flags = None
        with contextlib.suppress(KeyError):
            if fontraw['flags'] != 'NONE':
                flags = convert_flags(fontraw['flags'])

        font = iamraw.Font(
            name=fontraw['name'],
            scale=fontraw['scale'],
            stretch=stretch,
            style=style,
            weight=weight,
            flags=flags,
            pdfref=fontraw.get('pdfref', None),
        )
        fonts.append(font)
    return fonts


def dump_font_content(pages: iamraw.PageFontContents) -> str:
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
    dumped = yaml.dump(result)
    return dumped


@functools.lru_cache(configo.CACHE_SMALL)
def load_font_content(content, pages=None):
    loaded = utila.yaml_load(
        content,
        fname='rawmaker__fonts_content',
    )
    result = []
    for page in loaded:
        pagenumber = int(page['page'])
        if utila.should_skip(pagenumber, pages):
            continue

        def parse_font(pagefonts):
            item = []
            for fontraw in pagefonts:
                item.append(utila.parse_tuple(fontraw, length=4, typ=int))
            return item

        pagefonts = page['fonts']
        fonts = parse_font(pagefonts)
        result.append(iamraw.PageFontContent(content=fonts, page=pagenumber))
    return result


def convert_flags(flag: int) -> iamraw.FontFlags:
    """Parse font flag according to adobe pdf specification.

    >>> convert_flags(3)
    (<FontFlag.FIXEDPITCH: 1>, <FontFlag.SERIF: 2>)
    >>> convert_flags(70)
    (<FontFlag.SERIF: 2>, <FontFlag.SYMBOLIC: 3>, <FontFlag.ITALIC: 7>)
    >>> convert_flags(35)
    (<FontFlag.FIXEDPITCH: 1>, <FontFlag.SERIF: 2>, <FontFlag.NONSYMBOLIC: 6>)
    >>> convert_flags(262176)
    (<FontFlag.NONSYMBOLIC: 6>, <FontFlag.FORCEBOLD: 19>)
    >>> assert convert_flags(0) is None
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

    >>> toflag((iamraw.FontFlag.NONSYMBOLIC, iamraw.FontFlag.FORCEBOLD))
    262176
    >>> toflag([]) + toflag(None)
    0
    """
    if not items:
        return 0
    result = 0
    for item in items:
        result += math.pow(2, item.value - 1)
    result = int(result)
    return result
