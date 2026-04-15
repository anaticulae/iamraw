# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import configos
import utilo

import texmex


@configos.cache_small
def load_highnotes(content: str, pages: tuple = None):
    loaded = utilo.yaml_load(
        content,
        safe=False,
    )
    result = []
    for pagecontent in loaded:
        pagenumber = int(pagecontent['page'])
        if utilo.should_skip(pagenumber, pages):
            continue
        page = texmex.PageContentTextItems(page=pagenumber)
        page.content = [
            texmex.HighNote(
                start=item['start'],
                end=item['end'],
                value=item['value'],
            ) for item in pagecontent['content']
        ]
        result.append(page)
    return result


def dump_highnotes(pages) -> str:
    utilo.asserts_types(pages, texmex.PageContentTextItems)
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
    dumped = utilo.yaml_dump(result)
    return dumped
