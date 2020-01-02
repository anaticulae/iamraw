# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

from utila import file_read

from serializeraw import dump_hits
from serializeraw import load_hits
from tests.serializeraw import HITS_YAML


def test_load_and_dump_hits():
    expected = file_read(HITS_YAML)
    border, hits = load_hits(HITS_YAML)
    assert border, hits

    dumped = dump_hits(border, hits)
    assert dumped == expected

    loaded_border, loaded_hits = load_hits(dumped)
    assert loaded_border == border
    assert loaded_hits == hits
