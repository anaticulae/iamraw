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

from iamraw import Border
from iamraw import PageSize

# round results to 2 digits
NDIGITS = 2


def dump_boundingboxes(boxes):
    simple = [{
        'pages':
        page,
        'content': [{
            'item': index,
            'box': '%.2f %.2f %.2f %.2f' % tuple(box)
        } for index, box in pagebox],
    } for page, pagebox in enumerate(boxes)]
    dumped = dump(simple)
    return dumped


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


def dump_pageborders(size, border):
    assert len(size) == len(border)
    page = [
        {
            'number': index,
            'size': '%.2f %.2f' % size,  #(size.width, size.height),
            'border': '%.2f %.2f %.2f %.2f' % border,
        } for index, (size, border) in enumerate(zip(size, border))
    ]
    dumped = dump(page)
    return dumped


def load_pageborders(content: str):
    content = from_raw_or_path(content, ftype='yaml')
    loaded = load(content, Loader=FullLoader)
    size, border = [], []
    for item in loaded:
        size.append(PageSize(*[float(var) for var in item['size'].split()]))
        border.append(Border(*[float(var) for var in item['border'].split()]))
    return size, border
