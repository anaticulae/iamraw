# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import dataclasses
import enum

import iamraw.headlines


class ContentType(enum.Enum):
    # TODO: REMOVE, USE PageContentType instead!
    UNDEFINED = 0
    PARAGRAPH = 1
    BOXED = 2
    LIST = 3


@dataclasses.dataclass
class DocumentContent:
    content: object
    bounding: tuple = dataclasses.field(default=None)


@dataclasses.dataclass
class Paragraph(DocumentContent):

    def __repr__(self):
        return f"Paragraph(content='{str(self.content).strip()}')"


@dataclasses.dataclass
class Undefined(DocumentContent):
    container: int = dataclasses.field(default=-1)
    content: str = None


@dataclasses.dataclass
class DFormula(DocumentContent):
    number: int = dataclasses.field(default=-1)


ChapterText = list[DocumentContent]
ChapterTextList = list[ChapterText]

PageNumber = int
ParagraphContent = list[str]
ParagraphItem = tuple[iamraw.headlines.Headline, ParagraphContent]
Paragraphs = list[ParagraphItem]


@dataclasses.dataclass
class PageContentText:
    page: int = None
    content: list = None


PageContentTexts = list[PageContentText]


@dataclasses.dataclass
class HeadlineWithContent:
    # TODO: DO WE REQUIRE THIS?
    text: str = None
    content: list[str] = dataclasses.field(default_factory=list)


@dataclasses.dataclass
class TextSection:
    headline: str = None
    content: list = dataclasses.field(default_factory=list)
    pages: list = dataclasses.field(default_factory=list)

    def __getitem__(self, index):
        # TODO: support tuple unpacking, remove later
        if index > 1:
            raise IndexError
        return self.headline if not index else self.content

    def __eq__(self, value):
        # TODO: support tuple unpacking, remove later
        return self[0] == value[0] and self[1] == value[1]

    def __hash__(self):
        return hash(str(self))


TextSections = list[TextSection]
