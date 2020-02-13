# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import iamraw
import serializeraw


def example() -> iamraw.PageContentHits:
    result = [
        iamraw.PageContentHit(
            page=5,
            border=iamraw.Border(72.00, 39.95, 540.00, 758.84),
            hits=[
                (81, (539.80, 411.42, 543.99, 706.05)),
                (83, (75.98, 411.42, 543.99, 415.61)),
                (132, (69.01, 441.64, 542.99, 458.58)),
                (133, (68.81, 441.64, 68.81, 458.58)),
                (134, (543.19, 441.64, 543.19, 458.58)),
                (135, (68.61, 458.78, 543.39, 458.78)),
            ],
        ),
        iamraw.PageContentHit(
            page=7,
            border=iamraw.Border(78.00, 39.95, 540.00, 758.84),
            hits=[
                (145, (539.80, 411.42, 543.99, 706.05)),
                (180, (75.98, 411.42, 543.99, 415.61)),
            ],
        ),
    ]
    return result


def test_load_and_dump_hits():
    raw = example()
    dumped = serializeraw.dump_hits(raw)
    loaded = serializeraw.load_hits(dumped)
    assert loaded == raw
