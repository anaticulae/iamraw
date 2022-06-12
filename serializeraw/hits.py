# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import configo
import utila

import iamraw
import serializeraw.border


def dump_hits(hits: iamraw.PageContentHits) -> str:
    result = []
    for page in hits:
        # content:  index, current
        hits = [
            '%d %.2f %.2f %.2f %.2f' % (index, *current)
            for index, current in page.hits
        ]
        raw = {
            'border': '%.2f %.2f %.2f %.2f' % page.border,
            'hits': hits,
            'page': page.page
        }
        result.append(raw)
    dumped = utila.yaml_dump(result)
    return dumped


@configo.cache_small
def load_hits(content: str, pages: tuple = None) -> iamraw.PageContentHits:
    loaded = utila.yaml_load(
        content,
        fname='border_detection',
        safe=False,
    )
    result = []
    for page in loaded:
        pagenumber = int(page['page'])
        if utila.should_skip(pagenumber, pages):
            continue

        border = serializeraw.border.border_fromraw(page['border'])
        hits = []
        for hit in page['hits']:
            index, box = hit.split(' ', maxsplit=1)
            index, box = int(index), utila.parse_tuple(box)
            hits.append((index, box))

        current = iamraw.PageContentHit(
            page=pagenumber,
            border=border,
            hits=hits,
        )
        result.append(current)
    return result
