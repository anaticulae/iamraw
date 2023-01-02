# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import dataclasses

import utila

import iamraw


@dataclasses.dataclass
class TableBounding:
    bounding: iamraw.BoundingBox = None
    lines: iamraw.BoundingBoxes = dataclasses.field(default_factory=list)
    page: int = None

    def append(self, item):
        self.lines.append(item)  # pylint:disable=E1101

    def __getitem__(self, index):
        return self.lines[index]  # pylint:disable=E1101,E1136

    def __len__(self):
        return len(self.lines)

    @property
    def identifier(self) -> int:
        """\
        >>> assert TableBounding((10.5, 10.5, 20.5, 200.51), page=5).identifier
        """
        return utila.pagebox_hash(page=self.page, box=self.bounding)


TableBoundings = list[TableBounding]


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


PageContentTableBoundings = list[PageContentTableBounding]
