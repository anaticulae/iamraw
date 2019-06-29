# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

from iamraw import Font
from iamraw import Stretch
from iamraw import Style
from iamraw import Weight
from serializeraw import dump_font_content
from serializeraw import dump_font_header
from serializeraw import load_font_content
from serializeraw import load_font_header

FONT_CONTENT = [
    [(1, 0, 0, 0), (2, 0, 0, 1), (3, 0, 0, 2), (3, 0, 12, 3)],
    [],
    [(1, 0, 0, 4), (4, 1, 0, 5), (5, 0, 0, 6), (8, 1, 0, 5), (9, 0, 0, 6),
     (17, 0, 0, 5), (17, 0, 1, 7)],
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
