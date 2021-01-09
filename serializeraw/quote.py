# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utila
import yaml

import iamraw


def dump_blockquotes(blockquotes: iamraw.PageContentBlockQuotesList) -> str:
    converted = [(page.page, page.content) for page in blockquotes]
    dumped = yaml.safe_dump(converted)
    return dumped


def load_blockquotes(
        content: str,
        pages: tuple = None,
) -> iamraw.PageContentBlockQuotesList:
    content = utila.from_raw_or_path(content, ftype='yaml')
    loaded = yaml.safe_load(content)
    result = []
    for page, pagecontent in loaded:
        if utila.should_skip(page, pages):
            continue
        result.append(
            iamraw.PageContentBlockQuotes(
                page=page,
                content=pagecontent,
            ))
    return result
