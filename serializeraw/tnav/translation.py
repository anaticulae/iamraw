# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utila

import texmex


def dump_translations(items: texmex.Translations) -> str:
    dumped = utila.yaml_dump(items, safe=False)
    return dumped


def load_translations(
    content: str,
    pages: tuple = None,
) -> texmex.Translations:
    loaded = utila.yaml_load(content, safe=False)
    result = []
    for page in loaded:
        if utila.should_skip(page.page, pages):
            continue
        result.append(page)
    return result
