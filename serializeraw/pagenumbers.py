# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import contextlib

import configo
import utilo

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
    dumped = utilo.yaml_dump(result)
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
            bounding=utilo.from_tuple(bounding),
            detected=detectedpage,
        ) for pdfpage, bounding, detectedpage in content
    ]
    return result


@configo.cache_small
def load_pagenumbers(content: str, pages=None):
    loaded = utilo.yaml_load(
        content,
        fname=(
            'pagenumber__result_result',
            'groupme__pagenumbers_pagenumbers',
        ),
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
        if utilo.should_skip(pdfpage, pages):
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


def load_pagenumbers_magic(content: str, pages: tuple = None) -> dict:
    """Load extend page numbers with filled user pages.

    >>> import utilo
    >>> data = utilo.yaml_dump({3:'I', 4:'1', 5:'2', 6:'3'})
    >>> load_pagenumbers_magic(data)
    {3: 'I', 4: '1', 5: '2', 6: '3'}
    """
    loaded = utilo.yaml_load(
        content,
        fname='groupme__pagenumbers_magic',
    )
    result = {
        pdfpage: userpage
        for pdfpage, userpage in loaded.items()
        if not utilo.should_skip(page=pdfpage, pages=pages)
    }
    return result
