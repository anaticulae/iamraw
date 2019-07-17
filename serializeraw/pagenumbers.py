# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

from contextlib import suppress
from functools import lru_cache

from configo import CACHE_SMALL
from utila import from_raw_or_path
from yaml import FullLoader
from yaml import dump
from yaml import load

from iamraw import BoundingBox


def dump_pagenumbers(items) -> str:

    def raw(content):
        items = [{
            'pdfpage': pdfpage,
            'bounding': str(bounding),
            'detected': detectedpage
        } for pdfpage, bounding, detectedpage in sorted(
            content, key=lambda number: number[0])]
        return items

    try:
        result = raw(items)
    except ValueError:
        left, right = items
        result = {
            'left': raw(left),
            'right': raw(right),
        }
    dumped = dump(result)
    return dumped


@lru_cache(CACHE_SMALL)
def load_pagenumbers(content: str):
    content = from_raw_or_path(content, ftype='yaml')
    loaded = load(content, Loader=FullLoader)

    def to_int(item):
        with suppress(ValueError):
            return int(item)
        return item

    def fromraw(content):
        result = [(
            to_int(item['pdfpage']),
            BoundingBox.from_str(item['bounding']),
            to_int(item['detected'],),
        ) for item in content]
        return result

    try:
        return fromraw(loaded)
    except TypeError:
        return fromraw(loaded['left']), fromraw(loaded['right'])
