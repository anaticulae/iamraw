# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import functools

import configo
import utila

import iamraw


def dump_lists(lists: list) -> str:
    raw = []
    for (pagenumber, pagecontent) in lists:
        pagenumber = int(pagenumber)
        pageresult = [
            list_raw(instance, pagenumber=pagenumber)
            for instance in pagecontent
        ]
        if not pageresult:
            continue
        raw.append(dict(
            page=pagenumber,
            lists=pageresult,
        ))
    dumped = utila.yaml_dump(raw)
    return dumped


def list_raw(instance, pagenumber) -> dict:
    area = dump_area(instance.area)
    content = []
    for pnumber, item in instance.data:
        if not item:
            utila.error(instance)
            utila.error(f'page:{pagenumber};{pnumber} empty list item')
        content.append(f'{pnumber} {item}')
    result = dict(
        area=area,
        content=content,
        id=f'{instance.paragraph} {instance.merged}',
    )
    if instance.area_length:
        result['area_length'] = dump_area(instance.area_length)
    if instance.__strategy__:
        result['__strategy__'] = instance.__strategy__
    return result


@functools.lru_cache(configo.CACHE_SMALL)
def load_lists(content: str, pages=None) -> iamraw.PageContentLists:
    loaded = utila.yaml_load(
        content,
        fname='words__list_list',
    )
    result = []
    for page in loaded:
        pagenumber = int(page['page'])
        if utila.should_skip(pagenumber, pages):
            continue
        lists = []
        for listinstance in page['lists']:
            instance = load_list_instance(listinstance)
            instance.pdfpage = pagenumber
            lists.append(instance)
        result.append(iamraw.PageContentList(page=pagenumber, content=lists))
    return result


def load_list_instance(raw: dict) -> iamraw.PageList:
    area = load_area(raw['area'])
    area_length = load_area(raw.get('area_length', ''))
    paragraph, merged = utila.parse_tuple(
        raw['id'],
        length=2,
        typ=int,
    )
    result = iamraw.PageList(
        area=area,
        area_length=area_length,
        paragraph=paragraph,
        merged=merged,
    )
    for entree in raw['content']:
        # See (Number, Item)
        try:
            number, text = entree.split(maxsplit=1)
        except ValueError:
            utila.error('could not load list properly '
                        f'on raw {raw}: {entree}')
            number, text = '', entree
        # try to convert to int/float
        if number.isdigit():  # all decimal digits and not empty
            number = int(number)
        result.append(text, number)
    return result


def dump_area(area) -> str:
    """\
    >>> dump_area([(17, 18, 19), (0, 1, 2, 3), (0, 1, 2, 3)])
    '17 18 19|0 1 2 3|0 1 2 3'
    >>> dump_area([0, 1, 2, 3])
    '0 1 2 3'
    """
    area = area if isinstance(area[0], tuple) else [area]
    splitted = [utila.from_tuple(item) for item in area]
    raw = '|'.join(splitted)
    return raw


def load_area(raw: str) -> list:
    """\
    >>> load_area('17 18 19|0 1 2 3|0 1 2 3')
    [(17, 18, 19), (0, 1, 2, 3), (0, 1, 2, 3)]
    >>> load_area('0 1 2 3')
    [0, 1, 2, 3]
    """
    splitted = raw.split('|')
    if len(splitted) == 1:
        return [int(item) for item in splitted[0].split()]
    return [tuple(load_area(item)) for item in splitted]
