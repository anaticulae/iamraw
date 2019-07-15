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
from typing import List
from typing import Tuple


class ListType(Enum):
    UNDEFINED = None
    AMBIGUOUS = '*1.+-'
    DOTTED = '*'
    NUMBERED = '123'
    NUMBERED_WITH_DOT = '1.5.9.'  # default style
    PLUSED = '+'
    MINUSED = '-'


@dataclass
class PageList:

    data: List[Tuple[str, str]] = field(default_factory=list)
    area: List[int] = field(default_factory=list)

    def append(self, title: str, level: str = None):
        self.data.append((level, title))

    def __getitem__(self, index):
        return self.data[index]

    def __len__(self):
        return len(self.data)

    def ltype(self):
        return ListType.UNDEFINED
