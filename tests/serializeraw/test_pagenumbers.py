# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

from pytest import mark

from serializeraw import dump_pagenumbers
from serializeraw import load_pagenumbers
from tests.serializeraw.examples.pagenumbers import SINGLE_PAGES
from tests.serializeraw.examples.pagenumbers import TWO_PAGES


@mark.parametrize('pages', [SINGLE_PAGES, TWO_PAGES])
def test_dump_and_load_pagenumbers(pages):
    dumped = dump_pagenumbers(pages)
    assert len(dumped) > 200, str(dumped)
    loaded = load_pagenumbers(dumped)

    assert loaded == pages
