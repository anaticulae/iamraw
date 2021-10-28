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


def dump_quotations(quotations) -> str:
    result = []
    for page, index, sentence in quotations:
        result.append(f'{page} {index} {sentence}')
    dumped = yaml.dump(result)
    return dumped


def load_quotations(
    content: str,
    pages: tuple = None,
) -> iamraw.ExtractedQuotations:
    loaded = utila.yaml_load(
        content,
        safe=False,
    )
    result = []
    for item in loaded:
        page, index, sentence = item.split(maxsplit=2)
        page = int(page)
        if utila.should_skip(page, pages):
            continue
        index = int(index)
        result.append(iamraw.ExtractedQuotation(page, index, sentence))
    return result
