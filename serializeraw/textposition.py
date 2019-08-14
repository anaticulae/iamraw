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
from yaml import FullLoader
from yaml import dump
from yaml import load

from iamraw import BoundingBox
from iamraw import PageContentTextPosition
from iamraw import PageContentTextPositions


@lru_cache(CACHE_SMALL)
def load_textpositions(content: str) -> PageContentTextPositions:
    content = from_raw_or_path(content, ftype='yaml')
    loaded = load(content, Loader=FullLoader)

    result = []
    for page in loaded:
        pagenumber = int(page['page'])
        pagedata = {}
        for item in page['content']:
            key, position = item.split(maxsplit=1)
            pagedata[int(key)] = BoundingBox.from_str(position)

        textposition = PageContentTextPosition(
            content=pagedata,
            page=pagenumber,
        )
        result.append(textposition)
    return result


def dump_textpositions(items: PageContentTextPositions) -> str:
    result = []
    for page in items:
        pagenumber = page.page
        content = page.content
        raw = ['%s %s' % (key, str(value)) for key, value in content.items()]
        result.append({
            'content': raw,
            'page': pagenumber,
        })
    dumped = dump(result)
    return dumped
