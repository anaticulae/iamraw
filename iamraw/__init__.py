# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os

# annotation
from iamraw.annotation import Annotation
from iamraw.annotation import HyperLink
from iamraw.annotation import Link
from iamraw.annotation import PageAnnotation
from iamraw.annotation import PageAnnotations
from iamraw.annotation import PageLink
from iamraw.annotation import hyperlink_annotations
from iamraw.annotation import pagelink_annotations
# border
from iamraw.border import Border
# boounding
from iamraw.bounding import BoundingBox
from iamraw.bounding import PageBoundings
from iamraw.bounding import PageBoundingsList
from iamraw.bounding import common_box
# boxes
from iamraw.boxes import Box
from iamraw.boxes import HorizontalLine
from iamraw.boxes import PageContentBoxes
from iamraw.boxes import PageContentHorizontals
from iamraw.boxes import PagesWithBoxList
from iamraw.boxes import PagesWithHorizontalList
# document
from iamraw.document import Boxed
from iamraw.document import Char
from iamraw.document import Document
from iamraw.document import Line
from iamraw.document import Page
from iamraw.document import PageObject
from iamraw.document import PageSize
from iamraw.document import TextContainer
from iamraw.document import UnicodeChar
from iamraw.document import VirtualChar
# fonts
from iamraw.fonts import DEFAULT_STRETCH
from iamraw.fonts import DEFAULT_STYLE
from iamraw.fonts import DEFAULT_WEIGHT
from iamraw.fonts import Font
from iamraw.fonts import PageFontContent
from iamraw.fonts import PageFontContents
from iamraw.fonts import Stretch
from iamraw.fonts import Style
from iamraw.fonts import Weight
# headlines
from iamraw.headlines import Headline
from iamraw.headlines import PagesHeadlineList
# list
from iamraw.list import ListType
from iamraw.list import PageList
# pages
from iamraw.page import PageSizeBorder
from iamraw.page import PageSizeBorderList
# sections
from iamraw.sections import AreaItem
from iamraw.sections import DocumentSection
from iamraw.sections import Sections
# text
from iamraw.text import DOT
from iamraw.text import ChapterText
from iamraw.text import Content
from iamraw.text import ContentType
from iamraw.text import PageNumber
from iamraw.text import Paragraph
from iamraw.text import ParagraphContent
from iamraw.text import ParagraphItem
from iamraw.text import Paragraphs
from iamraw.text import Undefined
# textposition
from iamraw.textposition import PageContentTextPosition
from iamraw.textposition import PageContentTextPositions
# table of content
from iamraw.toc import Section
from iamraw.toc import Toc
from iamraw.toc import create_toc

__version__ = '1.6.0'

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
