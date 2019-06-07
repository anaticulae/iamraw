# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

from dataclasses import dataclass

from utila import INF


@dataclass
class BoundingBox:
    x_bottom: float = -INF
    y_bottom: float = -INF

    x_top: float = INF
    y_top: float = INF

    def __repr__(self):
        raw = ('BoundingBox(x_bottom=%.2f, y_bottom=%.2f, '
               'x_top=%.2f, y_top=%.2f)')
        return raw % (
            self.x_bottom,
            self.y_bottom,
            self.x_top,
            self.y_top,
        )

    def raw(self):
        return '%.2f %.2f %.2f %.2f' % (
            self.x_bottom,
            self.y_bottom,
            self.x_top,
            self.y_top,
        )

    def __getitem__(self, index):
        if index == 0:
            return self.x_bottom
        if index == 1:
            return self.y_bottom
        if index == 2:
            return self.x_top
        if index == 3:
            return self.y_top
        raise IndexError('Index to hight %d > 3' % index)

    @classmethod
    def from_list(cls, data):
        """Create Box from list"""
        assert len(data) == 4, 'data has wrong length %d, require 4' % len(data)
        return cls(
            x_bottom=data[0],
            y_bottom=data[1],
            x_top=data[2],
            y_top=data[3],
        )

    @classmethod
    def from_str(cls, raw: str):
        """Create BoundingBox from raw data which contains 4 floats"""
        length = len(raw.split())
        assert length == 4, 'wrong split length %d for "%s"' % (length, raw)
        return cls.from_list([float(item) for item in raw.split()])


@dataclass
class Boxed:
    """Object with outlines like a rectangle"""
    box: BoundingBox = None


@dataclass
class PageObject:
    """Object to store every unsupported type"""
    box: BoundingBox = None
    content: str = None
