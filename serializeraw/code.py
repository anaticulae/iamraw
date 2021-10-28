# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utila

import iamraw


def dump_codes(items: iamraw.PageContentCodes) -> str:
    # remove empty pages
    items = [item for item in items if item.content]
    # convert to yaml
    dumped = utila.yaml_dump(items, safe=False)
    return dumped


def load_codes(
    content: str,
    pages: tuple = None,
) -> iamraw.PageContentCodes:
    loaded = utila.yaml_load(
        content,
        fname='codero__result_result',
        safe=False,
    )
    result = []
    for page in loaded:
        if utila.should_skip(page.page, pages):
            continue
        result.append(page)
    return result
