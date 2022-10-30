# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import collections
import dataclasses

import utila

PageContentCode = collections.namedtuple(
    'PageContentCode',
    'page content',
)
PageContentCodes = list[PageContentCode]


@dataclasses.dataclass
class PeaceOfCode:
    caption: tuple[int] = dataclasses.field(default_factory=tuple)
    tokens: tuple[int] = dataclasses.field(default_factory=tuple)
    tokens_bounding: list = dataclasses.field(default_factory=list)
    caption_bounding: list = dataclasses.field(default_factory=list)
    page: int = None

    @property
    def identifier(self) -> int:
        """\
        >>> PeaceOfCode(tokens_bounding=[(10, 10, 10, 10)], page=5).identifier
        90015...0
        """
        bounding = utila.rect_max(self.tokens_bounding)
        return utila.pagebox_hash(page=self.page, box=bounding)


PeaceOfCodes = list[PeaceOfCode]
