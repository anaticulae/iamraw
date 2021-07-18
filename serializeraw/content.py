# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utila
import yaml

import iamraw


def dump_contentboundingbox(boxes: iamraw.ContentBoundingBoxes) -> str:
    converted = [(page.page, page.top, page.bottom) for page in boxes]
    dumped = yaml.safe_dump(converted)
    return dumped


def load_contentboundingbox(
    content: str,
    pages: tuple = None,
) -> iamraw.ContentBoundingBoxes:
    content = utila.from_raw_or_path(
        content,
        fname='groupme__content_content',
        ftype='yaml',
    )
    loaded = yaml.safe_load(content)
    result = []
    for page, top, bottom in loaded:
        if utila.should_skip(page, pages):
            continue
        result.append(iamraw.ContentBoundingBox(page, top, bottom))
    return result
