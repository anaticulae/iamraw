# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

from functools import lru_cache
from typing import Iterable

from configo import CACHE_SMALL
from utila import from_raw_or_path
from yaml import FullLoader
from yaml import dump
from yaml import load

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
def load_boxes(content: str) -> PagesWithBoxList:
    content = from_raw_or_path(content, ftype='yaml')
    loaded = load(content, Loader=FullLoader)

    pages = []
    for page in loaded:
        box = [
            Box(box=BoundingBox.from_list(
                [float(splitted)
                 for splitted in item.split()]),)
            for item in page['boxes']
        ]
        pagenumber = int(page['page'])
        boxes = PageContentBoxes(content=box, page=pagenumber)
        pages.append(boxes)
    return pages


@lru_cache(CACHE_SMALL)
def load_horizontals(content: str) -> PagesWithHorizontalList:

    def create_box(item: str):
        converted = [float(splitted) for splitted in item.split()]
        return BoundingBox.from_list(converted)

    content = from_raw_or_path(content, ftype='yaml')
    loaded = load(content, Loader=FullLoader)
    pages = []
    for page in loaded:
        horizontals = [
            HorizontalLine(box=create_box(item)) for item in page['horizontals']
        ]
        pagenumber = int(page['page'])
        item = PageContentHorizontals(content=horizontals, page=pagenumber)
        pages.append(item)
    return pages
