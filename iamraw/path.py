# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utila

con = utila.pathconnector  # pylint:disable=C0103


def text(path: str, prefix: str = '', ftype='yaml') -> str:
    """Add text file name of `rawmaker` to given `path

    Pattern:
        {path}_rawmaker_{prefix}_text_text.yaml

    Args:
        path(str): path to extracted `rawmaker`-content
        prefix(str): optional {prefix} to separate rawmaker-files
        ftype(str): change file type
    Returns:
        comined path
    """
    return con(path, 'rawmaker', 'text_text', prefix, ftype=ftype)


def textposition(path: str, prefix: str = '', ftype='yaml') -> str:
    return con(path, 'rawmaker', 'text_positions', prefix, ftype=ftype)


def outlines(path: str, prefix: str = '', ftype='yaml') -> str:
    return con(path, 'rawmaker', 'outlines_outlines', prefix, ftype=ftype)


def fontheader(path: str, prefix: str = '', ftype='yaml') -> str:
    return con(path, 'rawmaker', 'fonts_header', prefix, ftype=ftype)


def fontcontent(path: str, prefix: str = '', ftype='yaml') -> str:
    return con(path, 'rawmaker', 'fonts_content', prefix, ftype=ftype)


def sizeandborder(path: str, prefix: str = '', ftype='yaml') -> str:
    return con(path, 'rawmaker', 'border_pages', prefix, ftype=ftype)


def horizontals(path: str, prefix: str = '', ftype='yaml') -> str:
    return con(path, 'rawmaker', 'horizontals_horizontals', prefix, ftype=ftype)


def boxed(path: str, prefix: str = '', ftype='yaml') -> str:
    return con(path, 'rawmaker', 'boxes_boxes', prefix, ftype=ftype)


def line(path: str, prefix: str = '', ftype='yaml') -> str:
    return con(path, 'rawmaker', 'line_line', prefix, ftype=ftype)


def images(path: str, prefix: str = '', ftype='yaml') -> str:
    return con(path, 'rawmaker', 'images_images', prefix, ftype=ftype)


def formula(path: str, prefix: str = '', ftype='yaml') -> str:
    return con(path, 'rawmaker', 'formula_formula', prefix, ftype=ftype)


def headerfooters(path: str, prefix: str = '', ftype='yaml') -> str:
    return con(path, 'groupme', 'footer_footerheader', prefix, ftype=ftype)


def toc(path: str, prefix: str = '', ftype='yaml') -> str:
    return con(path, 'groupme', 'toc_toc', prefix, ftype=ftype)


def caption_figure(path: str, prefix: str = '', ftype='yaml') -> str:
    return con(path, 'caption', 'figure_caption', prefix, ftype=ftype)


figure_caption = caption_figure


def caption_image(path: str, prefix: str = '', ftype='yaml') -> str:
    return con(path, 'caption', 'image_caption', prefix, ftype=ftype)


image_caption = caption_image


def caption_table(path: str, prefix: str = '', ftype='yaml') -> str:
    return con(path, 'caption', 'table_caption', prefix, ftype=ftype)


def caption_code(path: str, prefix: str = '', ftype='yaml') -> str:
    return con(path, 'caption', 'code_code', prefix, ftype=ftype)


table_caption = caption_table


def caption_general(path: str, prefix: str = '', ftype='yaml') -> str:
    return con(path, 'caption', 'general_general', prefix, ftype=ftype)


general_cation = caption_general


def caption_result(path: str, prefix: str = '', ftype='yaml') -> str:
    return con(path, 'caption', 'result_result', prefix, ftype=ftype)


def sections_(path: str, prefix: str = '', ftype='yaml') -> str:
    return con(path, 'sections', 'section_result', prefix, ftype=ftype)


def magic_content(path: str, prefix: str = '', ftype='yaml') -> str:
    return con(path, 'magic', 'content_content', prefix, ftype=ftype)


def words_headlines(path: str, prefix: str = '', ftype='yaml') -> str:
    return con(path, 'words', 'headlines_headlines', prefix, ftype=ftype)


def words_headlines_oneline(path: str, prefix: str = '', ftype='yaml') -> str:
    return con(path, 'words', 'headlines_oneline', prefix, ftype=ftype)


def words_text(path: str, prefix: str = '', ftype='yaml') -> str:
    return con(path, 'words', 'text_text', prefix, ftype=ftype)


def words_word(path: str, prefix: str = '', ftype='yaml') -> str:
    return con(path, 'words', 'word_result', prefix, ftype=ftype)


def words_lists(path: str, prefix: str = '', ftype='yaml') -> str:
    return con(path, 'words', 'list_list', prefix, ftype=ftype)


def words_links(path: str, prefix: str = '', ftype='yaml') -> str:
    return con(path, 'words', 'links_links', prefix, ftype=ftype)


def wspace(path: str, prefix: str = '', ftype='yaml') -> str:
    return con(path, 'spacestation', 'wspace_wspace', prefix, ftype=ftype)


def wword(path: str, prefix: str = '', ftype='yaml') -> str:
    return con(path, 'spacestation', 'wspace_words', prefix, ftype=ftype)


def document_chardist(path: str, prefix: str = '', ftype='yaml') -> str:
    return con(path, 'spacestation', 'chardist_chardist', prefix, ftype=ftype)


def document_worddist(path: str, prefix: str = '', ftype='yaml') -> str:
    return con(path, 'spacestation', 'worddist_worddist', prefix, ftype=ftype)


def tablero_result(path: str, prefix: str = '', ftype='yaml') -> str:
    """Path to extraction result of tablero --decide step.

    >>> tablero_result('/data/resources')
    '/data/resources/tablero__decide_decide.yaml'
    """
    return con(path, 'tablero', 'decide_decide', prefix, ftype=ftype)


def codero_result(path: str, prefix: str = '', ftype='yaml') -> str:
    return con(path, 'codero', 'result_result', prefix, ftype=ftype)
