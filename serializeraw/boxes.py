# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

from utila import from_raw_or_path
from yaml import FullLoader
from yaml import dump
from yaml import load

from iamraw import BoundingBox
from iamraw import Box
from iamraw import HorizontalLine


def dump_boxes(pages):
    raw = []
    for index, page in enumerate(pages):
        result = [box.box.raw() for box in page]
        raw.append({
            'page': index,
            'boxes': result,
        })
    dumped = dump(raw)
    return dumped


def dump_horizontal(pages):
    raw = []
    for index, page in enumerate(pages):
        result = [horizontal.box.raw() for horizontal in page]
        raw.append({
            'page': index,
            'horizontal': result,
        })
    dumped = dump(raw)
    return dumped


def load_boxes(content: str):
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
        pages.append(box)
    return pages


def load_horizontals(content: str):

    def create_box(item: str):
        converted = [float(splitted) for splitted in item.split()]
        return BoundingBox.from_list(converted)

    content = from_raw_or_path(content, ftype='yaml')
    loaded = load(content, Loader=FullLoader)
    pages = []
    for page in loaded:
        box = [
            HorizontalLine(box=create_box(item)) for item in page['horizontal']
        ]
        pages.append(box)
    return pages
