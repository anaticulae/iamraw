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
from iamraw.border import PageSize
# boxes
from iamraw.boxes import Box
from iamraw.boxes import HorizontalLine
# document
from iamraw.document.document import Document
from iamraw.document.page import Char
from iamraw.document.page import Line
from iamraw.document.page import Page
from iamraw.document.page import TextContainer
from iamraw.document.page import VirtualChar
# utils
from iamraw.document.utils import BoundingBox
from iamraw.document.utils import Boxed
from iamraw.document.utils import PageObject
# fonts
from iamraw.fonts import Font
from iamraw.fonts import Stretch
from iamraw.fonts import Style
from iamraw.fonts import Weight
# table of content
from iamraw.toc import Section
from iamraw.toc import Toc
from iamraw.toc import create_toc

__version__ = '0.4.21'

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
