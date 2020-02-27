# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import pytest

import iamraw
import serializeraw
import tests.fixtures.textnavigator_style as tft


def test_textnavigator_style_highnotes():
    parsed = iamraw.highnotes(tft.EXAMPLE)
    expected = [iamraw.HighNote(start=20, end=21, value=1)]
    assert parsed == expected, parsed


def test_textnavigator_style_highnotes_remove_highnotes():
    removed = iamraw.remove_highnotes(tft.EXAMPLE)
    expected = tft.EXAMPLE.text[0:20] + tft.EXAMPLE.text[21:]
    assert removed == expected


@pytest.mark.parametrize('expected, merge', [
    (
        iamraw.TextStyle(content=[
            iamraw.CharStyle(start=0, end=20, size=12.0, rise=0.0),
            iamraw.CharStyle(start=20, end=81, size=12.0, rise=0.0),
            iamraw.CharStyle(start=81, end=82, size=12.0, rise=6.0),
        ]),
        False,
    ),
    (
        iamraw.TextStyle(content=[
            iamraw.CharStyle(start=0, end=81, size=12.0, rise=0.0),
            iamraw.CharStyle(start=81, end=82, size=12.0, rise=6.0),
        ]),
        True,
    ),
])
def test_textnavigator_style_remove_hightnotes(expected, merge):
    clean = iamraw.style_without_highnotes(tft.EXAMPLE, merge=merge)
    assert clean == expected


def test_textnavigator_style_dump_and_load_highnotes():
    highnotes = [
        iamraw.PageContentTextItems(
            page=2,
            content=[
                iamraw.HighNote(start=20, end=21, value=1),
                iamraw.HighNote(start=80, end=81, value=3),
                iamraw.HighNote(start=120, end=121, value=5),
            ],
        ),
        iamraw.PageContentTextItems(
            page=5,
            content=[
                iamraw.HighNote(start=80, end=81, value=3),
                iamraw.HighNote(start=120, end=121, value=5),
            ],
        )
    ]
    dumped = serializeraw.dump_highnotes(highnotes)
    loaded = serializeraw.load_highnotes(dumped)

    assert loaded == highnotes
