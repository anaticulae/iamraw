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
from texmex.group.fonts import document_textdistance
from texmex.group.fonts import document_textdistance_from_contentnavigators
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
from texmex.group.multiline import group_by_linedistance
from texmex.group.multiline import group_linedistances
from texmex.group.multiline import group_linedistances_complex
from texmex.group.multiline import group_page_by_fontsize
from texmex.group.multiline import group_page_by_size_distance
from texmex.group.multiline import group_pages_by_fontsize
from texmex.group.multiline import linedistance
from texmex.group.multiline import linedistances
from texmex.group.multiline import maxdistance
from texmex.group.multiline import merge_content
from texmex.group.multiline import merge_content_join
from texmex.group.multiline import unite_groups
# iterator
from texmex.iter import PageIter
from texmex.iter import TextContainerIterator
from texmex.iter import split_page
# navigator
from texmex.navigator import END
from texmex.navigator import HORIZONTAL
from texmex.navigator import PTCN
from texmex.navigator import PTN
from texmex.navigator import START
from texmex.navigator import NavigatorMixin
from texmex.navigator import PTCNs
from texmex.navigator import PTNMode
from texmex.navigator import PTNs
from texmex.navigator import SelectBounding
from texmex.navigator import create_pagetextcontentnavigators
from texmex.navigator import create_pagetextnavigator_fromstr
from texmex.navigator import create_pagetextnavigators
from texmex.navigator import determine_border
from texmex.navigator import fill_empty_navigators
from texmex.navigator import navigator_to_bounds
from texmex.navigator import navigator_to_content
from texmex.navigator import rotate_left
from texmex.navigator import single
# style
from texmex.style import HIGHNOTE_RISE_MIN
from texmex.style import CharStyle
from texmex.style import CharStyles
from texmex.style import HighNote
from texmex.style import HighNotes
from texmex.style import PageContentTextItems
from texmex.style import TextInfo
from texmex.style import TextStyle
from texmex.style import create_textstyle
from texmex.style import highnotes
from texmex.style import remove_highnotes
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

# TODO: REMOVE LATER
HIGHNOTE_MIN_RISE = HIGHNOTE_RISE_MIN
