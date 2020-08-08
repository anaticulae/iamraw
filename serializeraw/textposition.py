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

import iamraw


def dump_textpositions(items: iamraw.PageContentTextPositions) -> str:
    result = []
    for page in items:
        pagenumber = page.page
        content = page.content
        if not content:
            continue
        raw = [
            '%s %s %s' % (key, str(bounding), str(mean))
            for key, (bounding, mean) in content.items()
        ]
        result.append({
            'content': raw,
            'page': pagenumber,
        })
    dumped = yaml.dump(result)
    return dumped


@functools.lru_cache(configo.CACHE_SMALL)
def load_textpositions(
        content: str,
        pages=None,
) -> iamraw.PageContentTextPositions:
    content = utila.from_raw_or_path(
        content,
        fname='rawmaker__text_positions',
        ftype='yaml',
    )
    loaded = yaml.load(content, Loader=yaml.FullLoader)
    result = []
    for page in loaded:
        pagenumber = int(page['page'])
        if utila.should_skip(pagenumber, pages):
            continue
        pagedata = {}
        for item in page['content']:
            key, data = item.split(maxsplit=1)
            bounding, mean = data.rsplit(maxsplit=1)
            mean = float(mean)
            pagedata[int(key)] = (iamraw.BoundingBox.from_str(bounding), mean)
        if not content:
            continue
        textposition = iamraw.PageContentTextPosition(
            content=pagedata,
            page=pagenumber,
        )
        result.append(textposition)
    return result
