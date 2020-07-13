# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

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


@dataclasses.dataclass
class PageContentText:
    page: int = None
    content: list = None


PageContentTexts = typing.List[PageContentText]


@dataclasses.dataclass
class HeadlineWithContent:
    # TODO: DO WE REQUIRE THIS?
    text: str = None
    content: typing.List[str] = dataclasses.field(default_factory=list)


@dataclasses.dataclass
class TextSection:
    headline: str = None
    content: typing.List = dataclasses.field(default_factory=list)
    pages: typing.List = dataclasses.field(default_factory=list)

    def __getitem__(self, index):
        # TODO: support tuple unpacking, remove later
        if index > 1:
            raise IndexError
        return self.headline if index == 0 else self.content

    def __eq__(self, value):
        # TODO: support tuple unpacking, remove later
        return self[0] == value[0] and self[1] == value[1]


TextSections = typing.List[TextSection]
