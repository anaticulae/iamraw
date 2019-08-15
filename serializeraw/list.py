# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

from functools import lru_cache
from typing import List

from configo import CACHE_SMALL
from utila import from_raw_or_path
from utila import should_skip
from yaml import FullLoader
from yaml import dump
from yaml import load

from iamraw import PageList


def dump_lists(lists: List[str]) -> str:
    raw = []
    for (number, page) in lists:
        pageresult = []
        for (paragraph, merged, content) in page:
            # Number, Item
            area = ' '.join([str(item) for item in content.area])
            content = ['%s %s' % (number, item) for (number, item) in content]
            pageresult.append({
                'area': area,
                'content': content,
                'id': '%d %d' % (paragraph, merged),
            })
        if pageresult:
            raw.append({
                'page': number,
                'lists': pageresult,
            })
    dumped = dump(raw)
    return dumped


@lru_cache(CACHE_SMALL)
def load_lists(content: str, pages=None) -> List[str]:
    content = from_raw_or_path(content, ftype='yaml')
    loaded = load(content, Loader=FullLoader)
    result = []
    for page in loaded:
        pagenumber = int(page['page'])
        if should_skip(pagenumber, pages):
            continue
        content = page['lists']
        newpage = []
        for listinstance in content:
            paragraph, merged = [
                int(item) for item in listinstance['id'].split()
            ]
            area = [int(item) for item in listinstance['area'].split()]
            instance = PageList(area=area)
            for entree in listinstance['content']:
                # See (Number, Item)
                number, text = entree.split(maxsplit=1)
                # # try to convert to int/float
                if number.isdigit():  # all decimal digits and not empty
                    number = int(number)
                instance.append(text, number)
            newpage.append((paragraph, merged, instance))
        result.append((pagenumber, newpage))
    return result
