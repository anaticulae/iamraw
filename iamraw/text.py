# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import collections
import dataclasses
import enum
import typing

import iamraw.headlines

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
ChapterTextList = typing.List[ChapterText]

PageNumber = int
ParagraphContent = typing.List[str]
ParagraphItem = typing.Tuple[iamraw.headlines.Headline, ParagraphContent]
Paragraphs = typing.List[ParagraphItem]

PageContentText = collections.namedtuple('PageContentText', 'page, content')
PageContentTexts = typing.List[PageContentText]
