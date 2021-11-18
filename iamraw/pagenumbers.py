# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import dataclasses
import enum


class PageNumberOrientation(enum.Enum):
    LEFT = enum.auto()
    NORMAL = enum.auto()
    RIGHT = enum.auto()


@dataclasses.dataclass
class PageNumber:
    pdfpage: int = None
    bounding: tuple = dataclasses.field(default=None, compare=False, hash=False)
    detected: str = None
    direction: PageNumberOrientation = PageNumberOrientation.NORMAL

    def __getitem__(self, index):
        # TUPLE UNPACKING
        if index == 0:  # pylint:disable=compare-to-zero
            return self.pdfpage
        if index == 1:
            return self.bounding
        if index == 2:
            return self.detected
        raise IndexError

    def __lt__(self, item):
        """\
        >>> sorted([PageNumber(pdfpage=5), PageNumber(pdfpage=3)])
        [...pdfpage=3,...pdfpage=5,...]
        """
        return self.pdfpage < item.pdfpage
