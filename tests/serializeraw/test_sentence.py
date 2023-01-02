# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2022-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import iamraw
import serializeraw

SENTENCES = [
    iamraw.PageContent(
        page=10,
        content=[
            (10, 20, 50, 50),
            (40, 40, 80, 80),
            (40, 60, 80, 100),
            (40, 100, 80, 120),
        ],
    ),
    iamraw.PageContent(
        page=11,
        content=[
            (10, 20, 50, 50),
            (40, 40, 80, 80),
            (
                (40.0, 60, 80, 100),
                (40.0, 100, 80.0, 120),
            ),
            tuple(),
        ],
    )
]


def test_dump_load_sentence():
    dumped = serializeraw.dump_sentence_bounding(SENTENCES)
    loaded = serializeraw.load_sentence_bounding(dumped)
    assert loaded == SENTENCES
