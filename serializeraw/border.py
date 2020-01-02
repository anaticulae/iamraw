# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

from functools import lru_cache

from configo import CACHE_SMALL
from utila import debug
from utila import from_raw_or_path
from utila import should_skip
from yaml import FullLoader
from yaml import dump
from yaml import load

from iamraw import Border
from iamraw import PageSize
from iamraw import PageSizeBorder
from iamraw import PageSizeBorderList


# def dump_pageborders(size: List[PageSize], border: List[Border]) -> str:
def dump_pageborders(sizeandborders: PageSizeBorderList) -> str:
    page = [{
        'page': item.page,
        'size': size_toraw(item.size),
        'border': border_toraw(item.border),
    } for item in sizeandborders]
    dumped = dump(page)
    return dumped


@lru_cache(CACHE_SMALL)
def load_pageborders(content: str, pages=None) -> PageSizeBorderList:
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
    result = []
    for item in loaded:
        pagenumber = int(item['page'])
        if should_skip(pagenumber, pages):
            continue
        size = size_fromraw(item['size'])
        border = border_fromraw(item['border'])
        result.append(PageSizeBorder(size=size, border=border, page=pagenumber))
    return result


def size_toraw(size: PageSize) -> str:
    assert isinstance(size, PageSize)
    try:
        return '%.2f %.2f' % size  #(size.width, size.height)
    except TypeError as error:
        debug('%s %r' % (error, size))
        return 'None'


def size_fromraw(size: str) -> PageSize:
    assert isinstance(size, str)
    try:
        return PageSize(*[float(var) for var in size.split()])
    except ValueError as error:
        debug('%s %r' % (error, size))
        return PageSize(None, None)


def border_toraw(border: Border) -> str:
    assert isinstance(border, Border)
    try:
        return '%.2f %.2f %.2f %.2f' % border
    except TypeError as error:
        debug('%s %r' % (error, border))
        return 'None'


def border_fromraw(border: str) -> Border:
    assert isinstance(border, str)
    try:
        return Border(*[float(var) for var in border.split()])
    except ValueError as error:
        debug('%s %r' % (error, border))
        return Border(None, None, None, None)
