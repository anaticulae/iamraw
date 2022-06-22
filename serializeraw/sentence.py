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


def dump_sentence_bounding(sentences: iamraw.PageContents) -> str:
    dumper = lambda x: [utila.from_tuple(item) for item in x]
    result = serializeraw.dump_pagecontent(
        pages=sentences,
        pagedumper=dumper,
    )
    return result


def load_sentence_bounding(
    source: str,
    pages: tuple = None,
) -> iamraw.PageContents:
    loader = lambda x: [utila.parse_tuple(item) for item in x]
    result = serializeraw.load_pagecontent(
        content=source,
        pages=pages,
        pageloader=loader,
        fname='words__sentences_bounding',
    )
    return result
