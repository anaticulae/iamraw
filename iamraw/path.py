# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utila

connect = utila.pathconnector  # pylint:disable=C0103


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
    return connect(path, 'rawmaker', 'text_text', prefix)


def textposition(path: str, prefix: str = '') -> str:
    return connect(path, 'rawmaker', 'text_positions', prefix)


def outlines(path: str, prefix: str = '') -> str:
    return connect(path, 'rawmaker', 'outlines_outlines', prefix)


def fontheader(path: str, prefix: str = '') -> str:
    return connect(path, 'rawmaker', 'fonts_header', prefix)


def fontcontent(path: str, prefix: str = '') -> str:
    return connect(path, 'rawmaker', 'fonts_content', prefix)


def sizeandborder(path: str, prefix: str = '') -> str:
    return connect(path, 'rawmaker', 'border_pages', prefix)


def horizontals(path: str, prefix: str = '') -> str:
    return connect(path, 'rawmaker', 'horizontals_horizontals', prefix)


def boxed(path: str, prefix: str = '') -> str:
    return connect(path, 'rawmaker', 'boxes_boxes', prefix)


def line(path: str, prefix: str = '') -> str:
    return connect(path, 'rawmaker', 'line_line', prefix)


def images(path: str, prefix: str = '') -> str:
    return connect(path, 'rawmaker', 'images_images', prefix)


def formula(path: str, prefix: str = '') -> str:
    return connect(path, 'rawmaker', 'formula_formula', prefix)


def headerfooters(path: str, prefix: str = '') -> str:
    return connect(path, 'groupme', 'footer_footerheader', prefix)


def toc(path: str, prefix: str = '') -> str:
    return connect(path, 'groupme', 'toc_toc', prefix)


def caption_figure(path: str, prefix: str = '') -> str:
    return connect(path, 'caption', 'figure_caption', prefix)


figure_caption = caption_figure


def caption_image(path: str, prefix: str = '') -> str:
    return connect(path, 'caption', 'image_caption', prefix)


image_caption = caption_image


def caption_table(path: str, prefix: str = '') -> str:
    return connect(path, 'caption', 'table_caption', prefix)


def caption_code(path: str, prefix: str = '') -> str:
    return connect(path, 'caption', 'code_code', prefix)


table_caption = caption_table


def caption_general(path: str, prefix: str = '') -> str:
    return connect(path, 'caption', 'general_general', prefix)


general_cation = caption_general


def caption_result(path: str, prefix: str = '') -> str:
    return connect(path, 'caption', 'result_result', prefix)


def sections_(path: str, prefix: str = '') -> str:
    return connect(path, 'sections', 'section_result', prefix)


def magic_content(path: str, prefix: str = '') -> str:
    return connect(path, 'magic', 'content_content', prefix)


def words_headlines(path: str, prefix: str = '') -> str:
    return connect(path, 'words', 'headlines_headlines', prefix)


def words_headlines_oneline(path: str, prefix: str = '') -> str:
    return connect(path, 'words', 'headlines_oneline', prefix)


def words_text(path: str, prefix: str = '') -> str:
    return connect(path, 'words', 'text_text', prefix)


def words_word(path: str, prefix: str = '') -> str:
    return connect(path, 'words', 'word_result', prefix)


def words_lists(path: str, prefix: str = '') -> str:
    return connect(path, 'words', 'list_list', prefix)


def words_links(path: str, prefix: str = '') -> str:
    return connect(path, 'words', 'links_links', prefix)


def wspace(path: str, prefix: str = '') -> str:
    return connect(path, 'spacestation', 'wspace_wspace', prefix)


def wword(path: str, prefix: str = '') -> str:
    return connect(path, 'spacestation', 'wspace_words', prefix)


def document_chardist(path: str, prefix: str = '') -> str:
    return connect(path, 'spacestation', 'chardist_chardist', prefix)


def document_worddist(path: str, prefix: str = '') -> str:
    return connect(path, 'spacestation', 'worddist_worddist', prefix)


def tablero_result(path: str, prefix: str = '') -> str:
    """Path to extraction result of tablero --decide step.

    >>> tablero_result('/data/resources')
    '/data/resources/tablero__decide_decide.yaml'
    """
    return connect(path, 'tablero', 'decide_decide', prefix)


def codero_result(path: str, prefix: str = '') -> str:
    return connect(path, 'codero', 'result_result', prefix)
