# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import dataclasses

import utilo

import iamraw


def dump_hyperlinks(links: iamraw.ExtractedHyperLinks) -> str:
    result = []
    for hyperlink in links:
        result.append(dataclasses.asdict(hyperlink))
    dumped = utilo.yaml_dump(result)
    return dumped


def load_hyperlinks(
    content: str,
    pages: tuple = None,
) -> iamraw.ExtractedHyperLinks:
    loaded = utilo.yaml_load(content)
    result = []
    for item in loaded:
        hyperlink = iamraw.ExtractedHyperLink(**item)
        if utilo.should_skip(hyperlink.page, pages):
            continue
        result.append(hyperlink)
    return result
