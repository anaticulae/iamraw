# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import contextlib
import functools

import configo
import utila
import yaml

import iamraw


def dump_pagenumbers(items) -> str:

    def raw(content):
        items = [{
            'pdfpage': pdfpage,
            'bounding': str(bounding),
            'detected': detectedpage
        } for pdfpage, bounding, detectedpage in sorted(
            content, key=lambda number: number[0])]
        return items

    if not isinstance(items, tuple):
        # single
        result = raw(items)
    else:
        left, right = items
        result = {
            'left': raw(left),
            'right': raw(right),
        }
    dumped = yaml.dump(result)
    return dumped


@functools.lru_cache(configo.CACHE_SMALL)
def load_pagenumbers(content: str, pages=None):
    content = utila.from_raw_or_path(
        content,
        fname='groupme__pagenumbers_pagenumbers',
        ftype='yaml',
    )
    loaded = yaml.load(content, Loader=yaml.FullLoader)

    def to_int(item):
        with contextlib.suppress(ValueError):
            return int(item)
        return item

    def fromraw(content, pages):
        result = []
        for item in content:
            pagenumber = to_int(item['pdfpage'])
            if utila.should_skip(pagenumber, pages):
                continue
            box = iamraw.BoundingBox.from_str(item['bounding'])
            detected = to_int(item['detected'])
            result.append((pagenumber, box, detected))
        return result

    with contextlib.suppress(TypeError):
        return fromraw(loaded, pages)
    return fromraw(loaded['left'], pages), fromraw(loaded['right'], pages)
