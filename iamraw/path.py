# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utila


def text(path: str, prefix: str = '') -> str:
    """Add text file name of `rawmaker` to given `path

    Pattern:
        {path}_rawmaker_{prefix}_text_text.yaml

    Args:
        path(str): path to extracted `rawmaker`-content
        prefix(str): optional {prefix} to separate rawmaker-files
    Returns:
        comined path
    """
    return utila.pathconnector(path, 'rawmaker', 'text_text', prefix)


def textposition(path: str, prefix: str = '') -> str:
    return utila.pathconnector(path, 'rawmaker', 'text_positions', prefix)


def toc(path: str, prefix: str = '') -> str:
    return utila.pathconnector(path, 'rawmaker', 'toc_toc', prefix)


def fontheader(path: str, prefix: str = '') -> str:
    return utila.pathconnector(path, 'rawmaker', 'fonts_header', prefix)


def fontcontent(path: str, prefix: str = '') -> str:
    return utila.pathconnector(path, 'rawmaker', 'fonts_content', prefix)


def sizeandborder(path: str, prefix: str = '') -> str:
    return utila.pathconnector(path, 'rawmaker', 'border_pages', prefix)


def horizontals(path: str, prefix: str = '') -> str:
    return utila.pathconnector(path, 'rawmaker', 'boxes_horizontal', prefix)


def boxed(path: str, prefix: str = '') -> str:
    return utila.pathconnector(path, 'rawmaker', 'boxes_boxes', prefix)


def line(path: str, prefix: str = '') -> str:
    return utila.pathconnector(path, 'rawmaker', 'line_line', prefix)


def headerfooters(path: str, prefix: str = '') -> str:
    return utila.pathconnector(
        path,
        'groupme',
        'footer_footerheader',
        prefix,
    )
