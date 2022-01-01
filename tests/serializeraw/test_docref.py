# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import iamraw
import serializeraw

DOC_REFERENCE = [
    iamraw.DocRef(page=7, sentence=5, marked=[(31, 36)]),
    iamraw.DocRef(page=9, sentence=7, marked=[(44, 49)]),
    iamraw.DocRef(page=14, sentence=2, marked=[(33, 38)]),
    iamraw.DocRef(page=15, sentence=0, marked=[(2, 7)]),
    iamraw.DocRef(page=20, sentence=3, marked=[(22, 29), (40, 45)]),
]


def test_dump_and_load_docref():
    dumped = serializeraw.dump_docref(DOC_REFERENCE)
    loaded = serializeraw.load_docref(dumped)
    assert loaded == DOC_REFERENCE
