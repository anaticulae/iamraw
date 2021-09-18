# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import collections
import dataclasses
import typing

PageContentCode = collections.namedtuple(
    'PageContentCode',
    'page content',
)
PageContentCodes = typing.List[PageContentCode]


@dataclasses.dataclass
class PeaceOfCode:
    caption: typing.Set[int] = dataclasses.field(default_factory=set)
    tokens: typing.Set[int] = dataclasses.field(default_factory=set)
    tokens_bounding: list = dataclasses.field(default_factory=list)
    caption_bounding: list = dataclasses.field(default_factory=list)


PeaceOfCodes = typing.List[PeaceOfCode]
