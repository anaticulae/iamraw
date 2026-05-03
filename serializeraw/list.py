# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import configos
import utilo

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
        raw.append({
            'page': pagenumber,
            'lists': pageresult,
        })
    dumped = utilo.yaml_dump(raw)
    return dumped


def list_raw(instance, pagenumber) -> dict:
    area = dump_area(instance.area)
    content = []
    for pnumber, item in instance.data:
        if not item:
            utilo.error(instance)
            utilo.error(f'page:{pagenumber};{pnumber} empty list item')
        content.append(f'{pnumber} {item}')
    result = {
        'area': area,
        'content': content,
    }
    if instance.area_length:
        result['area_length'] = dump_area(instance.area_length)
    if instance.__strategy__:
        result['__strategy__'] = instance.__strategy__
    return result


@configos.cache_small
def load_lists(content: str, pages=None) -> iamraw.PageContentLists:
    loaded = utilo.yaml_load(
        content,
        fname=(
            'lists__result_result',
            'words__list_list',
        ),
    )
    result = []
    for page in loaded:
        pagenumber = int(page['page'])
        if utilo.should_skip(pagenumber, pages):
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
    result = iamraw.PageList(
        area=area,
        area_length=area_length,
    )
    for entree in raw['content']:
        # See (Number, Item)
        try:
            number, text = entree.split(maxsplit=1)
        except ValueError:
            utilo.error('could not load list properly '
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
    splitted = [utilo.from_tuple(item) for item in area]
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
