# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utilo

from iamraw import BoundingBox
from iamraw import Box
from iamraw import HorizontalLine
from iamraw import PageContentBoxes
from iamraw import PageContentHorizontals
from serializeraw import dump_boxes
from serializeraw import dump_horizontals
from serializeraw import load_boxes
from serializeraw import load_horizontals


def test_dump_and_load_boxes():
    pages = [
        PageContentBoxes(
            content=[
                Box(box=BoundingBox(72.20, 160.88, 539.80, 238.48)),
            ],
            page=2,
        ),
        PageContentBoxes(
            content=[
                Box(box=BoundingBox(68.61, 673.57, 543.39, 715.82)),
                Box(box=BoundingBox(68.61, 83.07, 543.39, 448.10)),
            ],
            page=3,
        ),
        PageContentBoxes(
            content=[
                Box(box=BoundingBox(68.61, 640.70, 543.39, 706.85)),
                Box(box=BoundingBox(68.61, 80.17, 543.39, 457.16)),
            ],
            page=4,
        ),
        PageContentBoxes(
            content=[Box(box=BoundingBox(68.61, 90.76, 543.39, 706.85))],
            page=5),
        PageContentBoxes(
            content=[Box(box=BoundingBox(68.61, 80.17, 543.39, 347.04))],
            page=6,
        ),
        PageContentBoxes(
            content=[Box(box=BoundingBox(68.61, 80.17, 543.39, 706.85))],
            page=7,
        ),
        PageContentBoxes(
            content=[Box(box=BoundingBox(68.61, 604.83, 543.39, 706.85))],
            page=8,
        ),
    ]

    dumped = dump_boxes(pages)

    assert dumped
    assert len(dumped) > 100

    loaded = load_boxes(dumped)
    assert loaded == pages

    loaded = load_boxes(dumped, (2, 3, 4, 5, 6, 7, 8))
    assert len(loaded) == 7


def test_dump_and_load_horizontal():
    pages = [
        PageContentHorizontals(
            content=[
                HorizontalLine(box=BoundingBox(72.00, 298.76, 540.00, 298.76)),
                HorizontalLine(box=BoundingBox(72.00, 710.53, 540.00, 710.53))
            ],
            page=1,
        ),
        PageContentHorizontals(
            content=[
                HorizontalLine(box=BoundingBox(72.00, 298.76, 540.00, 298.76)),
            ],
            page=5,
            rotated=True,
        ),
    ]

    dumped = dump_horizontals(pages)
    assert dumped
    assert len(dumped) > 100
    loaded = load_horizontals(dumped)
    assert loaded == pages


def test_boxes_rectangle_max_box():
    left_bottom = BoundingBox.from_list([0.0, 0.0, 100.0, 100.0])
    middle = BoundingBox.from_list([-25.0, 25.0, 50.0, 100.0])
    right_top = BoundingBox.from_list([75.0, 75.0, 150.0, 150.0])

    merged = utilo.rect_max([left_bottom, middle, right_top])
    expected = (-25.0, 0.0, 150.0, 150.0)
    assert merged == expected
