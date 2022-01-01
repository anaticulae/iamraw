# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import dataclasses

import utila
import yaml

import iamraw


def dump_hyperlinks(links: iamraw.ExtractedHyperLinks) -> str:
    result = []
    for hyperlink in links:
        result.append(dataclasses.asdict(hyperlink))
    dumped = yaml.safe_dump(result)
    return dumped


def load_hyperlinks(
    content: str,
    pages: tuple = None,
) -> iamraw.ExtractedHyperLinks:
    content = utila.from_raw_or_path(content, ftype='yaml')
    loaded = yaml.safe_load(content)
    result = []
    for item in loaded:
        hyperlink = iamraw.ExtractedHyperLink(**item)
        if utila.should_skip(hyperlink.page, pages):
            continue
        result.append(hyperlink)
    return result
