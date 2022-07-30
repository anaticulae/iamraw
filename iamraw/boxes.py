# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import collections
import dataclasses
import typing

import iamraw.document

PageContentBoxes = collections.namedtuple(
    'PageContentBoxes',
    'content page',
)
PageContentHorizontals = collections.namedtuple(
    'PageContentHorizontals',
    'content page',
)

PagesWithBoxList = typing.List[PageContentBoxes]
PagesWithHorizontalList = typing.List[PageContentHorizontals]


@dataclasses.dataclass
class HorizontalLine(iamraw.document.Boxed):

    @property
    def width(self):
        width_ = abs(self.box.x1 - self.box.x0)
        height_ = abs(self.box.y1 - self.box.y0)
        if height_ > width_:
            # rotated page
            return height_
        # normal horizontal
        return width_

    def __str__(self):
        xleft = min([self.box.x0, self.box.x1])
        return 'HorizontalLine[xleft=%d, width=%d]' % (xleft, self.width)


@dataclasses.dataclass
class Box(iamraw.document.Boxed):
    """This Box can contains Text, Images etc."""

    def __str__(self):
        return 'Box(box=%s)' % str(self.box)
