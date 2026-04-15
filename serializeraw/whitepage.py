# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import configos
import utilo

import iamraw


def dump_whitepages(pages: iamraw.PageContentWhitepages) -> str:
    """Dump list of `PageContentWhitePage`"""
    result = {}
    if isinstance(pages, list):
        pages = {item.page: item for item in pages}
    for page, value in pages.items():
        result[page] = value.content.name if value.content else None
    dumped = utilo.yaml_dump(result)
    return dumped


@configos.cache_small
def load_whitepages(
    content: str,
    pages=None,
) -> list[iamraw.WhitePage]:
    """Load whitepages from `content`. Content can be a path or loaded
    text data.

    Args:
        content(str): path or content of path
        pages(list): do not load `pages` which are not passed
    Returns:
        list of loaded `WhitePage` type
    """
    loaded = utilo.yaml_load(
        content,
        safe=False,
    )
    result = []
    for pagenumber, whitepage in loaded.items():
        if utilo.should_skip(pagenumber, pages):
            continue
        item = iamraw.PageContentWhitepage(
            page=pagenumber,
            content=iamraw.WhitePage[whitepage] if whitepage else None,
        )
        result.append(item)
    return result
