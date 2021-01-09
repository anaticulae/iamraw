# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import functools

import configo
import utila
import yaml

import iamraw


def dump_lists(lists: list) -> str:
    raw = []
    for (pagenumber, pagecontent) in lists:
        pagenumber = int(pagenumber)
        pageresult = []
        for lists_ in pagecontent:
            area = dump_area(lists_.area)
            content = []
            for pnumber, item in lists_.data:
                assert item, f'page: {pagenumber}; {pnumber} empty list content'
                content.append(f'{pnumber} {item}')
            pageresult.append({
                'area': area,
                'content': content,
                'id': f'{lists_.paragraph} {lists_.merged}',
            })
        if pageresult:
            raw.append({
                'page': pagenumber,
                'lists': pageresult,
            })
    dumped = yaml.safe_dump(raw)
    return dumped


@functools.lru_cache(configo.CACHE_SMALL)
def load_lists(content: str, pages=None) -> iamraw.PageContentLists:
    content = utila.from_raw_or_path(
        content,
        fname='words__list_list',
        ftype='yaml',
    )
    loaded = yaml.safe_load(content)
    result = []
    for page in loaded:
        pagenumber = int(page['page'])
        if utila.should_skip(pagenumber, pages):
            continue
        content = page['lists']
        newpage = []
        for listinstance in content:
            paragraph, merged = [
                int(item) for item in listinstance['id'].split()
            ]
            area = load_area(listinstance['area'])
            instance = iamraw.PageList(
                area=area,
                paragraph=paragraph,
                merged=merged,
            )
            for entree in listinstance['content']:
                # See (Number, Item)
                try:
                    number, text = entree.split(maxsplit=1)
                except ValueError:
                    utila.error('could not load list properly '
                                f'on page {pagenumber}: {entree}')
                    number, text = '', entree
                # try to convert to int/float
                if number.isdigit():  # all decimal digits and not empty
                    number = int(number)
                instance.append(text, number)
            newpage.append(instance)
        result.append(iamraw.PageContentList(page=pagenumber, content=newpage))
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
