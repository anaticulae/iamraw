# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import dataclasses
import enum

import configo
import utilo

import iamraw


@dataclasses.dataclass
class CharStyle:
    start: int
    end: int
    size: float = None
    rise: float = None
    font: int = None
    underline: bool = False

    def copy(self):
        return CharStyle(
            start=self.start,
            end=self.end,
            font=self.font,
            rise=self.rise,
            size=self.size,
            underline=self.underline,
        )

    @property
    def width(self):
        """Number of chars which hold this style."""
        return self.end - self.start

    @property
    def char_count(self):
        """Number of chars which hold this style."""
        return self.width


CharStyles = list[CharStyle]


@dataclasses.dataclass
class HighNote:
    start: int
    end: int
    value: int


HighNotes = list[HighNote]


@dataclasses.dataclass
class TextStyle:
    content: CharStyles = dataclasses.field(default_factory=list)
    rotation: float = 0.0

    def __post_init__(self):
        if not self.content:
            return
        last = self.content[0]  # pylint:disable=E1136
        for current in self.content[1:]:  # pylint:disable=E1136
            assert current.start < current.end, current
            assert current.start == last.end, f'{current.start} == {last.end}'
            last = current

    def __iter__(self):
        for style in self.content:  # pylint:disable=E1133
            yield style

    def __len__(self):
        return len(self.content)

    def textsize(self) -> float:
        return TextStyle.textsizes(self)

    @property
    def underlined(self) -> bool:
        return TextStyle.underlines(self)

    @property
    def fontid(self) -> int:
        return TextStyle.fontids(self)

    @classmethod
    def fontids(cls, item: 'TextStyle', method=utilo.mode):
        result = [[char.font] * char.char_count for char in item.content]
        result = utilo.flat(result)
        return method(result)

    @classmethod
    def textsizes(cls, item: 'TextStyle', method=utilo.mode):
        # detect most common font size(s)
        assert isinstance(item, cls), type(item)
        result = [[char.size] * char.char_count for char in item.content]
        result = utilo.flat(result)
        return method(result)

    @classmethod
    def underlines(cls, item: 'TextStyle', method=utilo.mode):
        assert isinstance(item, cls), type(item)
        result = [[1 if char.underline else 0] * char.char_count
                  for char in item.content]
        result = utilo.flat(result)
        return method(result)

    @classmethod
    def create(cls, start, end, size, rise=0, underline=False):
        return cls(content=[
            CharStyle(
                start=start,
                end=end,
                size=size,
                rise=rise,
                underline=underline,
            )
        ])

    def copy(self):
        return TextStyle(content=[item.copy() for item in self.content])  # pylint:disable=E1133


class TextLineStyle(enum.IntEnum):
    NONE = 0
    UNDERLINED = 1
    CROSSED = 2
    OVERLINED = 3


class TextState(enum.IntFlag):
    """\
    >>> int(TextState.FORMULA)
    32
    >>> int(TextState.FORMULA | TextState.CAPTION)
    34
    """
    HIDDEN = 0
    VISIBLE = 1
    CAPTION = 2
    CODE = 4
    IMAGE = 8
    FIGURE = 16
    FORMULA = 32
    PAGENUMBER = 64
    FOOTNOTE = 128
    HEADNOTE = 256
    TABLE = 512
    ALL = 1048575  # 1111...

    @property
    def visible(self) -> bool:
        """\
        >>> TextState.CAPTION.visible
        False
        >>> TextState.VISIBLE.visible
        True
        >>> TextState.HIDDEN.visible
        False
        >>> (TextState.CAPTION | TextState.VISIBLE).visible
        True
        >>> TextState.ALL.visible
        True
        """
        return bool(self.value % 2)


@utilo.cacheme
def skip(expected, current) -> bool:
    """\
    >>> from texmex import TextState
    >>> skip(TextState.VISIBLE, TextState.VISIBLE)
    False
    >>> skip(TextState.VISIBLE, TextState.HIDDEN)
    True
    >>> skip(TextState.ALL, TextState.HIDDEN)
    True
    >>> skip(TextState.ALL, TextState.TABLE)
    False
    >>> skip(TextState.ALL, TextState.CODE | TextState.IMAGE)
    False
    >>> skip(TextState.IMAGE, TextState.ALL)
    True
    """
    if expected is None:
        return False
    if current is None:
        return False
    if expected == current:
        return False
    if current in expected:
        if current & expected:
            # current is a teilmenge of expected
            return False
        return True
    return True


@dataclasses.dataclass
class TextInfo:
    """\
    Ensure that hashing is possible:
    >>> hash(TextInfo('This is content', style=TextStyle())) is not None
    True
    """
    text: str
    bounding: iamraw.BoundingBox = None
    style: TextStyle = None
    bounding_mean: float = None
    line: int = 0
    state: TextState = TextState.VISIBLE

    def copy(self):
        result = TextInfo(
            bounding=self.bounding.copy() if self.bounding else None,
            bounding_mean=self.bounding_mean,
            style=self.style.copy() if self.style else None,
            text=self.text,
            line=self.line,
        )
        return result

    def hide(self):
        self.state = TextState.HIDDEN

    def state_change(self, new):
        self.state = new

    @property
    def visible(self):
        return self.state >= TextState.VISIBLE

    def __repr__(self):
        return self.text + utilo.NEWLINE

    def __hash__(self):
        result = (hash(self.text) + hash(str(self.style)) +
                  hash(str(self.bounding)) + hash(self.line))
        return result


def splitby_count(item: TextInfo, counts: tuple) -> list:
    width = sum(counts)
    if not width:
        return []
    bounding_old = item.bounding
    step = (bounding_old[2] - bounding_old[0]) / width
    start = 0
    result = []
    for count in counts:
        text = item.text[start:start + count]
        x0 = bounding_old[0] + start * step
        bounding = utilo.roundme(
            x0,
            bounding_old[1],
            x0 + step * len(text),
            bounding_old[3],
        )
        new = TextInfo(
            text=text,
            bounding=bounding,
            bounding_mean=item.bounding_mean,
            # TODO: ADD ROTATION LATER
            style=TextStyle(content=substyle(
                item.style,
                start=start,
                end=start + count,
            )),
            line=item.line,
        )
        result.append(new)
        start += count
    return result


def substyle(styles: CharStyles, start, end) -> list:
    result = []
    for style in styles:
        # TODO: REWORK THIS DRAF LATER
        if start <= style.start <= end or start <= style.end <= end:
            result.append(style)
    return result


def create_textstyle(chars: iamraw.Chars) -> TextStyle:
    assert chars
    start = 0
    size, rise, font = chars[0].size, chars[0].rise, chars[0].font
    underline = chars[0].underline
    result = []
    for index, char in enumerate(chars[1:], start=1):
        if char.size != size or char.rise != rise or char.font != font or char.underline != underline:
            style = CharStyle(
                start=start,
                end=index,
                size=size,
                rise=rise,
                underline=underline,
                font=font,
            )
            result.append(style)
            start, size, rise, font = index, char.size, char.rise, char.font
            underline = char.underline
    if start != len(chars):
        style = CharStyle(
            start=start,
            end=len(chars),
            size=size,
            rise=rise,
            underline=underline,
            font=font,
        )
        result.append(style)
    return TextStyle(content=result)


HIGHNOTE_RISE_MIN = configo.HV_FLOAT_PLUS(default=5.0)


def highnotes(
    info: TextInfo,
    highnote_rise_min: float = HIGHNOTE_RISE_MIN,
) -> HighNotes:
    """Extract `HighNote`s out of text line. A highnote is a number
    which is a reference to an item defined in the footer.

    A HighNote is a number which has a text rise higher than
    `HIGHNOTE_RISE_MIN`.

    Args:
        info(TextInfo): text line which can contain HightNote's
        highnote_rise_min(float): required rise to be acceped as highnote
    Returns:
        list of parsed `HighNote`s
    """
    text = info.text
    result = []
    for style in info.style:
        if style.rise <= highnote_rise_min:
            continue
        value = text[style.start:style.end]
        try:
            value = int(value)
        except ValueError:
            continue
        note = HighNote(
            start=style.start,
            end=style.end,
            value=value,
        )
        result.append(note)
    return result


def remove_highnotes(info: TextInfo, magic: bool = False) -> str:
    """Replace hight notes with empty character. Therefore the text
    width is shrinked.

    Args:
        info(TextInfo): text data with rise information
        magic(bool): if True replace note due pattern
    Returns:
        text without any hightnotes
    Example:
        magic:True "Internetnutzer^1 waren" => "Internetnutzer{{hn:1:nh}} waren"
    """
    notes = highnotes(info)
    result = []
    current = 0
    for item in notes:
        if not magic:
            text = info.text[current:item.start]
        else:
            highnote = '{{hn:%d:nh}}' % item.value
            text = info.text[current:item.start] + highnote
        result.append(text)
        current = item.end
    if current != len(info.text):
        # append content after highnote
        result.append(info.text[current:])
    return ''.join(result)


def style_without_highnotes(
    info: TextInfo,
    merge: bool = False,
) -> TextStyle:
    notes = highnotes(info)
    tuplenotes = {(note.start, note.end) for note in notes}
    result = []
    for item in info.style:
        if (item.start, item.end) in tuplenotes:
            continue
        result.append(item.copy())
    last = 0
    for item in result:
        diff = item.start - last
        item.start = item.start - diff
        item.end = item.end - diff
        last = item.end
    # last
    if merge and result:
        merged = [result[0]]
        for item in result[1:]:
            if merged[-1].size == item.size and merged[-1].rise == item.rise:
                merged[-1].end = item.end
            else:
                merged.append(item)
        result = merged
    return TextStyle(content=result)


@dataclasses.dataclass
class PageContentTextItems:
    page: int
    content: list = dataclasses.field(default_factory=list)
