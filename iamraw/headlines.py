# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import contextlib
import dataclasses
import typing

import utila

import iamraw
import iamraw.toc


@dataclasses.dataclass
class Headline:
    title: str
    level: int = dataclasses.field(default=0)
    raw: str = dataclasses.field(default=None)
    raw_level: str = dataclasses.field(default=None, compare=False)
    page: int = dataclasses.field(default=-1)
    container: int = dataclasses.field(default=None)

    @property
    def start(self):
        with contextlib.suppress(TypeError):
            return self.container[0]  # pylint:disable=E1136
        return self.container

    @property
    def end(self):
        with contextlib.suppress(TypeError):
            return self.container[1]  # pylint:disable=E1136
        return self.container


Headlines = typing.List[Headline]
PagesHeadlineList = typing.List[Headlines]


def headlines_totoc(
        headlines: PagesHeadlineList,
        remove_rawinfo: bool = False,
) -> 'iamraw.Toc':
    try:
        flat = utila.flatten(headlines)
    except TypeError:
        # list is already flat
        flat = headlines
    result = iamraw.toc.create_toc(flat, remove_rawinfo=remove_rawinfo)
    return result
