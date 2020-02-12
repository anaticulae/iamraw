# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utila

import serializeraw
import tests.serializeraw


def test_load_and_dump_hits():
    expected = utila.file_read(tests.serializeraw.HITS_YAML)
    border, hits = serializeraw.load_hits(tests.serializeraw.HITS_YAML)
    assert border, hits

    dumped = serializeraw.dump_hits(border, hits)
    assert dumped == expected

    loaded_border, loaded_hits = serializeraw.load_hits(dumped)
    assert loaded_border == border
    assert loaded_hits == hits
