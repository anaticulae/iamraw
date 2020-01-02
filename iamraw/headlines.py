# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import dataclasses
import typing


@dataclasses.dataclass
class Headline:
    text: str
    level: int = dataclasses.field(default=0)
    rawlevel: str = dataclasses.field(default=None, compare=False)
    page: int = dataclasses.field(default=-1)
    container: int = dataclasses.field(default=None)

    @property
    def start(self):
        try:
            return self.container[0]  # pylint:disable=E1136
        except TypeError:
            return self.container

    @property
    def end(self):
        try:
            return self.container[1]  # pylint:disable=E1136
        except TypeError:
            return self.container


Headlines = typing.List[Headline]
PagesHeadlineList = typing.List[Headlines]
