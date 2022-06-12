# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import copy
import dataclasses
import typing

import utila

from iamraw.bounding import BoundingBox


@dataclasses.dataclass
class PageContentFooterHeader:
    header: list = None
    footer: list = None
    page: int = None

    def __getitem__(self, index):
        if not index:
            return self.header
        if index == 1:
            return self.footer
        raise IndexError

    def __repr__(self):
        result = f'PageContentFooterHeader(page={self.page}, '
        if self.header:
            result += 'header='
            result += str(self.header)
            result += ', '
        if self.footer:
            result += 'footer='
            result += str(self.footer)
        result += ')'
        result += utila.NEWLINE * 2
        return result


PageContentFooterHeaders = typing.List[PageContentFooterHeader]


@dataclasses.dataclass
class PageInformation:
    value: str = None
    raw: str = None


@dataclasses.dataclass
class HeaderInformation:
    begin: float = None
    end: float = None
    page: PageInformation = None

    def extend(self, begin=None, end=None):
        """Update area of HeaderInformation. Maximze area."""
        if begin is not None:
            self.begin = min((
                self.begin if self.begin is not None else utila.INF,
                begin,
            ))
        if end is not None:
            self.end = max((self.end if self.end is not None else 0.0, end))


@dataclasses.dataclass
class FooterInformation:
    begin: float = None
    end: float = None
    page: PageInformation = None

    def extend(self, begin=None, end=None):
        """Update area of FooterInformation. Maximze area."""
        if begin is not None:
            self.begin = min(
                self.begin if self.begin is not None else utila.INF,
                begin,
            )
        if end is not None:
            self.end = max(self.end if self.end is not None else 0.0, end)


@dataclasses.dataclass
class FootNote:
    number: int = -1
    page: int = -1
    bounding: tuple = None
    bounding_number: tuple = None

    def __repr__(self):
        raw = f'FootNote(number="{self.number}", page="{self.page}")'
        return raw


FootNotes = typing.List[FootNote]


@dataclasses.dataclass
class FootNoteRaw(FootNote):
    text: str = None
    raw: str = None
    raw_number: str = None
    style: list = dataclasses.field(default_factory=list)
    style_number: 'texmex.CharStyle' = None
    style_text: list = dataclasses.field(default_factory=list)

    def __repr__(self):
        text = '' if not self.text else utila.shrink(self.text, maxlength=300)
        raw = f'FootNoteRaw(number="{self.number}", text="{text}", page="{self.page}")'
        return raw


@dataclasses.dataclass
class FootNoteMerged(FootNote):
    """Merge multiple footnote over multiple pages."""
    notes: FootNotes = dataclasses.field(default_factory=list)

    @property
    def text(self):
        result = utila.normalize_text(self.notes, normalize_spaces=True)
        return result

    @property
    def style(self) -> list:
        # TODO: ADD SEPARATE STYLE FOR HIGHTNOTE AND TEXT
        import texmex
        content, start = [], 0
        highnote = None
        if self.notes and self.notes[0].style:
            highnote = self.notes[0].style[0]
        result = texmex.TextStyle(content=content)
        for note in self.notes:
            if not note.style:
                continue
            for item in note.style[1].content:
                item = copy.deepcopy(item)
                item.start += start
                item.end += start
                content.append(item)
            start = content[-1].end
        return highnote, result

    @property
    def raw_number(self):
        return self.notes[0].raw_number

    @property
    def style_number(self) -> 'texmex.CharStyle':
        return self.notes[0].style_number

    @property
    def style_text(self) -> list:
        return utila.flatten([item.style_text for item in self.notes])

    def __repr__(self):
        raw = f'FootNoteMerged(notes={self.notes})'
        return raw


@dataclasses.dataclass
class FootJudgedNote(FootNote):
    # author: str = None
    # title: str = None
    # year: int = None
    features: list = dataclasses.field(default_factory=list)


@dataclasses.dataclass
class HeaderTitle:
    # XXX: Store location and font?
    title: str = None
    raw: str = None


@dataclasses.dataclass
class HeaderImages:
    number: int = None
    location: BoundingBox = None


@dataclasses.dataclass
class RawText:
    text: str = None


@dataclasses.dataclass
class FixedHeaderInformation(HeaderInformation):
    title: HeaderTitle = None
    undefined: typing.List[RawText] = dataclasses.field(default_factory=list)
    images: typing.List[HeaderImages] = dataclasses.field(default_factory=list)

    def append(self, item):
        if isinstance(item, RawText):
            self.undefined.append(item)  # pylint:disable=E1101
        elif isinstance(item, HeaderImages):
            self.images.append(item)  # pylint:disable=E1101
        else:
            raise ValueError(f'wrong data type: {item}')


@dataclasses.dataclass
class FixedFooterInformation(FooterInformation):
    pass


@dataclasses.dataclass
class MovingFooterInformation(FooterInformation):
    notes: FootNotes = dataclasses.field(default_factory=list)

    def append(self, item):
        self.notes.append(item)  # pylint:disable=E1101

    def __getitem__(self, index):
        return self.notes[index]  # pylint:disable=E1101,E1136

    def __len__(self):
        return len(self.notes)

    def __repr__(self):
        raw = f'MovingFooterInformation(page={self.page}, notes={self.notes})'
        return raw


@dataclasses.dataclass
class PagesFooterInformation(FooterInformation):
    page_location: BoundingBox = None
