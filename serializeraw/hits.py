# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import functools

import configo
import utila
import yaml

import serializeraw.border


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
    return yaml.dump(raw)


@functools.lru_cache(configo.CACHE_SMALL)
def load_hits(content, pages=None):
    content = utila.from_raw_or_path(content, ftype='yaml')
    loaded = yaml.load(content, Loader=yaml.FullLoader)

    border = serializeraw.border.border_fromraw(loaded['border'])
    hits_raw = loaded['hits']

    hits = []
    for hit in hits_raw:
        splitted = hit.split(' ', maxsplit=2)
        page = int(splitted[0])
        if utila.should_skip(page, pages):
            continue
        index = int(splitted[1])
        box = serializeraw.border.border_fromraw(splitted[2])

        hits.append((page, index, box))
    return border, hits
