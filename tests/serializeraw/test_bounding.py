# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

from iamraw import BoundingBox
from serializeraw import dump_boundingboxes
from serializeraw import load_boundingboxes
# pylint:disable=W0611
from tests.serializeraw.fixtures import boxdata_from_pdf


def test_bounding_dump_and_load_boundingbox(boxdata_from_pdf):  #pylint:disable=W0621
    _, boxes = boxdata_from_pdf
    dumped = dump_boundingboxes(boxes)
    loaded = load_boundingboxes(dumped)
    assert loaded == boxes

    loaded = load_boundingboxes(dumped, (0, 1, 2))
    assert len(loaded) == 3


def test_bounding_repr():
    example = BoundingBox.from_str('1 2 3 4')
    assert eval(repr(example)) == example  # pylint:disable=eval-used


def test_bounding_round_coordinate():
    example = BoundingBox.from_str('1.033 2.22 3.555 4.4')
    assert example == BoundingBox(1.03, 2.22, 3.56, 4.4)
