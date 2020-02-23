# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================
import collections
import contextlib
import dataclasses
import typing

import utila

from iamraw.bounding import BoundingBox

PageSize = collections.namedtuple('PageSize', 'width height')


@dataclasses.dataclass
class PageObject:
    """Object to store every unsupported type"""
    box: BoundingBox = None
    content: str = None


@dataclasses.dataclass
class Page:
    page: int = 0
    dimension: BoundingBox = None
    children: typing.List[typing.Any] = dataclasses.field(default_factory=list)

    @property
    def text(self):
        result = []
        for item in self.children:  # pylint:disable=E1133
            with contextlib.suppress(AttributeError):
                result += item.text
        return ''.join(result)

    def __repr__(self):
        result = f'Page(page={self.page}, dimension={self.dimension})\n'
        content = ''.join([f'  {item}\n' for item in self.children])  # pylint:disable=E1133
        return result + content

    def __getitem__(self, key):
        """Iterate over children in page"""
        return self.children[key]  # pylint:disable=E1136

    def append(self, item):
        self.children.append(item)  # pylint:disable=E1101

    def __len__(self) -> int:
        return len(self.children)

    def empty(self) -> bool:
        return len(self) == 0


@dataclasses.dataclass
class Document:
    """A document describes a parsed PDF file. It is possbile to iterate over
    the different pages to inspect the parsed children."""
    dimension: PageSize = None
    pages: typing.List[Page] = dataclasses.field(default_factory=list)

    @property
    def text(self):
        """Return the raw text of the document separated by pages"""
        texts = []
        for page in self.pages:  # pylint: disable=not-an-iterable
            texts.append(page.text)
        return ''.join(texts)

    def __len__(self):
        """Return pagecount of document"""
        return len(self.pages)

    def __repr__(self):
        result = 'Document: pages[%d]\n' % len(self.pages)

        for page in self.pages:  # pylint: disable=not-an-iterable
            result += str(page) + utila.NEWLINE
        return result

    def __getitem__(self, key):
        """Iterate over pages"""
        return self.pages[key]  # pylint: disable=unsubscriptable-object


@dataclasses.dataclass
class Boxed:
    """Object with outlines like a rectangle"""
    box: BoundingBox = None


@dataclasses.dataclass
class Char(Boxed):
    value: str = None
    font: float = None
    size: float = None
    rise: float = None
    """Adobe PDF/9.3.7; Shall specify the distance in unscaled text
    space units to move text the baseline up or down.
    No rise 0, superscripts greater than 0, subscript lower than 0."""


@dataclasses.dataclass
class UnicodeChar(Char):
    special: str = None


@dataclasses.dataclass
class VirtualChar:
    value: str = None
    look: int = None
    size: float = None
    rise: float = None


@dataclasses.dataclass
class Line(Boxed):

    chars: typing.List[Char] = dataclasses.field(default_factory=list)

    @property
    def text(self) -> str:
        # pylint:disable=E1133
        return ''.join([item.value for item in self.chars])

    def __str__(self):
        return self.text

    def __repr__(self):
        # remove newline
        return str(self)[0:-1]

    def __getitem__(self, index):
        return self.chars[index]  # pylint:disable=E1136

    def __len__(self):
        return len(self.chars)


@dataclasses.dataclass
class TextContainer(Boxed):
    lines: typing.List[Line] = dataclasses.field(default_factory=list)

    @property
    def text(self):
        return ''.join([item.text for item in self.lines])  # pylint:disable=E1133

    def __len__(self):
        return len(self.lines)

    def __getitem__(self, index):
        return self.lines[index]  # pylint:disable=E1136


TextContainers = typing.List[TextContainer]
