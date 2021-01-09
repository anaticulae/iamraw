# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================
import iamraw
import serializeraw

EXPECTED = [
    [
        iamraw.Headline(
            title='CHAPTER 1',
            level=1,
            raw_level='1',
            container=0,
            page=6,
        ),
        iamraw.Headline(
            title='RestructuredText Tutorial',
            level=2,
            raw_level='',
            container=1,
            page=6,
        ),
    ],
    [
        iamraw.Headline(
            title='CHAPTER 2',
            level=1,
            raw_level='2',
            container=0,
            page=8,
        ),
        iamraw.Headline(
            title='RestructuredText Guide',
            level=2,
            raw_level='',
            container=1,
            page=8,
        ),
        iamraw.Headline(
            title='Basics',
            level=3,
            raw_level='',
            container=2,
            page=8,
        ),
        iamraw.Headline(
            title='Blockquotes',
            level=3,
            raw_level='',
            container=(10, 12),
            page=9,
        ),
        iamraw.Headline(
            title='Code: Block',
            level=None,
            raw_level='',
            container=10,
            page=9,
        ),
    ],
]


def test_headlines_dump_and_load_headlines():
    """Dump and load the example above"""
    dumped = serializeraw.dump_headlines(EXPECTED)
    loaded = serializeraw.load_headlines(dumped)

    assert loaded == EXPECTED

    loaded = serializeraw.load_headlines(dumped, tuple(range(10)))
    assert len(loaded) == 2


HEADLINE_CONTAINER_RANGE = [
    [
        iamraw.Headline(
            title='CHAPTER 1',
            level=1,
            raw_level='1',
            container=(5, 9),
            page=6,
        ),
        iamraw.Headline(
            title='RestructuredText Tutorial',
            level=2,
            raw_level='',
            container=(0, 5),
            page=6,
        ),
    ],
    [
        iamraw.Headline(
            title='Text Tutorial',
            level=2,
            raw_level='',
            container=0,
            page=6,
        ),
    ],
]


def test_headlines_dump_and_load_headlines_with_rangedcontainer():
    dumped = serializeraw.dump_headlines(HEADLINE_CONTAINER_RANGE)
    loaded = serializeraw.load_headlines(dumped)

    assert loaded == HEADLINE_CONTAINER_RANGE
