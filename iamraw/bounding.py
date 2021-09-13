# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================
"""Bounding
========

The BoundingBox describes a rectangle which contains the area of the
described item which the box refers.

.. code-block:: none

    x0,y0 ----------------|
    |                     |
    |    BoundingBox      |
    |                     |
    |-----------------x1,y1
"""

import dataclasses
import typing

import utila


@dataclasses.dataclass(unsafe_hash=True)
class BoundingBox:
    """\
    Let's start with an simple rectangle/box:

    >>> BoundingBox(10.5, 13.2, 23.33, 30.0)
    BoundingBox(x0=10.5, y0=13.2, x1=23.33, y1=30.0)

    Ensure that hashing works properly:
    >>> assert hash(BoundingBox(x0=10.5, y0=13.2, x1=23.33, y1=30.0))

    Ensure that comparing works:
    >>> assert BoundingBox(10.5, 13.2, 23.33, 30.0) == BoundingBox(10.5, 13.2, 23.33, 30.0)
    """

    x0: float = -utila.INF
    y0: float = -utila.INF
    x1: float = utila.INF
    y1: float = utila.INF

    def __repr__(self):
        result = (f'BoundingBox(x0={self.x0}, y0={self.y0}, '
                  f'x1={self.x1}, y1={self.y1})')
        return result

    def __str__(self):
        return f'{self.x0} {self.y0} {self.x1} {self.y1}'

    def __getitem__(self, index):
        if index == 0:  # pylint:disable=C2001
            return self.x0
        if index == 1:
            return self.y0
        if index == 2:
            return self.x1
        if index == 3:
            return self.y1
        raise IndexError(f'index out of range: {index}>3')

    def __setitem__(self, index, value):
        """Set `value` depending on `index`.

        >>> box = BoundingBox()
        >>> box[1] = 10
        >>> box.y0
        10
        """
        if index == 0:  # pylint:disable=C2001
            self.x0 = value
        elif index == 1:
            self.y0 = value
        elif index == 2:
            self.x1 = value
        elif index == 3:
            self.y1 = value
        else:
            raise IndexError(f'index out of range: {index}>3')

    def __len__(self):
        return 4

    def __post_init__(self):
        # round to clarify coordinate and avoid confusion in math accuracy
        self.x0 = utila.roundme(self.x0)
        self.x1 = utila.roundme(self.x1)
        self.y0 = utila.roundme(self.y0)
        self.y1 = utila.roundme(self.y1)
        # ensure correct coordinate relation
        assert self.x0 <= self.x1, f'{self.x0} <= {self.x1}'
        assert self.y0 <= self.y1, f'{self.y0} <= {self.y1}'

    @classmethod
    def from_list(cls, data):
        """Create `BoundingBox` from list"""
        assert len(data) == 4, f'data has wrong length {len(data)}, require 4'
        return cls(x0=data[0], y0=data[1], x1=data[2], y1=data[3])

    @classmethod
    def from_str(cls, raw: str):
        """Create `BoundingBox` from raw data which contains 4 floats"""
        splitted = raw.split()
        length = len(splitted)
        assert length == 4, f'wrong split length {length} for "{raw}"'
        created = cls.from_list([float(item) for item in splitted])
        return created

    def copy(self):
        return BoundingBox(x0=self.x0, y0=self.y0, x1=self.x1, y1=self.y1)


BoundingBoxes = typing.List[BoundingBox]


def split_y(
    bounding: BoundingBox,
    part: int,
    parts: int,
) -> BoundingBox:
    """Split `bounding` in `parts`.

    Args:
        bounding: parent BoundingBox to split into `part`
        part: number of sub-bounding from top to bottom
        parts: number of chunks to split parent box
    Returns:
        sub-BoundingBox
    """
    assert parts >= 0, 'non positive parts'
    assert part < parts, f'part:{part} < parts:{parts}'

    step = (bounding.y1 - bounding.y0) / parts

    result = BoundingBox(
        bounding.x0,
        bounding.y0 + step * part,
        bounding.x1,
        bounding.y0 + step * (part + 1),
    )
    return result


def split_x(
    bounding: BoundingBox,
    part: int,
    parts: int,
) -> BoundingBox:
    """Split `bounding` in `parts`.

    Args:
        bounding: parent BoundingBox to split into `part`
        part: number of sub-bounding from top to bottom
        parts: number of chunks to split parent box
    Returns:
        sub-BoundingBox
    """
    assert parts >= 0, 'non positive parts'
    assert part < parts, f'part:{part} < parts:{parts}'

    step = (bounding.x1 - bounding.x0) / parts

    result = BoundingBox(
        bounding.x0 + step * part,
        bounding.y0,
        bounding.x0 + step * (part + 1),
        bounding.y1,
    )
    return result


Boundings = typing.List[typing.Tuple[int, BoundingBox]]


@dataclasses.dataclass
class PageBoundings:
    # list of `BoundingBox`es on current `page`
    boundings: Boundings = dataclasses.field(default_factory=list)
    # current page number
    page: int = 0

    def __getitem__(self, index):
        # page, content
        if index == 0:  # pylint:disable=C2001
            return self.page
        if index == 1:
            return self.boundings
        raise IndexError(f'invalid index: {index}')


PageBoundingsList = typing.List[PageBoundings]


def between(bounding, ymin, ymax):
    """\
    >>> between(BoundingBox(15, 15, 40, 40), 15, 40)
    True
    >>> between(BoundingBox(15, 15, 40, 40), 20, 40)
    False
    """
    top = ymin <= bounding.y0 <= ymax
    bottom = ymin <= bounding.y1 <= ymax
    return top and bottom
