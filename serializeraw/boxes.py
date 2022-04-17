# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

from functools import lru_cache
from typing import Iterable

import utila
from configo import CACHE_SMALL

from iamraw import BoundingBox
from iamraw import Box
from iamraw import PageContentBoxes
from iamraw import PagesWithBoxList


def dump_boxes(pages: PagesWithBoxList) -> str:
    assert isinstance(pages, Iterable), type(pages)
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


@lru_cache(CACHE_SMALL)
def load_boxes(content: str, pages=None) -> PagesWithBoxList:
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
            Box(box=BoundingBox.from_list(
                [float(splitted)
                 for splitted in item.split()]),)
            for item in page['boxes']
        ]
        boxes = PageContentBoxes(content=box, page=pagenumber)
        result.append(boxes)
    return result
