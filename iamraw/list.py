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
import enum
import typing

import iamraw


class ListType(enum.Enum):
    UNDEFINED = None
    AMBIGUOUS = '*1.+-'
    DOTTED = '*'
    NUMBERED = '123'
    NUMBERED_WITH_DOT = '1.5.9.'  # default style
    PLUSED = '+'
    MINUSED = '-'


ListItem = typing.Tuple[str, str]
ListItems = typing.List[ListItem]


@iamraw.extracted
@dataclasses.dataclass
class PageList:
    data: ListItems = dataclasses.field(default_factory=list)
    area: typing.List[int] = dataclasses.field(default_factory=list)
    """Numbers of elements to build a list element."""
    area_length: typing.List[int] = dataclasses.field(default_factory=list)
    pdfpage: int = None

    def append(self, title: str, level: str = None):
        self.data.append((level, title))  # pylint:disable=E1101

    def __getitem__(self, index) -> ListItem:
        return self.data[index]  # pylint:disable=E1136

    def __len__(self):
        return len(self.data)

    def ltype(self):  # pylint:disable=R0201
        return ListType.UNDEFINED

    @property
    def identifier(self) -> int:
        """\
        Ensure to generate valid hash int value
        >>> assert PageList().identifier > 100000
        """
        raw = f'page:{self.pdfpage}area:{self.area}'
        result = hash(raw)
        return result


PageContentList = collections.namedtuple('PageContentList', 'page, content')
PageContentLists = typing.List[PageContentList]
