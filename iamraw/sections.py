# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import dataclasses
import typing

Page = int
Percentage = float  # start of area [0.0 Pagestart, 100.0 Pageend]
Position = typing.Tuple[Page, Percentage]

PERCENT_100 = 1.0  # analysed by hand


@dataclasses.dataclass
class AreaItem:
    """AreaItem is the smallest piece in document sections analysis

    Every `AreaItem` is constructed of smaller items, like text and/or
    fixgures but this is not analysed here.

    Example:
        document = Sections
        tablearea = DocumentSection
        areaitem = [table of content, table of figures, ...]
    """

    start: Position
    end: Position
    trust: Percentage  # [0.0 100.0]


@dataclasses.dataclass
class DocumentSection:
    """A document is devided in different `DocumentSection`s. These
    areas have different properties. To structure the content of a
    document, different area are required. Eeach `DocumentSection`
    contains different `AreaItem`s."""

    start: Position
    end: Position
    trust: Percentage = dataclasses.field(default=0.0, compare=False)
    content: typing.List[AreaItem] = dataclasses.field(default_factory=list)

    def __getitem__(self, index):
        return self.content[index]  #  pylint:disable=E1136

    def __len__(self):
        return len(self.content)


DocumentSections = typing.List[DocumentSection]


@dataclasses.dataclass
class MultipleSection:
    """Store more than one DocumentSection on a single page."""

    start: Position
    end: Position
    trust: Percentage = dataclasses.field(default=0.0, compare=False)
    content: DocumentSections = dataclasses.field(default_factory=list)

    def __getitem__(self, index):
        return self.content[index]  #  pylint:disable=E1136

    def __len__(self):
        return len(self.content)


@dataclasses.dataclass
class Sections:
    content: typing.List[DocumentSection] = dataclasses.field(
        default_factory=list)

    def __getitem__(self, index):
        return self.content[index]  #  pylint:disable=E1136

    def __len__(self):
        return len(self.content)

    def append(self, item):
        self.content.append(item)  #  pylint:disable=E1101


@dataclasses.dataclass
class Introduction(DocumentSection):
    """Title page, Eidesstattliche Erklaerung, Thank you, Copyright."""


@dataclasses.dataclass
class Unknown(DocumentSection):
    pass


@dataclasses.dataclass
class Table(DocumentSection):
    """Table of content, table of figure, shortcuts"""


@dataclasses.dataclass
class Content(DocumentSection):
    """The main content of a document, in the general, the largest area
    of document."""


@dataclasses.dataclass
class Appendix(DocumentSection):
    pass


@dataclasses.dataclass
class WhitePage(AreaItem):
    pass


@dataclasses.dataclass
class Index(AreaItem):
    pass


@dataclasses.dataclass
class Text(AreaItem):
    pass


@dataclasses.dataclass
class TableOfContent(AreaItem):
    pass


@dataclasses.dataclass
class TitlePage(AreaItem):
    pass


@dataclasses.dataclass
class Chapter(AreaItem):
    number: int = -1
    title: str = ''
