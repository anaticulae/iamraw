# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2020 by Helmut Konrad Fahrendholz. All rights reserved.
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

from iamraw import BoundingBox
from iamraw import PageContentTextPosition
from iamraw import PageContentTextPositions


def dump_textpositions(items: PageContentTextPositions) -> str:
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
    dumped = dump(result)
    return dumped


@lru_cache(CACHE_SMALL)
def load_textpositions(content: str, pages=None) -> PageContentTextPositions:
    content = from_raw_or_path(
        content,
        fname='rawmaker__text_positions',
        ftype='yaml',
    )
    loaded = load(content, Loader=FullLoader)

    result = []
    for page in loaded:
        pagenumber = int(page['page'])
        if should_skip(pagenumber, pages):
            continue
        pagedata = {}
        for item in page['content']:
            key, data = item.split(maxsplit=1)
            bounding, mean = data.rsplit(maxsplit=1)
            mean = float(mean)
            pagedata[int(key)] = (BoundingBox.from_str(bounding), mean)

        if not content:
            continue

        textposition = PageContentTextPosition(
            content=pagedata,
            page=pagenumber,
        )
        result.append(textposition)
    return result
