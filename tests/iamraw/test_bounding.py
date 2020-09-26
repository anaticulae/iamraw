# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import iamraw


def test_bounding_split_x():
    bounding = iamraw.BoundingBox(50, 50, 100, 100)
    equal = iamraw.split_x(bounding, 0, 1)

    assert equal == bounding

    first = iamraw.split_x(bounding, 0, 2)
    assert first == iamraw.BoundingBox(50, 50, 75, 100)

    second = iamraw.split_x(bounding, 1, 2)
    assert second == iamraw.BoundingBox(75, 50, 100, 100)


def test_bounding_split_y():
    bounding = iamraw.BoundingBox(50, 50, 100, 100)
    equal = iamraw.split_y(bounding, 0, 1)

    assert equal == bounding

    first = iamraw.split_y(bounding, 0, 2)
    assert first == iamraw.BoundingBox(50, 50, 100, 75)

    second = iamraw.split_y(bounding, 1, 2)
    assert second == iamraw.BoundingBox(50, 75, 100, 100)


def test_bounding_location_from_str():
    example = 'b(123.5;100.0;500.0;500.0)p5'
    parsed = iamraw.BoundingLocation.fromstr(example)

    assert parsed.value == (123.5, 100.0, 500.0, 500.0), parsed.value


def test_bounding_location_dump_load():
    example = iamraw.BoundingLocation.fromtuple(
        (5.0, 10.0, 50.0, 50.0),
        page=36,
    )
    dumped = str(example)
    loaded = iamraw.BoundingLocation.fromstr(dumped)
    assert loaded == example
