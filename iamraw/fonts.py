# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import collections
import dataclasses
import enum

import utilo

PageFontContent = collections.namedtuple('PageFontContent', 'content page')
PageFontContents = list[PageFontContent]


class FontFlag(enum.Enum):
    FIXEDPITCH = 1
    SERIF = 2
    SYMBOLIC = 3
    SCRIPT = 4
    NONSYMBOLIC = 6
    ITALIC = 7
    # font does not contain any upper case letter - this is used for titles etc.
    ALLCAP = 17
    # contains uppercase and lowercase letters
    SMALLCAP = 18
    FORCEBOLD = 19


FontFlags = tuple[FontFlag]


class Weight(enum.Enum):
    LIGHT = enum.auto()
    MEDIUM = enum.auto()
    BOLD = enum.auto()
    BLACK = enum.auto()


class Style(enum.Enum):
    NORMAL = enum.auto()
    ITALIC = enum.auto()
    OBLIQUE = enum.auto()


class Stretch(enum.Enum):
    # PDF 32000-1:2008 - Table 122
    ULTRACONDENSED = enum.auto()
    EXTRACONDENSED = enum.auto()

    CONDENSED = enum.auto()
    SEMICONDENSED = enum.auto()

    NORMAL = enum.auto()
    REGULAR = enum.auto()  #?

    SEMIEXPANDED = enum.auto()
    EXPANDED = enum.auto()

    EXTRAEXPANDED = enum.auto()
    ULTRAEXPANDED = enum.auto()
    EXTENDED = enum.auto()  #?


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


@dataclasses.dataclass
class Font:
    # DVDJKK+NimbusSanL-Regu
    # JCUGNO+NimbusSanL-Bold
    # CQYGZP+NimbusSanL-BoldItal
    pdfref: str = None
    name: str = dataclasses.field(default=None, compare=False, hash=False, repr=False)  # yapf:disable
    scale: float = None  # NOTE: Remove scale?
    weight: Weight = dataclasses.field(default=DEFAULT_WEIGHT)
    style: Style = dataclasses.field(default=DEFAULT_STYLE)
    stretch: Stretch = dataclasses.field(default=DEFAULT_STRETCH)
    flags: tuple = None
    """Reference used in pdf document."""

    def __hash__(self):
        """\
        font name is not part of hash value
        >>> assert hash(Font(name='abc')) ==  hash(Font(name=''))
        """
        # TODO: VERIFY THIS
        raw = bytes(str(self), 'utf8')
        hashed = utilo.binhash(raw)
        return hashed
