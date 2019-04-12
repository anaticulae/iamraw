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

    def __str__(self):
        return self.text


@dataclass
class TextContainer(PageObject):
    lines: List[Line] = field(default_factory=list)

    @property
    def text(self):
        return ''.join([item.text for item in self.lines])

    def __len__(self):
        return len(self.lines)

    def __getitem__(self, index):
        return self.lines[index]


@dataclass
class Page:
    number: int = 0
    dimension: BoundingBox = None
    children: List[Any] = field(default_factory=list)

    @property
    def text(self):
        result = []
        for item in self.children:
            try:
                result += item.text
            except AttributeError:
                pass
        return ''.join(result)
