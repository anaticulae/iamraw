# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utila

import iamraw


def dump_color_statistics(colors: iamraw.PageContents) -> str:
    result = []
    for page in colors:
        content = [
            f'{utila.rgb2int(*item[0])} {item[1]}' for item in page.content
        ]
        raw = dict(
            content=content,
            page=page.page,
        )
        result.append(raw)
    dumped = utila.yaml_dump(result)
    return dumped


def load_color_statistics(
    content: str,
    pages: tuple = None,
) -> iamraw.PageContents:
    loaded = utila.yaml_load(
        content,
        fname='colors__statistics_statistics',
    )
    result = []
    for page in loaded:
        pagenumber = int(page['page'])
        if utila.should_skip(pagenumber, pages):
            continue
        data = [
            utila.parse_tuple(item, length=2, typ=int)
            for item in page['content']
        ]
        data = [(utila.int2rgb(item[0]), item[1]) for item in data]
        result.append(iamraw.PageContent(
            page=pagenumber,
            content=data,
        ))
    return result
