# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utila

import iamraw
import serializeraw


def load_docinfo(path: str, pages: tuple = None) -> iamraw.DocInfo:  # pylint:disable=W0613
    # TODO: USE PAGES SELECTOR
    loaded = utila.yaml_load(
        path,
        fname='sections__docinfo_docinfo',
        safe=False,
    )
    return loaded


def dump_docinfo(docinfo: iamraw.DocInfo) -> str:
    dumped = utila.yaml_dump(docinfo, safe=False)
    return dumped


def create_docinfo(
    sections: str,
    pdfinfo: str = None,
    pages: tuple = None,
) -> 'iamraw.SectionLookup':
    sections = serializeraw.load_sections(content=sections, pages=pages)
    lookup = iamraw.SectionLookup(sections=sections)
    result = iamraw.DocInfo(sections=lookup)
    if utila.exists(pdfinfo):
        pdfinfo = serializeraw.load_pdfinfo(pdfinfo)
        result.pages = pdfinfo.pages
        result.generator = pdfinfo.generator
    return result
