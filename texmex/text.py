# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import dataclasses
import typing


@dataclasses.dataclass
class TextBounds:
    xdist: int
    ydist: int
    width: int
    height: int


@dataclasses.dataclass
class TextBoundsInfo:
    text: str
    bounds: TextBounds

    # TODO: Activate me for hunting bugs
    # def __post_init__(self):
    #     assert isinstance(self.bounds, TextBounds)


TextBoundsInfos = typing.List[TextBoundsInfo]
TextBoundsList = typing.List[TextBounds]

FontSize = int
Occurrence = float
FontOccurrence = typing.Tuple[FontSize, Occurrence]
FontOccurrences = typing.List[FontOccurrence]
