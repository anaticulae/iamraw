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

FINDINGS = [
    iamraw.Finding(number=10),
    iamraw.Finding(number=11, location=iamraw.Location(page=5)),
    iamraw.Finding(number=12, location=iamraw.Location(page=5)),
]


def test_dump_and_load_findings():
    dumped = serializeraw.dump_findings(FINDINGS)
    loaded = serializeraw.load_findings(dumped)
    assert loaded == FINDINGS


def test_select_pages():
    dumped = serializeraw.dump_findings(FINDINGS)
    loaded = serializeraw.load_findings(dumped, pages=5)
    assert len(loaded) == 2
