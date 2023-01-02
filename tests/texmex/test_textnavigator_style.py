# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import pytest

import serializeraw
import tests.fixtures.style
import texmex


def test_textnavigator_style_highnotes():
    parsed = texmex.highnotes(tests.fixtures.style.EXAMPLE)
    expected = [texmex.HighNote(start=20, end=21, value=1)]
    assert parsed == expected, parsed


def test_textnavigator_style_highnotes_remove_highnotes():
    example = tests.fixtures.style.EXAMPLE
    removed = texmex.remove_highnotes(example)
    expected = example.text[0:20] + example.text[21:]
    assert removed == expected


def test_remove_highnote_magic():
    removed = texmex.remove_highnotes(tests.fixtures.style.EXAMPLE, magic=True)
    assert 'Internetnutzer{{hn:1:nh}} waren' in removed


@pytest.mark.parametrize('expected, merge', [
    (
        texmex.TextStyle(content=[
            texmex.CharStyle(start=0, end=20, size=12.0, rise=0.0),
            texmex.CharStyle(start=20, end=81, size=12.0, rise=0.0),
            texmex.CharStyle(start=81, end=82, size=12.0, rise=6.0),
        ]),
        False,
    ),
    (
        texmex.TextStyle(content=[
            texmex.CharStyle(start=0, end=81, size=12.0, rise=0.0),
            texmex.CharStyle(start=81, end=82, size=12.0, rise=6.0),
        ]),
        True,
    ),
])
def test_textnavigator_style_remove_hightnotes(expected, merge):
    clean = texmex.style_without_highnotes(
        tests.fixtures.style.EXAMPLE,
        merge=merge,
    )
    assert clean == expected


def test_textnavigator_style_dump_and_load_highnotes():
    highnotes = [
        texmex.PageContentTextItems(
            page=2,
            content=[
                texmex.HighNote(start=20, end=21, value=1),
                texmex.HighNote(start=80, end=81, value=3),
                texmex.HighNote(start=120, end=121, value=5),
            ],
        ),
        texmex.PageContentTextItems(
            page=5,
            content=[
                texmex.HighNote(start=80, end=81, value=3),
                texmex.HighNote(start=120, end=121, value=5),
            ],
        )
    ]
    dumped = serializeraw.dump_highnotes(highnotes)
    loaded = serializeraw.load_highnotes(dumped)
    assert loaded == highnotes
