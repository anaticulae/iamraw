# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import dataclasses
import typing


@dataclasses.dataclass
class ContentBoundingBox:
    page: int
    top: float
    bottom: float

    def __getitem__(self, index):
        if index == 0:  # pylint:disable=C2001
            return self.top
        if index == 1:
            return self.bottom
        raise IndexError


ContentBoundingBoxes = typing.List[ContentBoundingBox]
