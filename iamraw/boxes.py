# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

from collections import namedtuple
from dataclasses import dataclass
from typing import List

from iamraw.document import Boxed

PageContentBoxes = namedtuple('PageContentBoxes', 'content page')
PageContentHorizontals = namedtuple('PageContentHorizontals', 'content page')

PagesWithBoxList = List[PageContentBoxes]
PagesWithHorizontalList = List[PageContentHorizontals]


@dataclass
class HorizontalLine(Boxed):

    @property
    def width(self):
        return abs(self.box.x1 - self.box.x0)

    def __str__(self):
        xleft = min([self.box.x0, self.box.x1])
        return 'HorizontalLine[xleft=%d, width=%d]' % (xleft, self.width)


@dataclass
class Box(Boxed):
    """This Box can contains Text, Images etc."""

    def __str__(self):
        return 'Box(box=%s)' % str(self.box)
