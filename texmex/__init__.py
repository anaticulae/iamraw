# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

# alignment
from texmex.alignment import TextAlignment
from texmex.alignment import TextAlignments
# character
from texmex.character import DOT
# group
from texmex.group.fonts import bounds_to_textbounds
from texmex.group.fonts import document_textdist_from_ptcns
from texmex.group.fonts import document_textdistance
from texmex.group.fonts import document_textfeed
from texmex.group.fonts import document_textsize
from texmex.group.fonts import feeddistance
from texmex.group.fonts import fontdistance
from texmex.group.fonts import fontdistance_textbounds
from texmex.group.fonts import textbounds
from texmex.group.fonts import textsize
from texmex.group.fonts import textsize_frompage
from texmex.group.multiline import MultilineGroup
from texmex.group.multiline import PageContentMultiLine
from texmex.group.multiline import group_linedistances
from texmex.group.multiline import group_page_by_fontsize
from texmex.group.multiline import group_page_by_size_distance
from texmex.group.multiline import group_pages_by_fontsize
from texmex.group.multiline import groupby_linedistance
from texmex.group.multiline import linedistance
from texmex.group.multiline import linedistances
from texmex.group.multiline import maxdistance
from texmex.group.multiline import merge_content
from texmex.group.multiline import merge_content_join
from texmex.group.multiline import unite_groups
from texmex.group.multiline.complex import group_linedistances_complex
# iterator
from texmex.iter import PageIter
from texmex.iter import TextContainerIterator
from texmex.iter import split_page
# navigator
from texmex.navigator import BEGIN
from texmex.navigator import END
from texmex.navigator import PTCN
from texmex.navigator import PTN
from texmex.navigator import NavigatorMixin
from texmex.navigator import NavigatorMixins
from texmex.navigator import PTCNs
from texmex.navigator import PTNs
from texmex.navigator import SelectBounding
from texmex.navigator import navigator_to_bounds
from texmex.navigator import navigator_to_content
from texmex.navigator import rotate_left
from texmex.navigator import single
# navigator:create
from texmex.navigator.create import HORIZONTAL
from texmex.navigator.create import PTNMode
from texmex.navigator.create import create_ptcns
from texmex.navigator.create import create_ptns
from texmex.navigator.create import determine_border
from texmex.navigator.create import fill_empty_navigators
from texmex.navigator.create import ptn_fromstr
# search
from texmex.search import search_area
# sentences
from texmex.sentences import SentenceType
from texmex.sentences import is_formula
from texmex.sentences import is_list
from texmex.sentences import is_listitem
from texmex.sentences import is_listsepa
from texmex.sentences import is_quote
from texmex.sentences import list_split
from texmex.sentences import nosentence
from texmex.sentences import sentence_type
# style
from texmex.style import HIGHNOTE_RISE_MIN
from texmex.style import CharStyle
from texmex.style import CharStyles
from texmex.style import HighNote
from texmex.style import HighNotes
from texmex.style import PageContentTextItems
from texmex.style import TextInfo
from texmex.style import TextLineStyle
from texmex.style import TextState
from texmex.style import TextStyle
from texmex.style import create_textstyle
from texmex.style import highnotes
from texmex.style import remove_highnotes
from texmex.style import splitby_count
from texmex.style import style_without_highnotes
# text
from texmex.text import FontOccurrence
from texmex.text import FontOccurrences
from texmex.text import FontSize
from texmex.text import Occurrence
from texmex.text import TextBounds
from texmex.text import TextBoundsInfo
from texmex.text import TextBoundsInfos
from texmex.text import connect_text
from texmex.text import count_textlines
# translation
from texmex.translation import Translation
from texmex.translation import TranslationLookup
from texmex.translation import Translations
# utils
from texmex.utils import topbottom

PageTextContentNavigator = PTCN
PageTextContentNavigators = PTCNs
PageTextNavigator = PTN
PageTextNavigators = PTNs
PageTextNavigatorMode = PTNMode
document_textdistance_from_contentnavigators = document_textdist_from_ptcns
group_by_linedistance = groupby_linedistance

create_pagetextnavigator_fromstr = ptn_fromstr
create_pagetextnavigators = create_ptns
create_pagetextcontentnavigators = create_ptcns

# TODO: REMOVE LATER
HIGHNOTE_MIN_RISE = HIGHNOTE_RISE_MIN
START = BEGIN
