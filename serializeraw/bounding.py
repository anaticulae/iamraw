# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import configos
import utilo

import iamraw
import serializeraw


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
    dumped = utilo.yaml_dump(simple)
    dumped = serializeraw.dump_yamlpages(dumped)
    return dumped


@configos.cache_small
def load_boundingboxes(content: str, pages=None) -> iamraw.PageBoundingsList:
    content = serializeraw.load_yamlpages(
        content,
        pages=pages,
        fname='rawmaker__border_boundingboxes',
    )
    loaded = utilo.yaml_load(
        content,
        fname='rawmaker__border_boundingboxes',
        safe=False,
    )
    result = []
    for page in loaded:
        pagenumber = int(page['page'])
        if utilo.should_skip(pagenumber, pages):
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
