# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import pytest
import utila

import iamraw
import texmex

SAMPLE = [
    (8, iamraw.BoundingBox.from_str('130.91 668.55 540.00 704.02')),
    (6, iamraw.BoundingBox.from_str('358.45 605.24 480.47 625.77')),
    (7, iamraw.BoundingBox.from_str('467.46 650.40 540.00 667.51')),
    (3, iamraw.BoundingBox.from_str('409.67 513.88 540.01 558.02')),
    (4, iamraw.BoundingBox.from_str('550.0 513.88 600.0 558.02')),
    (5, iamraw.BoundingBox.from_str('304.91 587.31 534.01 607.84')),
    (2, iamraw.BoundingBox.from_str('77.38 216.25 121.22 230.47')),
    (0, iamraw.BoundingBox.from_str('303.26 40.18 308.74 54.44')),
    (1, iamraw.BoundingBox.from_str('77.38 102.67 534.62 206.45')),
]


def document_size(items):
    dimension = utila.rect_max(items)
    return (dimension[2], dimension[3])


@pytest.fixture
def navigator() -> texmex.PTN:
    dimension = document_size([item for _, item in SAMPLE])
    result = texmex.PTN(pagesize=dimension)
    for item, position in SAMPLE:
        result.insert(bounding=position, text=str(item), style=None)
    assert len(result) == len(SAMPLE)
    return result
