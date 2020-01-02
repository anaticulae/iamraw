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

from iamraw import PageBoundings
from iamraw import PageBoundingsList


def dump_boundingboxes(boxes: PageBoundingsList) -> str:
    simple = []
    for page in boxes:
        assert isinstance(page, PageBoundings), type(page)
        item = {
            'page':
            page.page,
            'content': [{
                'item': index,
                'box': '%.2f %.2f %.2f %.2f' % tuple(box)
            } for index, box in page.boundings],
        }
        simple.append(item)
    dumped = dump(simple)
    return dumped


@lru_cache(CACHE_SMALL)
def load_boundingboxes(content: str, pages=None) -> PageBoundingsList:
    content = from_raw_or_path(content, ftype='yaml')
    loaded = load(content, Loader=FullLoader)
    result = []
    for page in loaded:
        pagenumber = int(page['page'])
        if should_skip(pagenumber, pages):
            continue
        boundings = [[
            item['item'],
            [float(var) for var in item['box'].split()],
        ] for item in page['content']]
        result.append(PageBoundings(boundings=boundings, page=pagenumber))
    return result
