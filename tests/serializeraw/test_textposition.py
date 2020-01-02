# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================
from iamraw import BoundingBox
from iamraw import PageContentTextPosition
from serializeraw import dump_textpositions
from serializeraw import load_textpositions

EXAMPLE = [
    PageContentTextPosition(
        content={
            0: BoundingBox.from_str('0 1 2 3'),
            5: BoundingBox.from_str('2 2 2 2'),
        },
        page=0,
    ),
    PageContentTextPosition(
        content={
            1: BoundingBox.from_str('2 1 2 3'),
            3: BoundingBox.from_str('4 2 6 2'),
        },
        page=3,
    ),
    PageContentTextPosition(
        content={
            0: BoundingBox.from_str('2 2 2 2'),
            1: BoundingBox.from_str('1 2 6 5'),
        },
        page=4,
    ),
]


def test_textpositions_dump_and_load_texpositions():
    dumped = dump_textpositions(EXAMPLE)
    loaded = load_textpositions(dumped)

    assert loaded == EXAMPLE

    loaded = load_textpositions(dumped, (0, 3))
    assert len(loaded) == 2
