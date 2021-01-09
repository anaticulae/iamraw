# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================
import iamraw
import serializeraw

EXAMPLE = [
    iamraw.PageContentLine(
        page=0,
        content=[
            (72.0, 81.47, 540.0, 81.47),
            (72.0, 493.24, 540.0, 493.24),
            (72.2, 553.52, 72.2, 631.12),
            (72.4, 553.72, 539.6, 553.72),
            (72.4, 630.92, 539.6, 630.92),
            (75.98, 633.01, 543.99, 633.01),
            (539.8, 553.52, 539.8, 631.12),
            (541.89, 557.5, 541.89, 635.1),
        ]),
    iamraw.PageContentLine(
        page=1,
        content=[
            (68.61, 76.18, 543.39, 76.18),
            (68.61, 118.43, 543.39, 118.43),
            (68.61, 343.9, 543.39, 343.9),
            (68.61, 708.93, 543.39, 708.93),
            (68.81, 76.38, 68.81, 118.23),
            (68.81, 344.1, 68.81, 708.73),
            (543.19, 76.38, 543.19, 118.23),
            (543.19, 344.1, 543.19, 708.73),
        ]),
]


def test_line_dump_load():
    dumped = serializeraw.dump_lines(EXAMPLE)
    loaded = serializeraw.load_lines(dumped)
    assert loaded == EXAMPLE
