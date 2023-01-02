# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

from iamraw import BoundingBox
from iamraw import HyperLink
from iamraw import Link
from iamraw import PageAnnotation
from iamraw import PageLink
from serializeraw import dump_annotations
from serializeraw import load_annotations

EXAMPLE = [
    PageAnnotation(
        [],
        [
            HyperLink(
                goal=
                'http://pythondsp.readthedocs.io/en/latest/pythondsp/toc.html',
                bounds=BoundingBox(x0=351.92, y0=71.00, x1=401.90, y1=80.92),
                typ=Link.HYPERLINK)
        ],
        page=0,
    ),
    PageAnnotation(
        [
            PageLink(goal='chapter*.1',
                     bounds=BoundingBox(
                         x0=49.40, y0=571.64, x1=137.22, y1=580.50),
                     typ=Link.INTERNAL),
            PageLink(goal='chapter.1',
                     bounds=BoundingBox(
                         x0=49.40, y0=549.72, x1=147.44, y1=558.59),
                     typ=Link.INTERNAL),
            PageLink(goal='section.1.1',
                     bounds=BoundingBox(
                         x0=64.34, y0=535.83, x1=146.54, y1=546.62),
                     typ=Link.INTERNAL),
        ],
        [],
        page=3  # we do not need `full` ascending pages
    ),
    PageAnnotation(
        [],
        [
            HyperLink(
                goal='https://drive.google.com/file/lSkE/view?usp=sharing',
                bounds=BoundingBox(x0=162.90, y0=456.32, x1=192.31, y1=467.11),
                typ=Link.HYPERLINK)
        ],
        page=4,
    ),
    # test to skip empty PageAnnoation
    PageAnnotation(
        [],
        [],
        page=6,
    ),
]


def test_annotation_dump_and_load():
    dumped = dump_annotations(EXAMPLE)
    loaded = load_annotations(dumped)
    # empty Annotations are not serialized
    example_without_last_one = EXAMPLE[:-1]
    assert loaded == example_without_last_one

    loaded = load_annotations(dumped, pages=(0, 4, 5))
    assert len(loaded) == 2
