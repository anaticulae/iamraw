# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import collections.abc

import configo
import utila

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
    dumped = utila.yaml_dump(raw)
    return dumped


@configo.cache_small
def load_boxes(content: str, pages=None) -> iamraw.PagesWithBoxList:
    loaded = utila.yaml_load(
        content,
        fname='rawmaker__boxes_boxes',
    )
    result = []
    for page in loaded:
        pagenumber = int(page['page'])
        if utila.should_skip(pagenumber, pages):
            continue
        box = [
            iamraw.Box(iamraw.BoundingBox.from_list(utila.parse_tuple(item)))
            for item in page['boxes']
        ]
        boxes = iamraw.PageContentBoxes(content=box, page=pagenumber)
        result.append(boxes)
    return result
