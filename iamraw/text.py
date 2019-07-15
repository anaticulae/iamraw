# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================
from dataclasses import dataclass
from dataclasses import field
from enum import Enum
from typing import List
from typing import Tuple

from iamraw.headlines import Headline

DOT = '•'


class ContentType(Enum):
    UNDEFINED = 0
    PARAGRAPH = 1
    BOXED = 2
    LIST = 3


@dataclass
class Content:
    content: object


@dataclass
class Paragraph(Content):
    pass


@dataclass
class Undefined(Content):
    container: int = field(default=-1)
    content: str = None


ChapterText = List[Content]

PageNumber = int
ParagraphContent = List[str]
ParagraphItem = Tuple[Headline, ParagraphContent]
Paragraphs = List[ParagraphItem]
