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
import serializeraw


def dump_wspaces(pages) -> str:

    def dumper(items: list) -> str:
        raw = [utila.from_tuple(item) for item in items]
        return raw

    dumped = serializeraw.dump_pagecontent(pages, pagedumper=dumper)
    return dumped


def load_wspaces(content: str, pages: tuple = None) -> iamraw.PageContents:

    def loader(items: list) -> iamraw.PageContents:
        loaded = [utila.parse_tuple(item) for item in items]
        return loaded

    loaded = serializeraw.load_pagecontent(
        content=content,
        pages=pages,
        pageloader=loader,
    )
    return loaded
