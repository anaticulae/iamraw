# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import contextlib
import dataclasses
import enum

import utila

SUMMARY = -1

LOCATION_PATTERN = utila.compiles(r"""
(
     p(?P<page>-{0,1}\d+)                        # page can be negative
     ((?P<shortcut>[a-z]+)(?P<value>-{0,1}\d+))?
)
""")


@dataclasses.dataclass(unsafe_hash=True)
class Location:
    """The location defines the object on which the Finding belongs to.

    .. code-block :: none

        Examples for location:

        page                p10
        chapter             p10     c2
        section             p5      sec3
        paragraph           p10     pa5
        sentence            p10     s10
        word                p13     w100
        char                p4      cr137
        whitespace          p3      ws17
        image               p1      i1
        oneline             p13     ol5
    """
    page: int = -1
    shortcut: str = None
    value: int = None

    @classmethod
    def fromstr(cls, raw: str):
        if not raw:
            utila.error(f'invalid location: {raw}')
            return None
        matched = LOCATION_PATTERN.match(raw)
        if not matched:
            utila.error(f'invalid location: {raw}')
            return None
        page, shortcut, value = int(matched['page']), 'p', None
        with contextlib.suppress(TypeError):
            value = int(matched['value'])
            shortcut = matched['shortcut']
        result = cls(page=page, shortcut=shortcut, value=value)
        return result

    @classmethod
    def from_page(cls, page: int):
        """\
        >>> Location.from_page(10)
        Location(page=10, shortcut='p', value=None)
        >>> Location.from_page(-1)
        Location(page=-1, shortcut='p', value=None)
        >>> str(Location.from_page(-1))
        'p-1'
        >>> str(Location.from_sentence(page=0, sentence=0))
        'p0s0'
        """
        assert page >= SUMMARY, str(page)
        return cls.fromstr(f'p{page}')

    @classmethod
    def from_sentence(cls, sentence: int, page: int):
        assert page >= SUMMARY, str(page)
        assert sentence >= 0, str(sentence)
        return cls.fromstr(f'p{page}s{sentence}')

    @classmethod
    def from_chapter(cls, chapter: int, page: int):
        assert page >= SUMMARY, str(page)
        assert chapter >= 0, str(chapter)
        return cls.fromstr(f'p{page}c{chapter}')

    @classmethod
    def from_word(cls, word: int, page: int):
        """\
        >>> str(Location.from_word(10, 5))
        'p5w10'
        """
        assert page >= SUMMARY, str(page)
        assert word >= 0, str(word)
        return cls.fromstr(f'p{page}w{word}')

    @classmethod
    def from_oneline(cls, line: int, page: int):
        assert page >= SUMMARY, str(page)
        assert line >= 0, str(line)
        return cls.fromstr(f'p{page}ol{line}')

    def __str__(self) -> str:  # pylint:disable=no-self-use
        value = self.value if self.value is not None else ''
        if self.shortcut == 'p':
            return f'p{self.page}'
        return f'p{self.page}{self.shortcut}{value}'

    def raw(self):
        # TODO: REMOVE WITH NEXT MAJOR
        return str(self)


SUMMARY_LOCATION = Location.from_page(SUMMARY)

RANGEDLOCATION_PATTERN = utila.compiles(r"""
    (p(?P<page>\d+)(_(?P<page_end>\d+))?[~]?)?
    (l(?P<line>\d+)(_(?P<line_end>\d+))?[~]?)?
    (t(?P<token>\d+)(_(?P<token_end>\d+))?[~]?)?
    (c(?P<char>\d+)(_(?P<char_end>\d+))?)?
""")

RANGEDLOCATION_KEYS = [
    'page', 'page_end', 'line', 'line_end', 'token', 'token_end', 'char',
    'char_end'
]


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

    @classmethod
    def fromstr(cls, raw: str):
        matched = RANGEDLOCATION_PATTERN.match(raw)
        if not matched:
            return None
        result = RangedLocation()
        for item in RANGEDLOCATION_KEYS:
            with contextlib.suppress(TypeError):
                setattr(result, item, int(matched[item]))
        return result

    def __repr__(self):
        values = [
            f'{key}={getattr(self, key)}' for key in RANGEDLOCATION_KEYS
            if getattr(self, key) is not None
        ]
        values = ', '.join(values)
        return f'RangedLocation({values})'

    @property
    def shortcut(self):
        return 'r'

    def __str__(self) -> str:
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

    def raw(self):
        # TODO: REMOVE WITH NEXT MAJOR
        return str(self)


BOUNDINGLOCATION_PATTERN = utila.compiles(r"""
    p(?P<page>\d+)
    (l(?P<line>\d+))?
    (?P<shortcut>b)
    \((?P<tuple>((-?\d+\.\d+;{0,1}){4,}))\)
""")


@dataclasses.dataclass(unsafe_hash=True)
class BoundingLocation:
    """The BoundingLocation defines the area which the Finding belongs to.

    This rectangle can be highlighted in further presentation steps. The
    rectangle is the simplest highlighting method.

    >>> BoundingLocation.fromstr('p5b(137.0;145.0;123.0;232.0)')
    BoundingLocation(page=5, shortcut='b', value=(137.0, 145.0, 123.0, 232.0), line=None)
    >>> BoundingLocation.fromstr('p5l10b(137.0;-145.0;123.0;-232.0)')
    BoundingLocation(page=5, shortcut='b', value=(137.0, -145.0, 123.0, -232.0), line=10)
    """
    page: int = -1
    shortcut: str = None
    # use a multiple of 4 to render more than one rectangle
    value: tuple = None
    line: int = None

    @classmethod
    def fromstr(cls, raw: str):
        assert raw, 'require input'
        matched = BOUNDINGLOCATION_PATTERN.match(raw)
        if not matched:
            return None
        page, shortcut, value = int(matched['page']), 'b', None
        value = utila.parse_tuple(matched['tuple'], separator=';', length=None)
        shortcut = matched['shortcut']
        result = cls(page=page, shortcut=shortcut, value=value)
        with contextlib.suppress(KeyError, TypeError):
            result.line = int(matched['line'])
        return result

    @classmethod
    def fromtuple(cls, bounding: tuple, page: int, line: int = None):
        return cls(shortcut='b', page=page, value=bounding, line=line)

    def __str__(self) -> str:
        rounded = utila.roundme(self.value)
        joined = utila.from_tuple(rounded, separator=';')
        raw = f'p{self.page}'
        if self.line is not None:
            raw += f'l{self.line}'
        raw += f'b({joined})'
        return raw

    def raw(self):
        # TODO: REMOVE WITH NEXT MAJOR
        return str(self)


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

    def __post_init__(self):
        assert isinstance(self.number, int) or self.number is None


Findings = list[Finding]


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


PageFindings = list[PageFinding]


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
