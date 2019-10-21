# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import pytest

import iamraw


@pytest.mark.parametrize('bounding, expected_area', [
    (iamraw.BoundingBox(x0=68.61, y0=140.62, x1=543.39, y1=223.71), 39449.47),
    ((68.61, 140.62, 543.39, 223.71), 39449.47),
])
def test_bounding_determine_area(bounding, expected_area):
    area = iamraw.area(bounding)
    assert area == expected_area, f'{area} != {expected_area}'
