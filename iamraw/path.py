# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import warnings

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


def images(path: str, prefix: str = '', ftype='') -> str:
    return con(path, 'rawmaker', 'images_images', prefix, ftype=ftype)


def formula(path: str, prefix: str = '', ftype='yaml') -> str:
    return con(path, 'rawmaker', 'formula_formula', prefix, ftype=ftype)


def caption_figure(path: str, prefix: str = '', ftype='yaml') -> str:
    # TODO: REMOVE WITH NEXT MAJOR
    warnings.warn('use caption_image, caption_figure will be removed later')
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


def words_sentences(path: str, prefix: str = '', ftype='yaml') -> str:
    return con(path, 'words', 'sentences_sentences', prefix, ftype=ftype)


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


def groupme_abbreviation(path: str, prefix: str = '', ftype='yaml') -> str:
    return con(path, 'groupme', 'abbreviation_abbreviation', prefix, ftype=ftype)  # yapf:disable


def groupme_area(path: str, prefix: str = '', ftype='yaml') -> str:
    return con(path, 'groupme', 'area_area', prefix, ftype=ftype)


def groupme_border_leftright(path: str, prefix: str = '', ftype='yaml') -> str:
    return con(path, 'groupme', 'border_leftright', prefix, ftype=ftype)


def groupme_distance(path: str, prefix: str = '', ftype='yaml') -> str:
    return con(path, 'groupme', 'distance_distance', prefix, ftype=ftype)


def groupme_pagenumbers(path: str, prefix: str = '', ftype='yaml') -> str:
    return con(path, 'groupme', 'pagenumbers_pagenumbers', prefix, ftype=ftype)


def groupme_headerfooters(path: str, prefix: str = '', ftype='yaml') -> str:
    return con(path, 'groupme', 'footer_footerheader', prefix, ftype=ftype)


headerfooters = groupme_headerfooters


def groupme_toc(path: str, prefix: str = '', ftype='yaml') -> str:
    return con(path, 'groupme', 'toc_toc', prefix, ftype=ftype)


toc = groupme_toc


def groupme_figuretable(path: str, prefix: str = '', ftype='yaml') -> str:
    return con(path, 'groupme', 'figuretable_figuretable', prefix, ftype=ftype)


def groupme_tabletable(path: str, prefix: str = '', ftype='yaml') -> str:
    return con(path, 'groupme', 'tabletable_tabletable', prefix, ftype=ftype)


def reftable_toc(path: str, prefix: str = '', ftype='yaml') -> str:
    return con(path, 'reftable', 'toc_toc', prefix, ftype=ftype)


def reftable_figure(path: str, prefix: str = '', ftype='yaml') -> str:
    return con(path, 'reftable', 'figure_figure', prefix, ftype=ftype)


def reftable_table(path: str, prefix: str = '', ftype='yaml') -> str:
    return con(path, 'reftable', 'table_table', prefix, ftype=ftype)


def reftable_abbrev(path: str, prefix: str = '', ftype='yaml') -> str:
    return con(path, 'reftable', 'abbrev_abbrev', prefix, ftype=ftype)


def pdfinfo(path: str) -> str:
    return utila.join(path, 'pdfinfo.yaml')


def smarty_phrases(path: str, prefix: str = '') -> str:
    return con(path, 'smarty', 'phrases_phrases', prefix)


def smarty_pleonasmas(path: str, prefix: str = '') -> str:
    return con(path, 'smarty', 'pleonasma_pleonasma', prefix)


def smarty_reduces(path: str, prefix: str = '') -> str:
    return con(path, 'smarty', 'reduce_reduce', prefix)


def smarty_spelling_hyphen(path: str, prefix: str = '') -> str:
    return con(path, 'smarty', 'spelling_hyphen', prefix)


def smarty_spelling_guess(path: str, prefix: str = '') -> str:
    return con(path, 'smarty', 'spelling_guess', prefix)
