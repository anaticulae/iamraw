# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import contextlib
import dataclasses
import enum
import re
import typing

import utila

SUMMARY = -1


@dataclasses.dataclass(unsafe_hash=True)
class Location:
    """The location defines the object on which the Finding belongs to.

    .. code-block :: none

        Examples for location:

        page                p10
        chapter             c2     p10
        section             sec3   p5
        paragraph           pa5    p10
        sentence            s10    p10
        word                w100   p13
        char                cr137  p4
        whitespace          ws17   p3
        image               i1     p1
        oneline             ol5    p13
    """
    page: int = -1
    shortcut: str = None
    value: int = None

    def raw(self) -> str:  # pylint:disable=no-self-use
        value = self.value if self.value else ''
        if self.shortcut == 'p':
            return f'p{self.page}'
        return f'{self.shortcut}{value}p{self.page}'

    PATTERN = re.compile(r'((?P<shortcut>[a-z]+)(?P<value>\d+))?p(?P<page>\d+)')

    @classmethod
    def fromstr(cls, raw: str):
        if not raw:
            return None
        matched = re.match(Location.PATTERN, raw)
        if not matched:
            return None

        page, shortcut, value = int(matched['page']), 'p', None
        with contextlib.suppress(TypeError):
            value = int(matched['value'])
            shortcut = matched['shortcut']

        result = cls(page=page, shortcut=shortcut, value=value)
        return result

    @classmethod
    def from_page(cls, page: int):
        assert page >= SUMMARY, str(page)
        return cls.fromstr(f'p{page}')

    @classmethod
    def from_sentence(cls, sentence: int, page: int):
        assert page >= SUMMARY, str(page)
        assert sentence >= 0, str(sentence)
        return cls.fromstr(f's{sentence}p{page}')

    @classmethod
    def from_chapter(cls, chapter: int, page: int):
        assert page >= SUMMARY, str(page)
        assert chapter >= 0, str(chapter)
        return cls.fromstr(f'c{chapter}p{page}')

    @classmethod
    def from_oneline(cls, line: int, page: int):
        assert page >= SUMMARY, str(page)
        assert line >= 0, str(line)
        return cls.fromstr(f'ol{line}p{page}')


SUMMARY_LOCATION = Location.from_page(SUMMARY)


@dataclasses.dataclass(unsafe_hash=True)
class RangedLocation:
    """RangedLocation defines a mark which can include more than one
    page, line and token definition.

    >>> RangedLocation.fromstr('p10_12~l6_9~t5_19')
    RangedLocation(page=10, page_end=12, line=6, line_end=9, token=5, token_end=19)
    >>> RangedLocation.fromstr('p10_12~l6~t5')
    RangedLocation(page=10, page_end=12, line=6, token=5)
    >>> RangedLocation.fromstr('p10~l6')
    RangedLocation(page=10, line=6)
    >>> RangedLocation.fromstr('p5')
    RangedLocation(page=5)
    >>> RangedLocation.fromstr('p5~t17')
    RangedLocation(page=5, token=17)
    >>> RangedLocation.fromstr('c5_10')
    RangedLocation(char=5, char_end=10)
    """

    page: int = None
    page_end: int = None
    line: int = None
    line_end: int = None
    token: int = None
    token_end: int = None
    char: int = None
    char_end: int = None

    PATTERN = re.compile(r'(p(?P<page>\d+)(_(?P<page_end>\d+))?[~]?)?'
                         r'(l(?P<line>\d+)(_(?P<line_end>\d+))?[~]?)?'
                         r'(t(?P<token>\d+)(_(?P<token_end>\d+))?[~]?)?'
                         r'(c(?P<char>\d+)(_(?P<char_end>\d+))?)?')

    KEYS = [
        'page', 'page_end', 'line', 'line_end', 'token', 'token_end', 'char',
        'char_end'
    ]

    @classmethod
    def fromstr(cls, raw: str):
        matched = re.match(RangedLocation.PATTERN, raw)
        if not matched:
            return None
        result = RangedLocation()
        for item in RangedLocation.KEYS:
            with contextlib.suppress(TypeError):
                setattr(result, item, int(matched[item]))
        return result

    def raw(self) -> str:
        result = f'p{self.page}'
        if self.page_end is not None:
            result += f'_{self.page_end}'
        if self.line is not None:
            result += f'~l{self.line}'
        if self.line_end is not None:
            result += f'_{self.line_end}'
        if self.token is not None:
            result += f'~t{self.token}'
        if self.token_end is not None:
            result += f'_{self.token_end}'
        if self.char is not None:
            result += f'~c{self.char}'
        if self.char_end is not None:
            result += f'_{self.char_end}'
        return result

    def __repr__(self):
        values = [
            f'{key}={getattr(self, key)}' for key in RangedLocation.KEYS
            if getattr(self, key) is not None
        ]
        values = ', '.join(values)
        return f'RangedLocation({values})'

    @property
    def shortcut(self):
        return 'r'


@dataclasses.dataclass(unsafe_hash=True)
class BoundingLocation:
    """The location defines the object on which the Finding belongs to.
    Defines rectangle which can be highlighted in further presentation
    steps. The rectangle is the simplest highlighting method.

    .. code-block :: none

        Examples for location:

        bounding    b(137.0;145.0;123.0;232.0)p5
    """
    page: int = -1
    shortcut: str = None
    value: tuple = None

    PATTERN = r'(?P<shortcut>b)\((?P<tuple>((\d+\.\d+;{0,1}){4}))\)p(?P<page>\d+)'

    def __str__(self) -> str:
        joined = ';'.join([str(item) for item in self.value])  # pylint:disable=E1133
        raw = f'b({joined})p{self.page}'
        return raw

    @classmethod
    def fromstr(cls, raw: str):
        assert raw, 'require input'
        matched = re.match(BoundingLocation.PATTERN, raw)
        if not matched:
            return None

        page, shortcut, value = int(matched['page']), 'b', None
        value = matched['tuple'].split(';')
        value = utila.roundme([float(item) for item in value])
        value = tuple(value)
        shortcut = matched['shortcut']
        result = cls(page=page, shortcut=shortcut, value=value)
        return result

    @classmethod
    def fromtuple(cls, bounding: tuple, page: int):
        return cls(shortcut='b', page=page, value=bounding)


class FindingLevel(enum.Enum):
    """Define how important an `Finding` is.

    Color:
        green(1)
        yellow(2, 3, 6)
        red(8, 10)
    """
    # MESSAGE = 0 ???
    # advice to use other pattern or style
    ADVICE = 1
    # page order
    CONVENTION = 2
    # style of paragraph, page
    REFACTOR = 3
    # umgangssprache, image black and white problem
    WARNING = 6
    # writing over border
    ERROR = 8
    # pdf analyzing error
    FATAL = 10
    UNDEFINED = -1


@dataclasses.dataclass(unsafe_hash=True)
class Finding:  # pylint:disable=R0903
    """Non active findings are not presentend to the user cause of lag
    of quality. There purpose is to improve the platform. A second point
    for non presenting is a to low confidence of the result."""

    number: int = dataclasses.field(compare=False, hash=False, default=-1)
    location: Location = None
    # how important a level is
    level: FindingLevel = None
    msgid: str = None
    solution: 'iamraw.Solution' = None
    confidence: float = None
    active: bool = False


Findings = typing.List[Finding]


@dataclasses.dataclass
class PageFinding:
    page: int = None
    content: Findings = dataclasses.field(default_factory=list)

    def __len__(self):
        return len(self.content)

    def __getitem__(self, index):
        return self.content[index]  # pylint:disable=E1136

    def append(self, item):
        self.content.append(item)  # pylint:disable=E1101


PageFindings = typing.List[PageFinding]


def select_findings(findings: Findings, msgid: set = None) -> Findings:
    """Select `Findings` specified by `msgid`

    >>> select_findings([Finding(msgid=1337), Finding(msgid=1338)], msgid=(1337,1400))
    [Finding(...msgid=1337...)]
    >>> select_findings([Finding(msgid=1337), Finding(msgid=1338)])
    [Finding(...msgid=1337...), Finding(...msgid=1338...)]
    """
    assert all(isinstance(item, Finding) for item in findings)
    if msgid is None:
        return findings
    if isinstance(msgid, int):
        msgid = {msgid}
    elif isinstance(msgid, list):
        msgid = set(msgid)
    return [item for item in findings if item.msgid in msgid]
