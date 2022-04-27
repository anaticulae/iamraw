# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import iamraw
import serializeraw

CONTENT = [
    iamraw.PageContentCode(
        page=10,
        content=[
            iamraw.PeaceOfCode(
                caption=(10, 11),
                tokens=(6, 7, 8, 9),
                tokens_bounding=[
                    (10.0, 12.0, 30.0, 40.0),
                    (10.2, 16.0, 30.0, 42.0),
                ],
                caption_bounding=[
                    (10.2, 12.2, 30.2, 40.2),
                ],
                page=10,
            ),
            iamraw.PeaceOfCode(page=10),
        ],
    )
]


def test_codes_dump_load():
    dumped = serializeraw.dump_codes(CONTENT)
    loaded = serializeraw.load_codes(dumped)
    assert loaded == CONTENT
