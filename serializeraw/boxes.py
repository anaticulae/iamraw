# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import collections.abc

import configo
import utilo

import iamraw


def dump_boxes(pages: iamraw.PagesWithBoxList) -> str:
    assert isinstance(pages, collections.abc.Iterable), type(pages)
    raw = []
    for page in pages:
        if not page.content:
            continue  # skip empty pages
        result = [str(box.box) for box in page.content]
        raw.append({
            'page': page.page,
            'boxes': result,
        })
    dumped = utilo.yaml_dump(raw)
    return dumped


@configo.cache_small
def load_boxes(content: str, pages=None) -> iamraw.PagesWithBoxList:
    loaded = utilo.yaml_load(
        content,
        fname='rawmaker__boxes_boxes',
    )
    result = []
    for page in loaded:
        pagenumber = int(page['page'])
        if utilo.should_skip(pagenumber, pages):
            continue
        box = [
            iamraw.Box(iamraw.BoundingBox.from_list(utilo.parse_tuple(item)))
            for item in page['boxes']
        ]
        boxes = iamraw.PageContentBoxes(content=box, page=pagenumber)
        result.append(boxes)
    return result
