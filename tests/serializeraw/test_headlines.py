# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================
from iamraw import Headline
from serializeraw import dump_headlines
from serializeraw import load_headlines

EXPECTED = [
    [
        Headline(
            text='CHAPTER 1',
            level=1,
            rawlevel='1',
            container=0,
            page=6,
        ),
        Headline(
            text='RestructuredText Tutorial',
            level=2,
            rawlevel='',
            container=1,
            page=6,
        ),
    ],
    [
        Headline(
            text='CHAPTER 2',
            level=1,
            rawlevel='2',
            container=0,
            page=8,
        ),
        Headline(
            text='RestructuredText Guide',
            level=2,
            rawlevel='',
            container=1,
            page=8,
        ),
        Headline(
            text='Basics',
            level=3,
            rawlevel='',
            container=2,
            page=8,
        ),
        Headline(
            text='Blockquotes',
            level=3,
            rawlevel='',
            container=1,
            page=9,
        ),
        Headline(
            text='Code: Block',
            level=3,
            rawlevel='',
            container=10,
            page=9,
        ),
    ],
]


def test_headlines_dump_and_load_headlines():
    """Dump and load the example above"""
    dumped = dump_headlines(EXPECTED)
    loaded = load_headlines(dumped)

    assert loaded == EXPECTED
