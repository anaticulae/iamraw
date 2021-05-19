# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os

import utila

import iamraw
from serializeraw.fonts import load_font_content
from serializeraw.fonts import load_font_header


def create_fontstore(
    header: str,
    content: str,
    pages: tuple = None,
) -> iamraw.FontStore:
    """Load FontStore from `header`-path and `content`-path

    Args:
        header(str): path to saved font-header
        content(str): path to saved font-content
        pages(tuple): pages to load
    Returns:
        created FontStore
    """

    fonts = load_font_header(header)
    pages = load_font_content(content, pages=pages)

    result = iamraw.FontStore(fonts, pages)
    return result


def create_fontstore_frompath(
    path: str,
    prefix: str = '',
    pages: tuple = None,
    logging: bool = True,
) -> iamraw.FontStore:
    header = iamraw.path.fontheader(path, prefix=prefix)
    content = iamraw.path.fontcontent(path, prefix=prefix)

    if not os.path.exists(header):
        if logging:
            utila.error(f'fontstore: {header} does not exists')
        return None
    if not os.path.exists(content):
        if logging:
            utila.error(f'fontstore: {content} does not exists')
        return None
    return create_fontstore(header, content, pages)
