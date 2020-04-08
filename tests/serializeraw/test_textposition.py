# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import iamraw
from iamraw import BoundingBox
from iamraw import PageContentTextPosition
from serializeraw import dump_textpositions
from serializeraw import load_textpositions

EXAMPLE = [
    PageContentTextPosition(
        content={
            0: iamraw.TextPosition(BoundingBox.from_str('0 1 2 3'), 0.0),
            5: iamraw.TextPosition(BoundingBox.from_str('2 2 2 2'), 0.0),
        },
        page=0,
    ),
    PageContentTextPosition(
        content={
            1: iamraw.TextPosition(BoundingBox.from_str('2 1 2 3'), 0.5),
            3: iamraw.TextPosition(BoundingBox.from_str('4 2 6 2'), 0.5),
        },
        page=3,
    ),
    PageContentTextPosition(
        content={
            0: iamraw.TextPosition(BoundingBox.from_str('2 2 2 2'), 0.5),
            1: iamraw.TextPosition(BoundingBox.from_str('1 2 6 5'), 1.0),
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
