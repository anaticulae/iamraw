# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import iamraw
import serializeraw

EXAMPLE = [
    [
        iamraw.BibliographyReference.create('Schewe Konrad', year=2016),
        iamraw.BibliographyReference.create('Schewe Konrad', year=None),
        iamraw.BibliographyReference.create('Schewe Konrad', year=1987),
    ],
]


def test_bibliography_dump_load():
    dumped = serializeraw.dump_bibliography_reference(EXAMPLE)
    loaded = serializeraw.load_bibliography_reference(dumped)
    assert loaded == EXAMPLE


def test_bibliography_author():
    author = iamraw.BibliographyReference.create('Schewe Konrad')
    assert author.author == 'Schewe'


def test_bibliographytable_dump_load():
    references = EXAMPLE[0]
    table = iamraw.BibliographyTable(
        headline='References',
        references=references,
        pdfpages=(4, 5, 6, 7),
    )
    dumped = serializeraw.dump_bibliography_reference(table)
    loaded = serializeraw.load_bibliography_reference(dumped)
    assert loaded == table
