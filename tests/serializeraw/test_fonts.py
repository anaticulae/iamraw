# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

from yaml import FullLoader
from yaml import load

from iamraw import Font
from iamraw import PageFontContent
from iamraw import Style
from iamraw import Weight
from serializeraw import dump_font_content
from serializeraw import dump_font_header
from serializeraw import load_font_content
from serializeraw import load_font_header

FONT_CONTENT = [
    PageFontContent(
        content=[
            (1, 0, 0, 0),
            (2, 0, 0, 1),
            (3, 0, 0, 2),
            (3, 0, 12, 3),
        ],
        page=3,
    ),
    PageFontContent(
        content=[
            (1, 0, 0, 4),
            (4, 1, 0, 5),
            (5, 0, 0, 6),
            (8, 1, 0, 5),
            (9, 0, 0, 6),
            (17, 0, 0, 5),
            (17, 0, 1, 7),
        ],
        page=5,
    ),
]

FONT_HEADER = [
    Font(name='WLXADN+NimbusSanL', scale=31.1, weight=Weight.BOLD),
    Font(
        name='AJOVIH+NimbusSanL',
        scale=21.7,
        weight=Weight.BOLD,
        style=Style.ITALIC,
    ),
    Font(name='WLXADN+NimbusSanL', scale=21.6, weight=Weight.BOLD),
]


def test_fonts_dump_and_load_font_content():
    dumped = dump_font_content(FONT_CONTENT)
    loaded = load_font_content(dumped)
    assert loaded == FONT_CONTENT


def test_fonts_dump_and_load_font_header():
    dumped = dump_font_header(FONT_HEADER)
    loaded = load_font_header(dumped)
    assert loaded == FONT_HEADER


FONT_HEADER_WITH_DEFAULT = [
    Font(name='WLXADN+NimbusSanL', scale=31.1, weight=Weight.BOLD),
    Font(
        name='AJOVIH+NimbusSanL',
        scale=21.7,
        weight=Weight.BOLD,
        style=Style.ITALIC,
    ),
    Font(name='WLXADN+NimbusSanL', scale=21.6),
]


def test_fonts_remove_default_while_dumping():
    dumped = dump_font_header(FONT_HEADER_WITH_DEFAULT)

    loaded = load(dumped, Loader=FullLoader)
    # first font
    # assert that some keys are there/left
    first_keys = loaded[0]['font']
    assert first_keys
    assert 'style' not in first_keys, str(first_keys)
    assert 'stretch' not in first_keys, str(first_keys)
    # third font
    # assert that some keys are there/left
    third_keys = loaded[2]['font']
    assert third_keys
    assert 'stretch' not in third_keys, str(third_keys)


def test_fonts_dump_and_load_none():
    header_with_none = [
        Font(
            name='WLXADN+NimbusSanL',
            scale=31.1,
            weight=Weight.BOLD,
            stretch=None,
            style=None,
        ),
    ]
    dumped = dump_font_header(header_with_none)
    loaded = load_font_header(dumped)

    assert loaded == header_with_none, str(loaded)
