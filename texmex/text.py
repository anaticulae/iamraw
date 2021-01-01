# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import contextlib
import dataclasses
import typing

import utila

import texmex


@dataclasses.dataclass
class TextBounds:
    leftdist: float
    rightdist: float
    topdist: float
    bottomdist: float


@dataclasses.dataclass
class TextBoundsInfo:
    text: str
    bounds: TextBounds

    # TODO: Activate me for hunting bugs
    # def __post_init__(self):
    #     assert isinstance(self.bounds, TextBounds)


TextBoundsInfos = typing.List[TextBoundsInfo]
TextBoundsList = typing.List[TextBounds]

FontSize = int
Occurrence = float
FontOccurrence = typing.Tuple[FontSize, Occurrence]
FontOccurrences = typing.List[FontOccurrence]


def count_textlines(page: 'texmex.NavigatorMixin', remove_empty=False) -> int:
    """Iterate over `page`-content and extract textlines. If
    `remove_empty` is True, all lines which contain nothing or spaces
    will be ignored.
    """
    content = []
    if isinstance(page, texmex.NavigatorMixin):
        return len([item for item in page if item.text.strip()])

    for item in page:
        with contextlib.suppress(AttributeError):
            content.extend([item.text for item in item.lines])

    if remove_empty:
        content = [item for item in content if item.strip()]
    return len(content)


def connect_text(items) -> str:
    with contextlib.suppress(AttributeError, TypeError):
        items = [item.text for item in items]
    items = [item.replace(utila.NEWLINE, ' ').strip() for item in items]
    # replace trennung
    items = [
        item[0:-1] if item[-1] in ('-', chr(173)) else item for item in items
    ]
    raw = ''.join(items)
    raw = raw.replace(utila.NEWLINE, ' ')
    return raw
