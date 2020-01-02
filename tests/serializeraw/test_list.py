# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

from serializeraw import dump_lists
from serializeraw import load_lists
from tests.serializeraw.examples.list import EXAMPLE


def test_words_list_dump_and_load_lists():
    result = EXAMPLE

    dumped = dump_lists(result)
    loaded = load_lists(dumped)
    assert loaded == result
    loaded = load_lists(dumped, (8, 24))
    assert len(loaded) == 2
