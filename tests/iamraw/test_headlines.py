# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import iamraw


def test_headline_start_end():
    ranged = iamraw.Headline(
        title='RestructuredText Tutorial',
        level=2,
        container=(1, 5),
        page=6,
    )
    assert ranged.start == 1
    assert ranged.end == 5

    not_ranged = iamraw.Headline(
        title='RestructuredText Tutorial',
        level=2,
        container=3,
        page=6,
    )
    assert not_ranged.start == 3
    assert not_ranged.end == 3
