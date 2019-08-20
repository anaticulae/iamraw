# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import iamraw
import serializeraw

EXAMPLE = [
    iamraw.PageContentLikelihood(
        page=0,
        content=[
            iamraw.Likelihood(0.99, 'header'),
            iamraw.Likelihood(0.5, 'title'),
            iamraw.Likelihood(0.1),
        ],
    ),
    iamraw.PageContentLikelihood(
        page=2,
        content=[
            iamraw.Likelihood(0.1),
            iamraw.Likelihood('Hello'),
        ],
    ),
    iamraw.PageContentLikelihood(
        page=3,
        content=[],
    ),
]


def test_likelihood_dump_and_load():
    dumped = serializeraw.dump_likelihood(EXAMPLE)
    loaded = serializeraw.load_likelihood(dumped)

    # Dump removes empty page 3
    assert loaded == EXAMPLE[0:2], str(loaded)


def test_likelihood_dump_and_load_page2():
    dumped = serializeraw.dump_likelihood(EXAMPLE)
    loaded = serializeraw.load_likelihood(dumped, pages=(2))

    subexample = [EXAMPLE[1]]
    assert loaded == subexample, str(loaded)
