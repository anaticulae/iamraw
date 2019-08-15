# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

from functools import lru_cache

from configo import CACHE_SMALL
from utila import from_raw_or_path
from utila import should_skip
from yaml import FullLoader
from yaml import dump
from yaml import load

from serializeraw.border import border_fromraw


def dump_hits(border, content):
    # content: page, index, current
    result = [
        '%d %d %.2f %.2f %.2f %.2f' % (page, index, *current)
        for page, index, current in content
    ]
    raw = {
        'border': '%.2f %.2f %.2f %.2f' % border,
        'hits': result,
    }
    return dump(raw)


@lru_cache(CACHE_SMALL)
def load_hits(content, pages=None):
    content = from_raw_or_path(content, ftype='yaml')
    loaded = load(content, Loader=FullLoader)

    border = border_fromraw(loaded['border'])
    hits_raw = loaded['hits']

    hits = []
    for hit in hits_raw:
        splitted = hit.split(' ', maxsplit=2)
        page = int(splitted[0])
        if should_skip(page, pages):
            continue
        index = int(splitted[1])
        box = border_fromraw(splitted[2])

        hits.append((page, index, box))
    return border, hits
