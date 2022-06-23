# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utila

import iamraw
import serializeraw


def dumper(boundings) -> list:
    result = []
    for bounding in boundings:
        single = utila.from_tuple(bounding)
        result.append(single)
    return result


def dump_sentence_bounding(sentences: iamraw.PageContents) -> str:
    result = serializeraw.dump_pagecontent(
        pages=sentences,
        pagedumper=dumper,
    )
    return result


def loader(boundings) -> list:
    result = []
    for bounding in boundings:
        single = utila.parse_tuple(bounding)
        result.append(single)
    return result


def load_sentence_bounding(
    source: str,
    pages: tuple = None,
) -> iamraw.PageContents:
    result = serializeraw.load_pagecontent(
        content=source,
        pages=pages,
        pageloader=loader,
        fname='words__sentences_bounding',
    )
    return result
