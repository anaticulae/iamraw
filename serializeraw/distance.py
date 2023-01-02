# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utila

import iamraw


def dump_distance(items: iamraw.PageContentAreaDistances) -> str:
    raw = []
    for page in items:
        content = []
        for item in page.content:
            before = utila.roundme(item.before) if item.before is not None else 'None' # yapf:disable
            after = utila.roundme(item.after) if item.after is not None else 'None' # yapf:disable
            content.append(f'{item.index} {before} {after}')
        raw.append({'page': page.page, 'content': content})
    dumped = utila.yaml_dump(raw)
    return dumped


def load_distance(
    content: str,
    pages: tuple = None,
) -> iamraw.PageContentAreaDistances:
    loaded = utila.yaml_load(content)
    result = []
    for page in loaded:
        pagenumber = int(page['page'])
        if utila.should_skip(pagenumber, pages):
            continue
        pagecontent = []
        for line in page['content']:
            index, before, after = line.split()
            try:
                before = float(before)
            except ValueError:
                before = None
            try:
                after = float(after)
            except ValueError:
                after = None
            index = int(index)
            pagecontent.append(
                iamraw.AreaDistance(
                    index=index,
                    before=before,
                    after=after,
                ))
        result.append(
            iamraw.PageContentAreaDistance(
                page=pagenumber,
                content=pagecontent,
            ))
    return result
