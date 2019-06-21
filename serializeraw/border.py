# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

from typing import List
from typing import Tuple

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


def dump_pageborders(size: List[PageSize], border: List[Border]) -> str:
    assert len(size) == len(border)
    page = [{
        'number': index,
        'size': size_toraw(size),
        'border': border_toraw(border),
    } for index, (size, border) in enumerate(zip(size, border))]
    dumped = dump(page)
    return dumped


def load_pageborders(content: str) -> Tuple[List[PageSize], List[Border]]:
    """Load pdf page size and content border from raw data

    This method loads 2 lists with items for every single page. The first list
    contains the size of the pdf page in "pixel?". The second list contains
    the border of the content of the page. This border is maximized in every
    4 page directions. The diff between pagesize - pageborder is the whitespace
    where is nothing printed.

    TODO: Clearify pixel or mm?

    Args:
        content(str): path or raw content to load
    Returns:
        List[PageSize], List[Border]
    """
    content = from_raw_or_path(content, ftype='yaml')
    loaded = load(content, Loader=FullLoader)
    size, border = [], []
    for item in loaded:
        size.append(size_fromraw(item['size']))
        border.append(border_fromraw(item['border']))
    return size, border


def size_toraw(size: PageSize) -> str:
    assert isinstance(size, PageSize)
    try:
        return '%.2f %.2f' % size  #(size.width, size.height)
    except TypeError:
        # PageSize(None,None)
        return 'None'


def size_fromraw(size: str) -> PageSize:
    assert isinstance(size, str)
    try:
        return PageSize(*[float(var) for var in size.split()])
    except ValueError:
        return PageSize(None, None)


def border_toraw(border: Border) -> str:
    assert isinstance(border, Border)
    try:
        return '%.2f %.2f %.2f %.2f' % border
    except TypeError:
        return 'None'


def border_fromraw(border: str) -> Border:
    assert isinstance(border, str)
    try:
        return Border(*[float(var) for var in border.split()])
    except ValueError:
        return Border(None, None, None, None)
