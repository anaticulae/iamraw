# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import iamraw
import serializeraw

EXAMPLE = [
    iamraw.PageContent(
        page=10,
        content=[
            ((255, 255, 255), 2000),
            ((0, 255, 0), 609),
            ((222, 12, 100), 50),
        ],
    ),
    iamraw.PageContent(
        page=12,
        content=[
            ((0, 255, 0), 609),
            ((222, 12, 100), 50),
        ],
    ),
]


def test_color_dump_load():
    dumped = serializeraw.dump_color_statistics(EXAMPLE)
    loaded = serializeraw.load_color_statistics(dumped)
    assert loaded == EXAMPLE
