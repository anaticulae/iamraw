# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import collections
import enum
import typing

PageContentContentType = collections.namedtuple(
    'PageContentContentType',
    'page, content',
)

PageContentContentTypes = typing.List[PageContentContentType]


class PageContentType(enum.Enum):
    BLOCKQUOTE = enum.auto()
    LIST = enum.auto()
    TEXT = enum.auto()
    FORMULA = enum.auto()
    CAPTION = enum.auto()
    TABLE = enum.auto()
    FIGURE = enum.auto()
    BOXED = enum.auto()
    UNDEFINED = -1
