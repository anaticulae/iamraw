# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import iamraw
import serializeraw

EXAMPLE = [
    [
        iamraw.BibliographyReference.create('Fahrendholz Konrad', year=2016),
        iamraw.BibliographyReference.create('Fahrendholz Konrad', year=None),
        iamraw.BibliographyReference.create('Fahrendholz Konrad', year=1987),
    ],
]


def test_bibliography_dump_load():
    dumped = serializeraw.dump_bibliography_reference(EXAMPLE)
    loaded = serializeraw.load_bibliography_reference(dumped)
    assert loaded == EXAMPLE


def test_bibliography_author():
    author = iamraw.BibliographyReference.create('Fahrendholz Konrad')
    assert author.author == 'Fahrendholz'
