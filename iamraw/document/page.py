# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019 by Helmut Konrad Fahrendholz. All rights reserved.
# Tis file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

from dataclasses import dataclass
from dataclasses import field
from typing import Any
from typing import List

from iamraw.document.utils import BoundingBox
from iamraw.document.utils import PageObject
from utila import INF
from utila import NEWLINE


@dataclass
class Char(PageObject):
    value: str = None
    size: float = None
    font: float = None
    style: float = None  # bold, italic, underline


@dataclass
class VirtualChar():
    value: str = None
    look: int = None


@dataclass
class Line(PageObject):

    chars: List[Char] = field(default_factory=list)

    @property
    def text(self) -> str:
        return ''.join([item.value for item in self.chars])

    @classmethod
    def from_str(cls, content: str):
        chars = [Char(value=item) for item in content]
        return cls(chars=chars)


@dataclass
class TextContainer(PageObject):
    lines: List[Line] = field(default_factory=list)

    @property
    def text(self):
        return NEWLINE.join([item.text for item in self.lines])


@dataclass
class Page:
    number: int = 0
    dimension: BoundingBox = None
    children: List[Any] = field(default_factory=list)
