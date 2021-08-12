# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

from functools import lru_cache
from typing import Iterable

import utila
from configo import CACHE_SMALL
from yaml import dump

from iamraw import BoundingBox
from iamraw import Box
from iamraw import HorizontalLine
from iamraw import PageContentBoxes
from iamraw import PageContentHorizontals
from iamraw import PagesWithBoxList
from iamraw import PagesWithHorizontalList


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
    dumped = dump(raw)
    return dumped


def dump_horizontals(pages: PagesWithHorizontalList) -> str:
    assert isinstance(pages, Iterable), type(pages)
    raw = []
    for page in pages:
        if not page.content:
            continue  # skip empty pages
        result = [str(horizontal.box) for horizontal in page.content]
        raw.append({
            'page': page.page,
            'horizontals': result,
        })
    dumped = dump(raw)
    return dumped


@lru_cache(CACHE_SMALL)
def load_boxes(content: str, pages=None) -> PagesWithBoxList:
    loaded = utila.yaml_from_raw_or_path(
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


@lru_cache(CACHE_SMALL)
def load_horizontals(
    content: str,
    pages=None,
    prefix='',
) -> PagesWithHorizontalList:
    if prefix:
        prefix = f'{prefix}_'
    loaded = utila.yaml_from_raw_or_path(
        content,
        fname=f'rawmaker__{prefix}horizontals_horizontals',
    )
    result = []
    for page in loaded:
        pagenumber = int(page['page'])
        if utila.should_skip(pagenumber, pages):
            continue
        horizontals = [
            HorizontalLine(box=BoundingBox(*utila.parse_tuple(item)))
            for item in page['horizontals']
        ]
        item = PageContentHorizontals(content=horizontals, page=pagenumber)
        result.append(item)
    return result
