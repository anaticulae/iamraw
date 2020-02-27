# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import functools

import configo
import utila
import yaml

import iamraw


@functools.lru_cache(configo.CACHE_SMALL)
def load_highnotes(content: str, pages: tuple = None):
    content = utila.from_raw_or_path(content, ftype='yaml')
    loaded = yaml.load(content, Loader=yaml.FullLoader)
    result = []
    for pagecontent in loaded:
        pagenumber = int(pagecontent['page'])
        if utila.should_skip(pagenumber, pages):
            continue
        page = iamraw.PageContentTextItems(page=pagenumber)
        page.content = [
            iamraw.HighNote(
                start=item['start'],
                end=item['end'],
                value=item['value'],
            ) for item in pagecontent['content']
        ]
        result.append(page)
    return result


def dump_highnotes(pages) -> str:
    assert_list(pages, iamraw.PageContentTextItems)
    result = []
    for page in pages:
        raw = {'page': page.page}
        items = [{
            'start': item.start,
            'end': item.end,
            'value': item.value
        } for item in page.content]
        raw['content'] = items
        result.append(raw)
    dumped = yaml.dump(result)
    return dumped


def assert_list(items, types):
    assert isinstance(items, list), type(items)
    verified = [isinstance(item, types) for item in items]
    assert verified, str(verified)
