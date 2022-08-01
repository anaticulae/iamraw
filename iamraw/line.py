# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import dataclasses
import typing


@dataclasses.dataclass
class PageContentLine:
    page: int
    content: list
    rotated: bool = False

    def __getitem__(self, index):
        """\
        >>> page, content = PageContentLine(5, ['EMPTY']); page, content
        (5, ['EMPTY'])
        """
        if index == 0:  # pylint:disable=compare-to-zero
            return self.page
        if index == 1:
            return self.content
        raise StopIteration


PageContentLines = typing.List[PageContentLine]
