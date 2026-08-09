# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import collections
import dataclasses
import enum
import hashlib
import math

import iamraw


class ListType(enum.Enum):
    UNDEFINED = None
    AMBIGUOUS = '*1.+-'
    DOTTED = '*'
    NUMBERED = '123'
    NUMBERED_WITH_DOT = '1.5.9.'  # default style
    PLUSED = '+'
    MINUSED = '-'


ListItem = tuple[str, str]
ListItems = list[ListItem]


@iamraw.extracted
@dataclasses.dataclass
class PageList:
    data: ListItems = dataclasses.field(default_factory=list)
    area: list[int] = dataclasses.field(default_factory=list)
    """Numbers of elements to build a list element."""
    area_length: list[int] = dataclasses.field(default_factory=list)
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
        >>> hashed  = PageList().identifier
        >>> assert abs(hashed)  > 100000, hashed
        """
        raw = f'page:{self.pdfpage}area:{self.area}'
        result = freehash(raw)
        return result


# TODO: REMOVE LATER
def freehash(data: bytes, digits: int = 16) -> str:
    """Hash data to ease using.

    Hint: Use this for non secure approaches only.

    >>> freehash(b'this is data', digits=10)
    4923296541
    """
    if not isinstance(data, (bytes, str)):
        data = str(data)
    if isinstance(data, str):
        # convert to byte
        data: bytes = data.encode('utf8', errors='ignore')
    # hexdigits produces two chars for one digit?
    digits = math.ceil(digits / 2)
    hashed = hashlib.blake2b(data, digest_size=digits)
    result: str = hashed.hexdigest()
    result = result.replace('a', '1')
    result = result.replace('b', '2')
    result = result.replace('c', '3')
    result = result.replace('d', '4')
    result = result.replace('e', '5')
    result = result.replace('f', '6')
    result: int = int(result)
    return result


PageContentList = collections.namedtuple('PageContentList', 'page, content')
PageContentLists = list[PageContentList]
