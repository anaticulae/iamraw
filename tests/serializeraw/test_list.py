# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import serializeraw
import tests.serializeraw.examples.list


def test_dump_load_list():
    expected = tests.serializeraw.examples.list.EXAMPLE
    dumped = serializeraw.dump_lists(expected)
    loaded = serializeraw.load_lists(dumped)
    assert loaded == expected
    loaded = serializeraw.load_lists(dumped, (8, 24))
    assert len(loaded) == 2
