# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

from iamraw import BoundingBox
from iamraw import HyperLink
from iamraw import Link
from iamraw import PageLink
from serializeraw import dump_annotations
from serializeraw import load_annotations

EXAMPLE = [
    [[],
     [
         HyperLink(
             goal='http://pythondsp.readthedocs.io/en/latest/pythondsp/toc.html',
             bounds=BoundingBox(
                 x_bottom=351.92, y_bottom=71.00, x_top=401.90, y_top=80.92),
             typ=Link.HYPERLINK)
     ]],
    [[
        PageLink(
            goal='chapter*.1',
            bounds=BoundingBox(
                x_bottom=49.40, y_bottom=571.64, x_top=137.22, y_top=580.50),
            typ=Link.INTERNAL),
        PageLink(
            goal='chapter.1',
            bounds=BoundingBox(
                x_bottom=49.40, y_bottom=549.72, x_top=147.44, y_top=558.59),
            typ=Link.INTERNAL),
        PageLink(
            goal='section.1.1',
            bounds=BoundingBox(
                x_bottom=64.34, y_bottom=535.83, x_top=146.54, y_top=546.62),
            typ=Link.INTERNAL),
    ], []],
    [[],
     [
         HyperLink(
             goal='https://drive.google.com/file/lSkE/view?usp=sharing',
             bounds=BoundingBox(
                 x_bottom=162.90, y_bottom=456.32, x_top=192.31, y_top=467.11),
             typ=Link.HYPERLINK)
     ]],
]


def test_annotation_dump_and_load():
    dumped = dump_annotations(EXAMPLE)

    loaded = load_annotations(dumped)

    assert str(loaded) == str(EXAMPLE)
