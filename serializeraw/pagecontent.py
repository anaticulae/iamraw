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


def dump_pagecontent(
    pages: iamraw.PageContents,
    pagedumper: callable = None,
) -> str:
    pagedumper = pagedumper if pagedumper else lambda x: x
    converted = [(page.page, pagedumper(page.content)) for page in pages]
    dumped = utilo.yaml_dump(converted)
    return dumped


def load_pagecontent(
    content: str,
    pages: tuple = None,
    pageloader: callable = None,
    fname: str = None,
) -> iamraw.PageContents:
    content = utilo.from_raw_or_path(content, ftype='yaml', fname=fname)
    loaded = utilo.yaml_load(content)
    pageloader = pageloader if pageloader else lambda x: x
    result = []
    for page, pagecontent in loaded:
        if utilo.should_skip(page, pages):
            continue
        pagecontent = pageloader(pagecontent)
        result.append(iamraw.PageContent(
            page=page,
            content=pagecontent,
        ))
    return result
