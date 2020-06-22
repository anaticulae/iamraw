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
