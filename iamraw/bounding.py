# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================
"""
    x0,y0 ----------------|
    |                     |
    |    BoundingBox      |
    |                     |
    |-----------------x1,y1
"""
import math
from dataclasses import dataclass
from dataclasses import field
from typing import List
from typing import Tuple

import utila
from utila import INF


@dataclass
class BoundingBox:

    x0: float = -INF
    y0: float = -INF
    x1: float = INF
    y1: float = INF

    def __repr__(self):
        raw = 'BoundingBox(x0=%.2f, y0=%.2f, x1=%.2f, y1=%.2f)'
        return raw % (self.x0, self.y0, self.x1, self.y1)

    def __str__(self):
        return '%.2f %.2f %.2f %.2f' % (self.x0, self.y0, self.x1, self.y1)

    def __getitem__(self, index):
        if index == 0:
            return self.x0
        if index == 1:
            return self.y0
        if index == 2:
            return self.x1
        if index == 3:
            return self.y1
        raise IndexError('index to hight %d > 3' % index)

    def __len__(self):
        return 4

    def __post_init__(self):
        # round to clarify coordinate and avoid confusion in math accuracy
        self.x0 = utila.roundme(self.x0)
        self.x1 = utila.roundme(self.x1)
        self.y0 = utila.roundme(self.y0)
        self.y1 = utila.roundme(self.y1)
        # ensure correct coordinate relation
        assert self.x0 <= self.x1, '%.2f <= %.2f' % (self.x0, self.x1)
        assert self.y0 <= self.y1, '%.2f <= %.2f' % (self.y0, self.y1)

    @classmethod
    def from_list(cls, data):
        """Create `BoundingBox` from list"""
        assert len(data) == 4, 'data has wrong length %d, require 4' % len(data)
        return cls(x0=data[0], y0=data[1], x1=data[2], y1=data[3])

    @classmethod
    def from_str(cls, raw: str):
        """Create `BoundingBox` from raw data which contains 4 floats"""
        splitted = raw.split()
        length = len(splitted)
        assert length == 4, 'wrong split length %d for "%s"' % (length, raw)
        return cls.from_list([float(item) for item in splitted])


def area(bounding) -> float:
    """Determine area out of `BoundingBox` or `tuple(4)`

    Args:
        bounding(BoundingBox/tuple): area to determine size of
    Returns:
        size of bounds [ ]
    """

    assert len(bounding) == 4, str(bounding)
    height = math.fabs(bounding[2] - bounding[0])
    width = math.fabs(bounding[1] - bounding[3])

    result = height * width
    result = utila.roundme(result)
    return result


def common_box(items) -> BoundingBox:
    """Determine largest box which contains the border of all `items`"""
    x0, y0, x1, y1 = INF, INF, -INF, -INF
    for (cx0, cy0, cx1, cy1) in items:
        x0 = min(x0, cx0)
        y0 = min(y0, cy0)
        x1 = max(x1, cx1)
        y1 = max(y1, cy1)
    return BoundingBox.from_list([x0, y0, x1, y1])


@dataclass
class PageBoundings:
    # list of `BoundingBox`es on current `page`
    boundings: List[Tuple[int, BoundingBox]] = field(default_factory=list)
    # current page number
    page: int = 0


PageBoundingsList = List[PageBoundings]
