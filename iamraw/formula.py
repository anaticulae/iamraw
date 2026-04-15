# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import collections
import dataclasses

import utilo

PageContentFormula = collections.namedtuple(
    'PageContentFormula',
    'content page',
)

PageContentFormulas = list[PageContentFormula]


@dataclasses.dataclass
class Formula:
    line: int = None
    lineend: int = None
    char: int = None
    charend: int = None
    raw: str = None


Formulas = list[Formula]

PageContentRawFormula = collections.namedtuple(
    'PageContentRawFormula',
    'content page',
)

PageContentRawFormulas = list[PageContentRawFormula]


@dataclasses.dataclass
class MathChar:
    bounding: tuple = None
    size: float = None
    value: str = None


MathChars = list[MathChar]


@dataclasses.dataclass
class FormulaRaw:

    page: int = None
    content: MathChars = dataclasses.field(default_factory=list)
    label: str = None
    label_bounding: tuple = None
    """Store reference to formula."""

    def __post_init__(self):
        # assert len(self.sizes) == len(self.raw), f'{len(self.sizes)} == {len(self.raw)}' # yapf:disable
        if len(self.sizes) != len(self.raw):
            utilo.debug(f'{len(self.sizes)} == {len(self.raw)}')
            utilo.debug('XXXX'+utilo.fix_encoding(self.raw)+'XXXX')

    def append(self, item):
        self.content.append(item)  # pylint:disable=E1101

    def __getitem__(self, index):
        return self.content[index]  # pylint:disable=E1136

    @property
    def bounding(self) -> tuple:
        boundings = [item.bounding for item in self.content]  # pylint:disable=E1133
        if self.label_bounding:
            boundings.append(self.label_bounding)
        result = utilo.rect_max(boundings)
        return result

    @property
    def raw(self) -> str:
        result = ''.join([item.value.strip() for item in self.content])  # pylint:disable=E1133
        if self.label:
            result = f'{self.label}:{result}'
        return result

    @property
    def sizes(self) -> utilo.Floats:
        result = [item.size for item in self.content]  # pylint:disable=E1133
        return result

    def __str__(self) -> str:
        return f'FormulaRaw({self.raw})'

    def __repr__(self):
        return str(self)


FormulasRaw = list[FormulaRaw]
