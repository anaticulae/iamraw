# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import collections
import dataclasses
import typing

import utila

PageContentFormula = collections.namedtuple(
    'PageContentFormula',
    'content page',
)

PageContentFormulas = typing.List[PageContentFormula]


@dataclasses.dataclass
class Formula:
    line: int = None
    lineend: int = None
    char: int = None
    charend: int = None
    raw: str = None


Formulas = typing.List[Formula]

PageContentRawFormula = collections.namedtuple(
    'PageContentRawFormula',
    'content page',
)

PageContentRawFormulas = typing.List[PageContentRawFormula]


@dataclasses.dataclass
class MathChar:
    bounding: tuple = None
    size: float = None
    value: str = None


MathChars = typing.List[MathChar]


@dataclasses.dataclass
class FormulaRaw:

    page: int = None
    content: MathChars = dataclasses.field(default_factory=list)

    def append(self, item):
        self.content.append(item)  # pylint:disable=E1101

    def __getitem__(self, index):
        return self.content[index]  # pylint:disable=E1136

    @property
    def bounding(self) -> tuple:
        boundings = [item.bounding for item in self.content]  # pylint:disable=E1133
        result = utila.rectangle_max(boundings)
        return result

    def __str__(self) -> str:
        raw = ''.join([item.value.strip() for item in self.content])  # pylint:disable=E1133
        return f'FormulaRaw({raw})'


FormulasRaw = typing.List[FormulaRaw]
