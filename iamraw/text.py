# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import dataclasses
import enum
import typing

from iamraw.headlines import Headline

DOT = '•'


class ContentType(enum.Enum):
    UNDEFINED = 0
    PARAGRAPH = 1
    BOXED = 2
    LIST = 3


@dataclasses.dataclass
class DocumentContent:
    content: object


@dataclasses.dataclass
class Paragraph(DocumentContent):
    pass


@dataclasses.dataclass
class Undefined(DocumentContent):
    container: int = dataclasses.field(default=-1)
    content: str = None


ChapterText = typing.List[DocumentContent]

PageNumber = int
ParagraphContent = typing.List[str]
ParagraphItem = typing.Tuple[Headline, ParagraphContent]
Paragraphs = typing.List[ParagraphItem]
