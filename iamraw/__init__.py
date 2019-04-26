# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019 by Helmut Konrad Fahrendholz. All rights reserved.
# Tis file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os

# document
from iamraw.document.document import Document
from iamraw.document.page import Char
from iamraw.document.page import Line
from iamraw.document.page import Page
from iamraw.document.page import TextContainer
from iamraw.document.page import VirtualChar
# utils
from iamraw.document.utils import BoundingBox
from iamraw.document.utils import PageObject
# table of content
from iamraw.toc import Section
from iamraw.toc import Toc
from iamraw.toc import create_toc

__version__ = '0.4.4'

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
