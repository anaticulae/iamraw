# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import contextlib
import dataclasses
import re

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


TextBoundsInfos = list[TextBoundsInfo]
TextBoundsList = list[TextBounds]

FontSize = int
Occurrence = float
FontOccurrence = tuple[FontSize, Occurrence]
FontOccurrences = list[FontOccurrence]


def count_textlines(page: 'texmex.NavigatorMixin', remove_empty=False) -> int:
    """Iterate over `page`-content and extract textlines.

    If `remove_empty` is True, all lines which contain nothing or spaces
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


def connect_text(
    items,
    merge_divis: bool = True,
    normalize_newline: bool = True,
    normalize_spaces: bool = False,
) -> str:
    r"""\
    >>> connect_text(['Dieser Satz ent-\n', 'hält eine Trennung.'], merge_divis=True)
    'Dieser Satz enthält eine Trennung.'
    >>> connect_text(['Der Stadtteil Berlin-\n', 'Neuköln liegt im Süden von Berlin.'])
    'Der Stadtteil Berlin-Neuköln liegt im Süden von Berlin.'
    >>> connect_text(['Das  sind   eindeutig zu   viele Trennungen.'], normalize_spaces=True)
    'Das sind eindeutig zu viele Trennungen.'
    >>> connect_text(['Special Char' + chr(173) + '\n', 'sol hier'])
    'Special Charsol hier'
    >>> connect_text([''])
    ''
    """
    # prepare input data
    with contextlib.suppress(AttributeError, TypeError):
        items = [item.text for item in items]
    text = ''.join(items)
    if merge_divis:
        # Ensure that divis of following UpperCase-Word is not merged
        # TODO: IMPORVE REGEX
        text = re.sub(r'[-\xad]\n(?P<data>[a-zäöü])', r'\g<data>', text)
        text = re.sub(r'[-\xad]\n(?P<data>[A-ZÄÖÜ])', r'-\g<data>', text)
    if normalize_newline:
        text = text.replace('\n', ' ')
    if normalize_spaces:
        text = re.sub(r'\s+', ' ', text)
    return text
