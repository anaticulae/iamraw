# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

from serializeraw import dump_text
from serializeraw import load_text
from tests.serializeraw.examples.words import EXAMPLE
from tests.serializeraw.examples.words import HEADLINES


def test_words_dump_and_load_words_result():
    result, headlines = EXAMPLE, HEADLINES
    dumped = dump_text(result)
    loaded = load_text(dumped, headlines)
    assert loaded == result

    loaded = load_text(dumped, headlines, (6, 7, 8, 9))
    assert len(loaded) == 3
