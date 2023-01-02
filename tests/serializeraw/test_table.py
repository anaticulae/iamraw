# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import iamraw
import serializeraw

EXAMPLE = [
    iamraw.PageContentTableBounding(
        page=2,
        content=[
            iamraw.TableBounding(
                bounding=(115.37, 532.84, 479.91, 767.56),
                lines=[
                    (210.49, 755.4, 210.49, 767.36),
                    (210.49, 743.05, 210.49, 755.0),
                    (210.49, 730.7, 210.49, 742.65),
                    (210.49, 718.34, 210.49, 730.3),
                    (210.49, 705.99, 210.49, 717.94),
                    (210.49, 693.63, 210.49, 705.59),
                    (210.49, 681.28, 210.49, 693.24),
                    (210.49, 668.93, 210.49, 680.88),
                    (210.49, 656.57, 210.49, 668.53),
                    (210.49, 644.22, 210.49, 656.18),
                    (210.49, 631.87, 210.49, 643.82),
                    (210.49, 619.51, 210.49, 631.47),
                    (115.37, 767.56, 479.91, 767.56),
                    (115.37, 755.2, 479.91, 755.2),
                    (115.37, 742.85, 479.91, 742.85),
                    (115.37, 730.5, 479.91, 730.5),
                    (479.71, 533.04, 479.71, 544.99),
                ],
                page=2,
            ),
        ],
    )
]


def test_table_dump_and_load():
    dumped = serializeraw.dump_tables(EXAMPLE)
    loaded = serializeraw.load_tables(dumped)
    assert loaded == EXAMPLE
