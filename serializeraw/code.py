# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utilo

import iamraw


def dump_codes(items: iamraw.PageContentCodes) -> str:
    # remove empty pages
    items = [item for item in items if item.content]
    raw = [dump_page(item) for item in items]
    # convert to yaml
    dumped = utilo.yaml_dump(raw)
    return dumped


def dump_page(page: iamraw.PageContentCode) -> dict:
    content = [
        dict(
            caption=utilo.from_tuple(code.caption) if code.caption else tuple(),
            caption_bounding=[
                utilo.from_tuple(item) for item in code.caption_bounding
            ],
            tokens=utilo.from_tuple(code.tokens) if code.tokens else tuple(),
            tokens_bounding=[
                utilo.from_tuple(item) for item in code.tokens_bounding
            ],
        ) for code in page.content
    ]
    result = dict(content=content, page=page.page)
    return result


def load_page(page) -> iamraw.PageContentCode:
    pagenr = int(page['page'])
    content = [
        iamraw.PeaceOfCode(
            caption=utilo.parse_tuple(
                code['caption'],
                length=None,
                typ=int,
            ) if code['caption'] else tuple(),
            caption_bounding=[
                utilo.parse_tuple(item) for item in code['caption_bounding']
            ],
            tokens=utilo.parse_tuple(
                code['tokens'],
                length=None,
                typ=int,
            ) if code['tokens'] else tuple(),
            tokens_bounding=[
                utilo.parse_tuple(item) for item in code['tokens_bounding']
            ],
            page=pagenr,
        ) for code in page['content']
    ]
    return iamraw.PageContentCode(content=content, page=pagenr)


def load_codes(
    content: str,
    pages: tuple = None,
) -> iamraw.PageContentCodes:
    loaded = utilo.yaml_load(
        content,
        fname='codero__result_result',
        safe=False,
    )
    result = []
    for page in loaded:
        if utilo.should_skip(page['page'], pages):
            continue
        content = load_page(page)
        result.append(content)
    return result
