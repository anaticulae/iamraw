# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

from dataclasses import dataclass
from dataclasses import field
from enum import Enum
from enum import auto


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
    CONDENSED = auto()
    REGULAR = auto()
    EXTENDED = auto()


DEFAULT_WEIGHT = Weight.MEDIUM
DEFAULT_STYLE = Style.NORMAL
DEFAULT_STRETCH = Stretch.REGULAR


@dataclass(unsafe_hash=True)
class Font:
    # DVDJKK+NimbusSanL-Regu
    # JCUGNO+NimbusSanL-Bold
    # CQYGZP+NimbusSanL-BoldItal
    name: str
    scale: float
    weight: Weight = field(default=DEFAULT_WEIGHT)
    style: Style = field(default=DEFAULT_STYLE)
    stretch: Stretch = field(default=DEFAULT_STRETCH)
