# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

from collections import namedtuple
from dataclasses import dataclass
from dataclasses import field
from enum import Enum
from enum import auto
from typing import List

PageFontContent = namedtuple('PageFontContent', 'content page')
PageFontContents = List[PageFontContent]


class Weight(Enum):
    LIGHT = auto()
    MEDIUM = auto()
    BOLD = auto()
    BLACK = auto()


class Style(Enum):
    NORMAL = auto()
    ITALIC = auto()
    OBLIQUE = auto()


class Stretch(Enum):
    # PDF 32000-1:2008 - Table 122
    ULTRACONDENSED = auto()
    EXTRACONDENSED = auto()

    CONDENSED = auto()
    SEMICONDENSED = auto()

    NORMAL = auto()
    REGULAR = auto()  #?

    SEMIEXPANDED = auto()
    EXPANDED = auto()

    EXTRAEXPANDED = auto()
    ULTRAEXPANDED = auto()
    EXTENDED = auto()  #?


def __repr__(self):
    msg = f'{self.__class__.__module__}.{self.__class__.__name__}.{self.name}'
    return msg


# create manually to have valid python code
Stretch.__repr__ = __repr__
Style.__repr__ = __repr__
Weight.__repr__ = __repr__

DEFAULT_WEIGHT = Weight.MEDIUM
DEFAULT_STYLE = Style.NORMAL
DEFAULT_STRETCH = Stretch.REGULAR


@dataclass(unsafe_hash=True)
class Font:
    # DVDJKK+NimbusSanL-Regu
    # JCUGNO+NimbusSanL-Bold
    # CQYGZP+NimbusSanL-BoldItal
    name: str
    scale: float  # NOTE: Remove scale?
    weight: Weight = field(default=DEFAULT_WEIGHT)
    style: Style = field(default=DEFAULT_STYLE)
    stretch: Stretch = field(default=DEFAULT_STRETCH)
