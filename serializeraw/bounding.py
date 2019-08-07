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


def dump_boundingboxes(boxes):
    simple = [{
        'page':
        page,
        'content': [{
            'item': index,
            'box': '%.2f %.2f %.2f %.2f' % tuple(box)
        } for index, box in pagebox],
    } for page, pagebox in enumerate(boxes)]
    dumped = dump(simple)
    return dumped


@lru_cache(CACHE_SMALL)
def load_boundingboxes(content):
    content = from_raw_or_path(content, ftype='yaml')
    loaded = load(content, Loader=FullLoader)
    pages = []
    for page in loaded:
        borders = [[
            item['item'],
            [float(var) for var in item['box'].split()],
        ] for item in page['content']]
        pages.append(borders)
    return pages
