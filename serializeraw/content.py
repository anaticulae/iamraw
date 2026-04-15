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


def dump_contentboundingbox(boxes: iamraw.ContentBoundingBoxes) -> str:
    converted = [(page.page, page.top, page.bottom) for page in boxes]
    dumped = utilo.yaml_dump(converted)
    return dumped


def load_contentboundingbox(
    content: str,
    pages: tuple = None,
) -> iamraw.ContentBoundingBoxes:
    loaded = utilo.yaml_load(
        content,
        fname='groupme__content_content',
    )
    result = []
    for page, top, bottom in loaded:
        if utilo.should_skip(page, pages):
            continue
        result.append(iamraw.ContentBoundingBox(page, top, bottom))
    return result
