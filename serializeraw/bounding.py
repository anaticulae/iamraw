# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import functools

import configo
import utila
import yaml

import iamraw


def dump_boundingboxes(boxes: iamraw.PageBoundingsList) -> str:
    simple = []
    for page in boxes:
        assert isinstance(page, iamraw.PageBoundings), type(page)
        item = {
            'page':
                page.page,
            'content': [
                '%d %.2f %.2f %.2f %.2f' % (index, *tuple(box))
                for index, box in page.boundings
            ],
        }
        simple.append(item)
    dumped = yaml.dump(simple)
    return dumped


@functools.lru_cache(configo.CACHE_SMALL)
def load_boundingboxes(content: str, pages=None) -> iamraw.PageBoundingsList:
    content = utila.from_raw_or_path(
        content,
        fname='rawmaker__border_boundingboxes',
        ftype='yaml',
    )
    loaded = yaml.load(content, Loader=yaml.FullLoader)
    result = []
    for page in loaded:
        pagenumber = int(page['page'])
        if utila.should_skip(pagenumber, pages):
            continue
        boundings = []
        for item in page['content']:
            key, position = item.split(maxsplit=1)
            boundings.append((
                int(key),
                tuple(float(var) for var in position.split()),
            ))
        result.append(
            iamraw.PageBoundings(
                boundings=boundings,
                page=pagenumber,
            ))
    return result
