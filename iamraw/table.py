# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import dataclasses
import typing

import iamraw


@dataclasses.dataclass
class TableBounding:
    bounding: iamraw.BoundingBox = None
    lines: iamraw.BoundingBoxes = dataclasses.field(default_factory=list)

    def append(self, item):
        self.lines.append(item)  # pylint:disable=E1101

    def __getitem__(self, index):
        return self.lines[index]  # pylint:disable=E1101,E1136

    def __len__(self):
        return len(self.lines)


TableBoundings = typing.List[TableBounding]


@dataclasses.dataclass
class PageContentTableBounding:
    page: int = None
    content: TableBoundings = dataclasses.field(default_factory=list)

    def append(self, item):
        self.content.append(item)  # pylint:disable=E1101

    def __getitem__(self, index):
        return self.content[index]  # pylint:disable=E1101,E1136

    def __len__(self):
        return len(self.content)


PageContentTableBoundings = typing.List[PageContentTableBounding]
