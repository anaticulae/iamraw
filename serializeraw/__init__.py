#==============================================================================
# C O P Y R I G H T
#------------------------------------------------------------------------------
# Copyright (c) 2019-2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
#==============================================================================
"""Package to load and store raw objects as yaml files.

Reuqired environment variables:

PYTHONHASHSEED:

    This packages requires to set `PYTHONHASHSEED` to ensure that using the
    buildin function `hash` always generates the equal value. If
    `PYTHONHASHSEED` is not set, a random seed is used and therefore
    serializing data is not possible.

"""

# patch yaml dump method
import serializeraw.__patch__
# abbreviations
from serializeraw.abbreviation import dump_abbreviation
from serializeraw.abbreviation import dump_abbreviation_table
from serializeraw.abbreviation import dump_text_abbreviations
from serializeraw.abbreviation import load_abbreviation
from serializeraw.abbreviation import load_abbreviation_table
from serializeraw.abbreviation import load_text_abbreviations
# annotation
from serializeraw.annotation import dump_annotations
from serializeraw.annotation import load_annotations
# bib
from serializeraw.bibliography import dump_bibliography_reference
from serializeraw.bibliography import load_bibliography_reference
# border
from serializeraw.border import dump_leftright_border
from serializeraw.border import dump_pageborders
from serializeraw.border import load_leftright_border
from serializeraw.border import load_pageborders
# bounding
from serializeraw.bounding import dump_boundingboxes
from serializeraw.bounding import load_boundingboxes
# boxedcontent
from serializeraw.boxedcontent import dump_boxedcontent
from serializeraw.boxedcontent import load_boxedcontent
# boxes
from serializeraw.boxes import dump_boxes
from serializeraw.boxes import dump_horizontals
from serializeraw.boxes import load_boxes
from serializeraw.boxes import load_horizontals
# caption
from serializeraw.caption import dump_captions
from serializeraw.caption import load_captions
# chapter
from serializeraw.chapter import dump_chapter
from serializeraw.chapter import load_chapter
# content
from serializeraw.content import dump_contentboundingbox
from serializeraw.content import load_contentboundingbox
# distance
from serializeraw.distance import dump_distance
from serializeraw.distance import load_distance
# docref
from serializeraw.docref import dump_docref
from serializeraw.docref import load_docref
# document
from serializeraw.document import dump_document
from serializeraw.document import load_document
# figures
from serializeraw.figure import dump_figures
from serializeraw.figure import load_figures
# findings
from serializeraw.findings import dump_findings
from serializeraw.findings import load_findings
# fonts
from serializeraw.fonts import convert_flags as load_flags
from serializeraw.fonts import dump_font_content
from serializeraw.fonts import dump_font_header
from serializeraw.fonts import load_font_content
from serializeraw.fonts import load_font_header
from serializeraw.fonts import toflag as dump_flags
# fontstore
from serializeraw.fontstore import create_fontstore
from serializeraw.fontstore import create_fontstore_frompath
# footnotes
from serializeraw.footnotes import load_footnotes
# formula
from serializeraw.formula import dump_formulas
from serializeraw.formula import load_formulas
# formularaw
from serializeraw.formularaw import dump_rawformulas
from serializeraw.formularaw import load_rawformulas
# headerfooter
from serializeraw.headerfooter import dump_footnote
from serializeraw.headerfooter import dump_headerfooter
from serializeraw.headerfooter import load_footnote
from serializeraw.headerfooter import load_headerfooter
# headlines
from serializeraw.headlines import dump_headlines
from serializeraw.headlines import load_headlines
# hits
from serializeraw.hits import dump_hits
from serializeraw.hits import load_hits
# href
from serializeraw.href import dump_hyperlinks
from serializeraw.href import load_hyperlinks
# images
from serializeraw.images import dump_image_info
from serializeraw.images import load_image_info
from serializeraw.images import load_image_infos_frompath
# likelihood
from serializeraw.likelihood import dump_likelihood
from serializeraw.likelihood import load_likelihood
# lines
from serializeraw.line import dump_lines
from serializeraw.line import load_lines
# list
from serializeraw.list import dump_lists
from serializeraw.list import load_lists
# magic
from serializeraw.magic import dump_magic_types
from serializeraw.magic import dump_types
from serializeraw.magic import load_magic_types
from serializeraw.magic import load_types
# content
from serializeraw.pagecontent import dump_pagecontent
from serializeraw.pagecontent import load_pagecontent
# pagenumbers
from serializeraw.pagenumbers import dump_pagenumbers
from serializeraw.pagenumbers import load_pagenumbers
# pdfinfo
from serializeraw.pdfinfo import date_fromstr
from serializeraw.pdfinfo import date_str
from serializeraw.pdfinfo import dump_pdfinfo
from serializeraw.pdfinfo import load_pdfinfo
# quotes
from serializeraw.quote import dump_blockquotes
from serializeraw.quote import dump_quotations
from serializeraw.quote import load_blockquotes
from serializeraw.quote import load_quotations
# sections
from serializeraw.sections import dump_sections
from serializeraw.sections import load_sections
# spacestation
from serializeraw.spacestation import dump_document_chardist
from serializeraw.spacestation import dump_document_worddist
from serializeraw.spacestation import dump_wspaces
from serializeraw.spacestation import dump_wwords
from serializeraw.spacestation import load_document_chardist
from serializeraw.spacestation import load_document_worddist
from serializeraw.spacestation import load_wspaces
from serializeraw.spacestation import load_wwords
# style
from serializeraw.style import dump_doctextstyle
from serializeraw.style import load_doctextstyle
# table
from serializeraw.table import dump_tables
from serializeraw.table import load_tables
# text
from serializeraw.text import dump_text
from serializeraw.text import load_text
# textnavigator
from serializeraw.textnavigator.create import create_pagetextcontentnavigators_fromfile
from serializeraw.textnavigator.create import create_pagetextcontentnavigators_frompath
from serializeraw.textnavigator.create import create_pagetextnavigators_fromfile
from serializeraw.textnavigator.create import create_pagetextnavigators_frompath
from serializeraw.textnavigator.filter import remove_magic
from serializeraw.textnavigator.highnote import dump_highnotes
from serializeraw.textnavigator.highnote import load_highnotes
# textpostions
from serializeraw.textposition import dump_textpositions
from serializeraw.textposition import load_textpositions
# titlepage
from serializeraw.titlepage import dump_titlepage
from serializeraw.titlepage import load_titlepage
# toc
from serializeraw.toc import dump_toc
from serializeraw.toc import load_toc
# utils
from serializeraw.utils import validate
# whitepage
from serializeraw.whitepage import dump_whitepages
from serializeraw.whitepage import load_whitepages
# yamlpages
from serializeraw.yamlpages import dump_yamlpages
from serializeraw.yamlpages import load_yamlpages
from serializeraw.yamlpages import write_yamlpages

ptcn_fromfile = create_pagetextcontentnavigators_fromfile  # pylint:disable=C0103
ptcn_frompath = create_pagetextcontentnavigators_frompath  # pylint:disable=C0103
ptn_fromfile = create_pagetextnavigators_fromfile  # pylint:disable=C0103
ptn_frompath = create_pagetextnavigators_frompath  # pylint:disable=C0103
