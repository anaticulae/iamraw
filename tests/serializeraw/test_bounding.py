# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import iamraw
import serializeraw
# pylint:disable=W0611
from tests.serializeraw.fixtures import boxdata_from_pdf


def test_bounding_dump_and_load_boundingbox(boxdata_from_pdf):  #pylint:disable=W0621
    _, boxes = boxdata_from_pdf
    dumped = serializeraw.dump_boundingboxes(boxes)
    loaded = serializeraw.load_boundingboxes(dumped)
    assert loaded == boxes

    loaded = serializeraw.load_boundingboxes(dumped, pages=(0, 1, 2))
    assert len(loaded) == 3


def test_bounding_repr():
    # required for eval statement
    from iamraw import BoundingBox  # pylint:disable=C0415
    example = iamraw.BoundingBox.from_str('1 2 3 4')
    assert eval(repr(example)) == example  # pylint:disable=eval-used # nosec


def test_bounding_round_coordinate():
    example = iamraw.BoundingBox.from_str('1.033 2.22 3.555 4.4')
    assert example == iamraw.BoundingBox(1.03, 2.22, 3.56, 4.4)
