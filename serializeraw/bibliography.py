# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import dataclasses

import utila

import iamraw


def dump_bibliography_reference(references: iamraw.BibliographyReferences) -> str: # yapf:disable
    r"""\
    >>> dump_bibliography_reference(iamraw.BibliographyTable(headline='Bibliography', references=[]))
    "__strategy__: null\nheadline: Bibliography\npdfpages: ''\nreferences: []\n"
    """
    if not isinstance(references, iamraw.BibliographyTable):
        # TODO: REMOVE OUTDATED DUMP WITH NEW MAJOR
        result = []
        for page in references:
            result.append([dataclasses.asdict(item) for item in page])
        dumped = utila.yaml_dump(result)
        return dumped
    return dump_bib_table(references)


def dump_bib_table(table: iamraw.BibliographyTable) -> str:
    assert table.references is not None, str(table)
    if table.pdfpages is not None:
        pdfpages = utila.from_tuple(table.pdfpages)
    else:
        pdfpages = ''
    raw = dict(
        headline=table.headline,
        pdfpages=pdfpages,
        references=[dataclasses.asdict(item) for item in table.references],
        __strategy__=table.__strategy__,
    )
    dumped = utila.yaml_dump(raw)
    return dumped


def load_bibliography_reference(content: str) -> iamraw.BibliographyReferences:
    """\
    >>> load_bibliography_reference(dump_bibliography_reference(
    ... iamraw.BibliographyTable(headline='Bibliography', references=[])))
    BibliographyTable(headline='Bibliography', references=[], pdfpages='')
    """
    loaded = utila.yaml_load(
        content,
        fname=(
            'bibliography__result_result',
            'detector__bibliography_detected',
        ),
    )
    if isinstance(loaded, list):
        result = []
        for page in loaded:
            references = [iamraw.BibliographyReference(**item) for item in page]
            result.append(references)
        for page in result:
            for item in page:
                item.authors = load_authors(item.authors)
        return result
    return load_bib_table(loaded)


def load_bib_table(table: dict) -> iamraw.BibliographyTable:
    headline = table.get('headline', '')
    pdfpages = table.get('pdfpages', None)
    if pdfpages:
        pdfpages = utila.parse_tuple(pdfpages, length=None, typ=int)
    references = table.get('references', [])
    strategy = table.get('__strategy__', None)
    result = iamraw.BibliographyTable(
        headline=headline,
        pdfpages=pdfpages,
        references=[load_reference(item) for item in references],
    )
    result.__strategy__ = strategy
    return result


def load_reference(raw):
    item = iamraw.BibliographyReference(**raw)
    item.authors = load_authors(item.authors)
    return item


def load_authors(authors: list) -> list:
    # parse complex authors correctly
    result = []
    for author in authors:
        if not isinstance(author, dict):
            # TODO: IS TUPLE SO IMPORTANT HERE?
            result.append(tuple(author))
            continue
        if 'firstname' in author:
            result.append(iamraw.Person(**author))
            continue
        result.append(iamraw.NoPerson(**author))
    return result
