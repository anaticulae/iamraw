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
from typing import Any
from typing import List

from iamraw.document.utils import BoundingBox
from iamraw.document.utils import Boxed


@dataclass
class Char(Boxed):
    value: str = None
    font: float = None


@dataclass
class VirtualChar:
    value: str = None
    look: int = None


@dataclass
class Line(Boxed):

    chars: List[Char] = field(default_factory=list)

    @property
    def text(self) -> str:
        return ''.join([item.value for item in self.chars])

    def __str__(self):
        return self.text

    def __repr__(self):
        return str(self)[0:-1]  # remove newline

    def __getitem__(self, index):
        return self.chars[index]


@dataclass
class TextContainer(Boxed):
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

    def __repr__(self):
        result = 'Page[%d, %s]\n' % (self.number, self.dimension)
        for item in self.children:
            result += '  %s\n' % item
        return result
