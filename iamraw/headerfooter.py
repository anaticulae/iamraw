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
import typing

import utila

from iamraw.bounding import BoundingBox

PageContentFooterHeader = collections.namedtuple(
    'PageContentFooterHeader',
    'header, footer, page',
)

PageContentFooterHeaders = typing.List[PageContentFooterHeader]


@dataclasses.dataclass  # pylint:disable=R0903
class PageInformation:
    value: str = None
    raw: str = None


@dataclasses.dataclass  # pylint:disable=R0903
class HeaderInformation:
    begin: float = None
    end: float = None
    page: PageInformation = None

    def extend(self, begin=None, end=None):
        """Update area of HeaderInformation. Maximze area."""
        if begin is not None:
            self.begin = min(
                self.begin if self.begin is not None else utila.INF,
                begin,
            )
        if end is not None:
            self.end = max(self.end if self.end is not None else 0.0, end)


@dataclasses.dataclass  # pylint:disable=R0903
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


@dataclasses.dataclass  # pylint:disable=R0903
class FootNote:
    number: int
    text: str
    raw: str
    author: str = None
    title: str = None
    year: int = None


@dataclasses.dataclass  # pylint:disable=R0903
class HeaderTitle:
    # XXX: Store location and font?
    title: str = None
    raw: str = None


@dataclasses.dataclass  # pylint:disable=R0903
class HeaderImages:
    number: int = None
    location: BoundingBox = None


@dataclasses.dataclass  # pylint:disable=R0903
class RawText:
    text: str = None


@dataclasses.dataclass  # pylint:disable=R0903
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


@dataclasses.dataclass  # pylint:disable=R0903
class FixedFooterInformation(FooterInformation):
    pass


@dataclasses.dataclass  # pylint:disable=R0903
class MovingFooterInformation(FooterInformation):
    notes: typing.List[FootNote] = dataclasses.field(default_factory=list)

    def append(self, item):
        self.notes.append(item)  # pylint:disable=E1101

    def __getitem__(self, index):
        return self.notes[index]  # pylint:disable=E1101,E1136

    def __len__(self):
        return len(self.notes)


@dataclasses.dataclass  # pylint:disable=R0903
class PagesFooterInformation(FooterInformation):
    page_location: BoundingBox = None
