# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================
import collections
import dataclasses
import typing

from iamraw.bounding import BoundingBox

PageContentFooterHeader = collections.namedtuple(
    'PageContentFooterHeader',
    'header, footer, page',
)


@dataclasses.dataclass  # pylint:disable=R0903
class PageInformation:
    value: str = None
    raw: str = None


@dataclasses.dataclass  # pylint:disable=R0903
class HeaderInformation:
    begin: float
    end: float
    page: PageInformation = None


@dataclasses.dataclass  # pylint:disable=R0903
class FooterInformation:
    begin: float
    end: float
    page: PageInformation = None


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


@dataclasses.dataclass  # pylint:disable=R0903
class FixedFooterInformation(FooterInformation):
    pass


@dataclasses.dataclass  # pylint:disable=R0903
class MovingFooterInformation(FooterInformation):
    notes: typing.List[FootNote] = dataclasses.field(default_factory=list)


@dataclasses.dataclass  # pylint:disable=R0903
class PagesFooterInformation(FooterInformation):
    page_location: BoundingBox = None
