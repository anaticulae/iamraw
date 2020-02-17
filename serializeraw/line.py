# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================
import utila
import yaml

import iamraw


def dump_lines(lines: iamraw.PageContentLines) -> str:
    lines = sorted(lines, key=lambda x: x.page)
    result = []
    for page in lines:
        content = ['%.2f %.2f %.2f %.2f' % item for item in page.content]
        raw = {'page': page.page, 'content': content}
        result.append(raw)
    dumped = yaml.dump(result)
    return dumped


def load_lines(content: str, pages: tuple = None) -> iamraw.PageContentLines:
    content = utila.from_raw_or_path(content, ftype='yaml')
    loaded = yaml.load(content, Loader=yaml.FullLoader)
    result = []
    for page in loaded:
        pagenumber = int(page['page'])
        if utila.should_skip(pagenumber, pages):
            continue
        content = []
        for raw in page['content']:
            # TODO: REPLACE WITH UTILA CODE
            item = tuple(utila.roundme(float(var)) for var in raw.split())
            content.append(item)
        result.append(iamraw.PageContentLine(page=pagenumber, content=content))
    return result
