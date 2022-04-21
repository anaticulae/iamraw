# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================
"""\
>>> page = Page(page=10, dimension=(0, 0, 768, 912))
>>> page.page
10
>>> page.height
912
"""

import collections
import contextlib
import dataclasses
import typing

import utila

import iamraw.bounding

PageSize = collections.namedtuple('PageSize', 'width height')
PageSizes = typing.List[PageSize]


@dataclasses.dataclass
class PageObject:
    """Object to store every unsupported type"""
    box: iamraw.bounding.BoundingBox = None
    content: str = None


@dataclasses.dataclass
class Page:
    page: int = 0
    dimension: iamraw.bounding.BoundingBox = None
    children: typing.List[typing.Any] = dataclasses.field(default_factory=list)

    @property
    def width(self) -> int:
        if not self.dimension:
            return None
        return self.dimension[2]

    @property
    def height(self) -> int:
        if not self.dimension:
            return None
        return self.dimension[3]

    @property
    def text(self) -> str:
        textcontainer = []
        for item in self.children:  # pylint:disable=E1133
            with contextlib.suppress(AttributeError):
                textcontainer.append(item.text)
        result = utila.NEWLINE.join(textcontainer)
        return result

    def __repr__(self):
        result = (f'\nPage(page={self.page}, dimension={self.dimension})\n'
                  f'{self.text}')
        return result

    def __getitem__(self, key):
        """Iterate over children in page"""
        return self.children[key]  # pylint:disable=E1136

    def append(self, item):
        self.children.append(item)  # pylint:disable=E1101

    def __len__(self) -> int:
        return len(self.children)

    def empty(self) -> bool:
        return not self.children


Pages = typing.List[Page]


@dataclasses.dataclass
class Document:
    """A document describes a parsed PDF file.

    It is possbile to iterate over the different pages to inspect the
    parsed children.
    """
    dimension: PageSize = None
    pages: Pages = dataclasses.field(default_factory=list)

    @property
    def text(self) -> str:
        """Return the raw text of the document separated by pages"""
        texts = []
        for page in self:
            texts.append(page.text)
        result = utila.NEWLINE.join(texts)
        return result

    def append(self, page):
        self.pages.append(page)  # pylint:disable=E1101

    def __len__(self):
        """Return pagecount of document"""
        return len(self.pages)

    def __repr__(self):
        result = [f'Document: pages={len(self.pages)}']
        for page in self:
            result.append(str(page))
        result: str = utila.NEWLINE.join(result)
        return result

    def __getitem__(self, key):
        """Iterate over pages"""
        return self.pages[key]  # pylint: disable=unsubscriptable-object


@dataclasses.dataclass
class Boxed:
    """Object with outlines like a rectangle"""
    box: iamraw.bounding.BoundingBox = None


@dataclasses.dataclass
class Char(Boxed):
    value: str = None
    font: float = None
    size: float = None
    rise: float = None
    underline: bool = False
    """Adobe PDF/9.3.7; Shall specify the distance in unscaled text
    space units to move text the baseline up or down.
    No rise 0, superscripts greater than 0, subscript lower than 0."""
    flags: int = None


Chars = typing.List[Char]


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

    def __getitem__(self, index):
        return self.chars[index]  # pylint:disable=E1136

    def __len__(self):
        return len(self.chars)

    def append(self, char):
        assert isinstance(char, Char), type(char)
        self.chars.append(char)  # pylint:disable=E1101

    @classmethod
    def fromstr(cls, text):
        result = cls()
        for char in text:
            result.append(Char(value=char))
        return result

    def __repr__(self):
        return f'Line(text="{self.text.strip()}")'


Lines = typing.List[Line]


@dataclasses.dataclass
class TextContainer(Boxed):
    lines: Lines = dataclasses.field(default_factory=list)
    state: 'texmex.TextState' = None

    @property
    def text(self) -> str:
        result = ''.join([item.text for item in self])
        return result

    def append(self, item):
        self.lines.append(item)  # pylint:disable=E1101

    def __str__(self) -> str:
        return self.text

    def __getitem__(self, index) -> Line:
        return self.lines[index]  # pylint:disable=E1136

    def __len__(self) -> int:
        return len(self.lines)

    @classmethod
    def fromstr(cls, text, state=None):
        result = cls()
        for line in text.splitlines():
            # ensure that line ends with newline
            line = line + utila.NEWLINE
            result.append(Line.fromstr(line))
        result.state = state
        return result

    @property
    def textstate(self) -> 'texmex.TextState':
        """\
        >>> TextContainer().textstate
        <TextState.VISIBLE:...>
        """
        import texmex
        if self.state is None:
            # if no state is given, use visible the default state
            return texmex.TextState.VISIBLE
        return self.state

    @property
    def visible(self):
        import texmex
        return self.textstate == texmex.TextState.VISIBLE


TextContainers = typing.List[TextContainer]


@dataclasses.dataclass
class VerticalTextContainer(TextContainer):
    pass


VerticalTextContainers = typing.List[VerticalTextContainer]
