# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================
from iamraw import BoundingBox
from iamraw import Box
from iamraw import HorizontalLine
from serializeraw import dump_boxes
from serializeraw import dump_horizontals
from serializeraw import load_boxes
from serializeraw import load_horizontals


def test_dump_and_load_boxes():
    pages = [
        [Box(box=BoundingBox(72.20, 160.88, 539.80, 238.48))],
        [
            Box(box=BoundingBox(68.61, 673.57, 543.39, 715.82)),
            Box(box=BoundingBox(68.61, 83.07, 543.39, 448.10))
        ],
        [
            Box(box=BoundingBox(68.61, 640.70, 543.39, 706.85)),
            Box(box=BoundingBox(68.61, 80.17, 543.39, 457.16))
        ],
        [Box(box=BoundingBox(68.61, 90.76, 543.39, 706.85))],
        [Box(box=BoundingBox(68.61, 80.17, 543.39, 347.04))],
        [Box(box=BoundingBox(68.61, 80.17, 543.39, 706.85))],
        [Box(box=BoundingBox(68.61, 80.17, 543.39, 706.85))],
        [Box(box=BoundingBox(68.61, 604.83, 543.39, 706.85))],
        [],
    ]

    dumped = dump_boxes(pages)

    assert dumped
    assert len(dumped) > 100

    loaded = load_boxes(dumped)
    assert loaded == pages


def test_dump_and_load_horizontal():
    pages = [
        [
            HorizontalLine(box=BoundingBox(72.00, 298.76, 540.00, 298.76)),
            HorizontalLine(box=BoundingBox(72.00, 710.53, 540.00, 710.53))
        ],
        [],
        [
            HorizontalLine(box=BoundingBox(72.00, 298.76, 540.00, 298.76)),
        ],
        [],
        [],
    ]

    dumped = dump_horizontals(pages)

    assert dumped
    assert len(dumped) > 100

    loaded = load_horizontals(dumped)
    assert loaded == pages
