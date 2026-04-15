# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import configo
import utilo

import iamraw


# def dump_pageborders(size: List[PageSize], border: List[Border]) -> str:
def dump_pageborders(sizeandborders: iamraw.PageSizeBorderList) -> str:
    page = [{
        'page': item.page,
        'size': size_toraw(item.size),
        'border': border_toraw(item.border),
    } for item in sizeandborders]
    dumped = utilo.yaml_dump(page)
    return dumped


@configo.cache_small
def load_pageborders(
    content: str,
    pages: tuple = None,
) -> iamraw.PageSizeBorderList:
    """Load pdf page size and content border from raw data

    This method loads 2 lists with items for every single page. The first list
    contains the size of the pdf page in "pixel?". The second list contains
    the border of the content of the page. This border is maximized in every
    4 page directions. The diff between pagesize - pageborder is the whitespace
    where is nothing printed.

    TODO: Clearify pixel or mm?

    Args:
        content(str): path or raw content to load
        pages(tuple): select pages to load
    Returns:
        List[PageSize], List[Border]
    """
    loaded = utilo.yaml_load(
        content,
        fname='rawmaker__border_pages',
    )
    result = []
    for item in loaded:
        pagenumber = int(item['page'])
        if utilo.should_skip(pagenumber, pages):
            continue
        size = size_fromraw(item['size'])
        border = border_fromraw(item['border'])
        result.append(
            iamraw.PageSizeBorder(
                size=size,
                border=border,
                page=pagenumber,
            ))
    return result


def size_toraw(size: iamraw.PageSize) -> str:
    try:
        return '%.2f %.2f' % size  #(size.width, size.height)
    except TypeError as error:
        utilo.debug('%s %r' % (error, size))
    return 'None'


def size_fromraw(size: str) -> iamraw.PageSize:
    assert isinstance(size, str)
    try:
        return iamraw.PageSize(*[float(var) for var in size.split()])
    except ValueError as error:
        utilo.debug('%s %r' % (error, size))
    return iamraw.PageSize(None, None)


def border_toraw(border: iamraw.Border) -> str:
    assert isinstance(border, iamraw.Border)
    try:
        return '%.2f %.2f %.2f %.2f' % border
    except TypeError as error:
        utilo.debug('%s %r' % (error, border))
    return 'None'


def border_fromraw(border: str) -> iamraw.Border:
    assert isinstance(border, str)
    try:
        return iamraw.Border(*[float(var) for var in border.split()])
    except ValueError as error:
        utilo.debug('%s %r' % (error, border))
    return iamraw.Border(None, None, None, None)


def load_leftright_border(content: str, pages: tuple = None) -> dict:
    loaded = utilo.yaml_load(
        content,
        fname='groupme__border_leftright',
    )
    lookup = {}
    for line in loaded:
        page, border = line.split(maxsplit=1)
        page = int(page)
        if utilo.should_skip(page, pages):
            continue
        border = utilo.parse_tuple(border, length=4)
        lookup[page] = border
    return lookup


def dump_leftright_border(result: list) -> str:
    """Convert a list of page borders(items) to yaml.

    item = (pagenumber, left, right, top, bottom)
    """
    result = [utilo.from_tuple(item) for item in result]
    dumped = utilo.yaml_dump(result)
    return dumped
