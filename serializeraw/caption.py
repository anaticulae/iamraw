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


def dump_captions(items: iamraw.PageContentCaptions) -> str:
    # remove empty pages
    items = [item for item in items if item.content]
    # convert to yaml
    dumped = yaml.dump(items)
    return dumped


def load_captions(
        content: str,
        pages: tuple = None,
) -> iamraw.PageContentCaptions:
    content = utila.from_raw_or_path(content, ftype='yaml')
    loaded = yaml.load(content, Loader=yaml.FullLoader)
    result = []
    for page in loaded:
        if utila.should_skip(page.page, pages):
            continue
        result.append(page)
    return result
