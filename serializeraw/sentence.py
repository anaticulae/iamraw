# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2022-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utilo

import iamraw
import serializeraw


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


def dump_sentence_bounding(sentences: iamraw.PageContents) -> str:
    result = serializeraw.dump_pagecontent(
        pages=sentences,
        pagedumper=dumper,
    )
    return result


MULTILINE_SEPARATOR = '  '


def dumper(boundings) -> list:
    result = []
    for bounding in boundings:
        single = not bounding or isinstance(bounding[0], (int, float))
        if single:
            if not bounding:
                utilo.debug(f'dump empty bounding: {boundings}')
            item = utilo.from_tuple(bounding)
        else:
            item = utilo.from_tuple(
                [utilo.from_tuple(it) for it in bounding],
                separator=MULTILINE_SEPARATOR,
            )
        result.append(item)
    return result


def loader(boundings) -> list:
    result = []
    for bounding in boundings:
        if not bounding:
            # empty element
            utilo.debug(f'load empty boundung: {boundings}')
            result.append(tuple())
            continue
        single = MULTILINE_SEPARATOR not in bounding
        if single:
            item = utilo.parse_tuple(bounding)
        else:
            splitted = utilo.parse_tuple(
                bounding,
                length=None,
                typ=str,
                separator=MULTILINE_SEPARATOR,
            )
            item = tuple(utilo.parse_tuple(it) for it in splitted)
        result.append(item)
    return result
