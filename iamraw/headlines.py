# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2022 by Helmut Konrad Fahrendholz. All rights reserved.
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


@dataclasses.dataclass(unsafe_hash=True)
class Headline:
    title: str
    level: int = dataclasses.field(default=0)
    raw: str = dataclasses.field(default=None)
    raw_level: str = dataclasses.field(default=None, compare=False)
    page: int = dataclasses.field(default=-1)
    container: int = dataclasses.field(default=None)
    decoration: int = dataclasses.field(default=None)

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
    level_default: int = 1,
) -> 'iamraw.Toc':
    """Convert headlines to toc-structure. Use level_default=None to
    skip setting default level.

    Hint: Converting to toc requires a None-Level for every item.
    """
    try:
        flat = utila.flatten(headlines)
    except TypeError:
        # list is already flat
        flat = headlines
    # disable default level by setting None
    if level_default is not None:
        for item in flat:
            # set default level if level is None
            if item.level is None:
                item.level = level_default
    for item in flat:
        assert item.level is not None, str(item)
    result = iamraw.toc.create_toc(flat, remove_rawinfo=remove_rawinfo)
    return result
