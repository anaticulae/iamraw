# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import serializeraw
import tests.serializeraw.examples.list


def test_words_list_dump_and_load_lists():
    dumped = serializeraw.dump_lists(tests.serializeraw.examples.list.EXAMPLE)
    loaded = serializeraw.load_lists(dumped)

    assert loaded == tests.serializeraw.examples.list.EXAMPLE
    loaded = serializeraw.load_lists(dumped, (8, 24))
    assert len(loaded) == 2
