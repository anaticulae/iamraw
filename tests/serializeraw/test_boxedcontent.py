# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

from serializeraw import dump_boxedcontent
from serializeraw import load_boxedcontent
from tests.serializeraw.examples.boxedcontent import EXAMPLE


def test_words_boxed_dump_and_load():
    dumped = dump_boxedcontent(EXAMPLE)

    loaded = load_boxedcontent(dumped)
    assert loaded == EXAMPLE
