# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import contextlib
import functools

import configo
import utila

import iamraw


def dump_pagenumbers(items) -> str:
    if not isinstance(items, tuple):
        # single
        result = dump_raw(items)
    else:
        left, right = items
        result = dict(
            left=dump_raw(left),
            right=dump_raw(right),
        )
    dumped = utila.yaml_dump(result)
    return dumped


def dump_raw(content) -> list:
    # sort by page number
    content = sorted(
        content,
        key=lambda number: number[0],
    )
    result = [
        dict(
            pdfpage=pdfpage,
            bounding=str(bounding),
            detected=detectedpage,
        ) for pdfpage, bounding, detectedpage in content
    ]
    return result


@functools.lru_cache(configo.CACHE_SMALL)
def load_pagenumbers(content: str, pages=None):
    loaded = utila.yaml_load(
        content,
        fname='groupme__pagenumbers_pagenumbers',
    )
    with contextlib.suppress(TypeError):
        return fromraw(loaded, pages=pages)
    leftright = (
        fromraw(loaded['left'], pages=pages),
        fromraw(loaded['right'], pages=pages),
    )
    return leftright


def fromraw(content, pages):
    result = []
    for item in content:
        pdfpage = toint(item['pdfpage'])
        if utila.should_skip(pdfpage, pages):
            continue
        box = iamraw.BoundingBox.from_str(item['bounding'])
        detected = toint(item['detected'])
        result.append(
            iamraw.PageNumber(
                detected=detected,
                bounding=box,
                pdfpage=pdfpage,
            ))
    return result


def toint(item):
    with contextlib.suppress(ValueError):
        return int(item)
    return item
