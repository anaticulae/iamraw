# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import copy
import dataclasses
import enum
import typing

import utila

import iamraw
import texmex
import texmex.style
import texmex.text
import texmex.utils

START = 0.0
END = 1.0

DISABLE_VALIDATION = END * 2


class SelectBounding(enum.Enum):
    MAX = enum.auto()
    TOP = enum.auto()
    BOTTOM = enum.auto()
    MEAN = enum.auto()
    TWO_THIRDS = enum.auto()


@dataclasses.dataclass
class NavigatorMixin:
    """\
    Args:
        page(int): page number of Navigator-instance
        pagesize(tuple): maximal width/height of Navigator
    Sizes:
        A4: 210 x 297 mm, 8.26 x 11.69 inch, 595 x 842pt
                                             612 x 792pt
    """
    page: int = -1
    pagesize: tuple = (612.0, 792.0)

    def between(
        self,
        top: float,
        bottom: float,
        left: float = START,
        right: float = END,
        selector: SelectBounding = SelectBounding.MAX,
    ) -> list:
        """Return content between top and bottom and left to right in
        range [top(0.0), bottom(1.0)] and [left(0.0), right(1.0)].

        Args:
            top(float): accepted content after top mark
            bottom(float): accepted content before bottom mark
            left(float): accepted content after left mark
            right(float): accepted content before right mark
            selector: select different bounding checker
        Returns:
            list of `TextInfo`
        """
        assert START <= top <= bottom <= END, f'{START}<={top}<={bottom}<={END}'
        assert START <= left <= right <= DISABLE_VALIDATION, f'{START}<={left}<={right}<={DISABLE_VALIDATION}'
        if not self.data:
            # empty page
            return []
        # valid rectangle with possible content
        before = top * self.pagesize[1]
        after = bottom * self.pagesize[1]
        beforeleft = left * self.pagesize[0]
        afterright = right * self.pagesize[0]
        inside = (before, after, beforeleft, afterright)
        # collect valid content
        result = []
        for item in self.data:
            if not valid(item, inside, selector=selector):
                continue
            result.append(item.copy())
        return result

    def before(
        self,
        height: float,
        width: float = END,
        selector: SelectBounding = SelectBounding.MAX,
    ) -> list:
        """Determine elements on the top of the document

        Args:
            height(float[0.0,1.0]): 0.0 is top, 1.0 is bottom
            width: marker from left to right, return elements [0.0 width]
            selector: select bounding check strategy
        Returns:
            list of `TextInfo`
        """
        result = self.between(
            START,
            height,
            left=START,
            right=width,
            selector=selector,
        )
        return result

    def after(
        self,
        height,
        width=START,
        selector: SelectBounding = SelectBounding.MAX,
    ):
        """Determine elements after `height` till the bottom of the
        page. Additonal shrink from left to right with `width`."""
        result = self.between(height, END, width, END, selector=selector)
        return result

    @property
    def debug(self):
        return utila.NEWLINE.join((line.text.strip() for line in self))

    def print_debug(self):
        utila.log(f'page: {self.page} size: {self.pagesize}')
        utila.log(self.debug)

    def hull_empty(self):
        raise NotImplementedError  # pragma: no cover

    @property
    def rotated(self):
        return self.pagesize[0] > self.pagesize[1]


@dataclasses.dataclass
class PTN(NavigatorMixin):
    """The PTN eases to navigate through the textual content of a Page.

    The text is processed from top to down and left to right.

    To fill navigator with content use `insert`. Acessing the data is
    possible trough `between`, `before`, `after` or __getitem__.

    Make Navigator compareable.

    >>> assert PTN() == PTN()
    >>> assert PTN(page=10) != PTN()
    >>> PTN().rotated
    False
    """
    data: typing.List = dataclasses.field(default_factory=list)
    # access textual element by BoundingBox
    fast: typing.Dict = dataclasses.field(default_factory=dict)

    def insert(
        self,
        text: str,
        style: texmex.style.TextStyle,
        bounding: iamraw.BoundingBox,
        bounding_mean: float = None,
        line: int = 0,
        state: 'TextState' = None,
        sort: callable = True,
    ):
        """Insert text element top to bottom and left to right.

        Args:
            text(str): content of text chunk
            style: style for every character of `text`
            bounding(iamraw.BoundingBox): position and dimension of text area
            bounding_mean: average distance from bottom line to char top
            line(int): position in parsed container
            state(TextState): add type information to text token
            sort(strategy): if True, insert bounding dependent
        """
        state = texmex.TextState.VISIBLE if state is None else state
        utila.asserts(text, str)
        self.assert_bounding(bounding)
        datum = texmex.style.TextInfo(
            bounding=bounding,
            bounding_mean=bounding_mean,
            style=style,
            text=text,
            line=line,
            state=state,
        )
        if sort:
            if isinstance(sort, bool):
                # use default inserting position
                sort = insert_position
            position = sort(bounding=bounding, data=self.data)
            self.data.insert(position, datum)
        else:
            self.data.append(datum)
        if hasattr(self, 'fast'):
            self.fast[bounding] = datum

    def __getitem__(self, index) -> texmex.style.TextInfo:
        return self.data[index]

    def __len__(self) -> int:
        """Count text chunks"""
        return len(self.data)

    def __iter__(self):
        return iter(self.data)

    def clear(self):
        self.data.clear()
        self.fast.clear()

    @property
    def dimension(self):
        return iamraw.PageSize(*self.pagesize)

    @property
    def width(self):
        return self.pagesize[0]

    @property
    def height(self):
        return self.pagesize[1]

    def offset(self, top: float, bottom: float) -> typing.Tuple[int, int]:
        """Determine the range of content index which represents the
        dataindex's of [top, bottom]."""
        assert START <= top <= bottom <= END
        after = bottom * self.height
        before = top * self.height  # greater than
        result = []
        for index, item in enumerate(self.data):
            # before and after are pixel coordinates
            if before <= item.bounding.y0 <= item.bounding.y1 <= after:
                result.append(index)
        if not result:
            return None, None
        top, bottom = result[0], result[-1] + 1
        return top, bottom

    def find(self, location: iamraw.BoundingBox):
        assert isinstance(location, iamraw.BoundingBox), type(location)
        try:
            return self.fast[location]
        except KeyError as error:
            raise ValueError(f'could not find {location}') from error

    def remove(self, line):
        """Remove `line` out of navigator."""
        bounding = line.bounding
        self.data.remove(line)
        del self.fast[bounding]

    def assert_bounding(self, bounding):
        x0, y0, x1, y1 = bounding
        assert x0 <= x1, f'{x0}<={x1}; {bounding}'
        assert y0 <= y1, f'{y0}<={y1}; {bounding}'
        # TODO: Substract border to move starting text to (0,0)?. If not,
        # x1 is sometimes higher than self.width.
        if (x1 - x0) > self.width:
            utila.error(f'page: {self.page} width: {x1-x0} < {self.width}')
        # assert (x1 - x0) < self.width, f'{x1-x0} < {self.width}'
        if (y1 - y0) > self.height:
            utila.error(f'page: {self.page} height: {y1-y0} < {self.height}')
        # assert (y1 - y0) < self.height, f'{y1-y0} < {self.height}'

    def hull_empty(self):
        """\
        >>> PTN(page=10).hull_empty()
        PTN(page=10, pagesize=(612.0, 792.0), data=[], fast={})
        """
        result = copy.deepcopy(self)
        result.clear()
        return result


@dataclasses.dataclass
class PTCN(NavigatorMixin):
    """Iterate over page content without footer and header.

    See: :class:`hey.textnavigator.navigator.PTN`.
    """

    def __init__(
        self,
        textnavigator: PTN,
        content: iamraw.Border,
        *,
        validate_leftright: bool = True,
    ):
        """Navigate throw text content, ignore footer and header

        Args:
            textnavigator: `textnavigator` with items are located
                           outside of `content`.
            content: distance from page border which defines start of content.
            validate_leftright(bool): do not check left right coordinate.
        """
        super().__init__(pagesize=(textnavigator.width, textnavigator.height))
        msg = 'require `PTN` got: %s' % type(textnavigator)
        assert isinstance(textnavigator, PTN), msg
        msg = 'require `Border` got: %s' % type(content)
        assert isinstance(content, iamraw.Border), msg
        assert content.bottom >= 100, str(content)  # ensure that are pixel
        self.content = content
        pagesize = iamraw.PageSize(
            width=textnavigator.width,
            height=textnavigator.height,
        )
        top, bottom = texmex.utils.topbottom(pagesize, content)
        assert 0 <= top <= bottom <= 1.0, f'0 <= {top} <= {bottom} <= 1.0'
        self.page = textnavigator.page
        # disable validation if required
        right = END if validate_leftright else DISABLE_VALIDATION
        # fill content navigator
        self.data = textnavigator.between(top, bottom, right=right)
        self._offset = textnavigator.offset(top, bottom)

    @property
    def offset(self):
        return self._offset

    @property
    def width(self):
        # TODO: adjust dimension to content border
        return self.content.right

    @property
    def height(self):
        # TODO: adjust dimension to content border
        return self.content.bottom - self.content.top

    def clear(self):
        self.data.clear()
        self._offset = None, None

    def __getitem__(self, index):
        return self.data[index]

    def __len__(self):
        return len(self.data)

    def hull_empty(self):
        """\
        >>> PTCN(PTN(page=10), iamraw.Border(20, 500, 20, 700)).hull_empty()
        PTCN(page=10, pagesize=(612.0, 792.0))
        """
        result = copy.deepcopy(self)
        result.clear()
        return result

    assert_bounding = PTN.assert_bounding
    insert = PTN.insert


def rotate_left(navigator):

    def rotate_bounding(bounding: tuple, width: float) -> iamraw.BoundingBox:
        x0, y0, x1, y1 = bounding
        box = (
            y0,
            width - x1,
            y1,
            width - x0,
        )
        result = iamraw.BoundingBox.from_list(box)
        return result

    result = PTN(
        page=navigator.page,
        pagesize=(navigator.height, navigator.width),
    )
    for item in navigator:
        result.insert(
            text=item.text,
            style=item.style,
            bounding=rotate_bounding(item.bounding, width=navigator.width),
            bounding_mean=item.bounding_mean,
            line=item.line,
            state=item.state,
        )
    return result


PTNs = typing.List[PTN]
PTCNs = typing.List[PTCN]


def insert_position(bounding: tuple, data: list) -> int:
    """Determine position in data list to insert Textinfo."""
    x0, y0 = int(bounding[0]), int(bounding[1])
    position = 0
    for item in data:
        pos = item.bounding
        if int(pos[1]) == y0:
            if x0 <= int(pos[0]):
                break
        elif y0 <= pos[1]:  # pylint:disable=R5601
            break
        position += 1
    return position


def insert_position_middle(bounding: tuple, data: list) -> int:
    """This strategy produces better results when inserting horizontal
    lines and is more accurat for this case."""
    x0, y0 = int(bounding[0]), (bounding[1] + bounding[3]) // 2
    position = 0
    for item in data:
        pos = item.bounding
        if (pos.y0 + pos.y1) // 2 == y0:
            if x0 <= int(pos.x0):
                break
        elif y0 <= (pos.y0 + pos.y1) // 2:  # pylint:disable=R5601
            break
        position += 1
    return position


def valid(item, inside, selector=SelectBounding.MAX):  # pylint:disable=R1260,R0911
    bounding = item.bounding
    (before, after, beforeleft, afterright) = inside
    # before and after are pixel coordinates
    if selector == SelectBounding.MAX:
        if not before <= bounding.y0 <= bounding.y1 <= after:
            return False
    elif selector == SelectBounding.MEAN:  # pylint:disable=R5601
        mean = bounding.y1 - item.bounding_mean
        if not before <= mean <= bounding.y1 <= after:
            return False
    elif selector == SelectBounding.TWO_THIRDS:  # pylint:disable=R5601
        sixty = bounding.y1 - (bounding.y1 - bounding.y0) * 0.66
        if not before <= sixty <= bounding.y1 <= after:
            return False
    elif selector == SelectBounding.TOP:  # pylint:disable=R5601
        if not before <= bounding.y0 <= after:
            return False
    elif selector == SelectBounding.BOTTOM:  # pylint:disable=R5601
        if not before <= bounding.y1 <= after:
            return False
    # TODO: ACTIVATE AFTER FIXING CONTENT BORDER OF MASTER_72
    # THERE ARE SOME SPACES WHICH MOVES CONTENT OVER THE PAGES,
    # THEREFORE 3.1. is ignored
    if not beforeleft <= bounding.x0 <= bounding.x1 <= afterright:
        return False
    return True


def navigator_to_content(navigator: PTN) -> texmex.text.TextBoundsInfos:
    result = []
    for item in navigator:
        info = texmex.text.TextBoundsInfo(
            bounds=item.bounding,
            text=item.text,
        )
        result.append(info)
    return result


def navigator_to_bounds(navigator: PTN) -> iamraw.BoundingBoxes:
    """Extract list of `BoundingBox` from `PTN`."""
    assert isinstance(navigator, NavigatorMixin), type(navigator)
    return [item.bounding for item in navigator]


class PTNMode(enum.Enum):
    BOTH = enum.auto()
    HORIZONTAL = enum.auto()
    VERTICAL = enum.auto()


def create_pagetextnavigators(  # pylint:disable=R0914,R1260
    text: iamraw.Document,
    text_positions,
    fontstore: iamraw.FontStore = None,
    fill_empty: bool = True,
    mode=PTNMode.BOTH,
    sort: bool = True,
) -> PTNs:
    result = []
    for textposition in text_positions:
        page = textposition.page
        content = utila.select_page(text, page)
        if content.width is not None:
            pagesize = (content.width, content.height)
        else:
            # TODO: OUTDATED, REMOVE LATER
            pagesize = text.dimension
        navigator = PTN(
            pagesize=pagesize,
            page=page,
        )
        textid = 0
        # remove horizontal or vertical text container
        content = select_textcontainer(content, mode=mode)
        for item in content:
            try:
                lines = item.lines
            except AttributeError:
                continue
            pos, mean = textposition.content[textid]
            for index, line in enumerate(lines):
                bounding = iamraw.split_y(pos, index, len(lines))
                if fontstore:
                    for char_number, char in enumerate(line.chars):
                        fontid = fontstore.fontid(
                            page,
                            textid,
                            index,
                            char_number,
                        )
                        char.font = fontid
                style = texmex.style.create_textstyle(line.chars)
                if isinstance(item, iamraw.VerticalTextContainer):
                    style.rotation = 1.0
                # TODO: Remove strip after container is fixed
                if not line.text.strip():
                    # skip bad removed rawmaker extraction
                    continue
                navigator.insert(
                    text=line.text,
                    style=style,
                    bounding=bounding,
                    bounding_mean=mean,
                    line=index,
                    sort=sort,
                )
            textid += 1
        result.append(navigator)
    if fill_empty:
        result = fill_empty_navigators(result, dimension=text.dimension)
    return result


def select_textcontainer(content, mode: PTNMode):
    if not content:
        return content

    if mode == PTNMode.HORIZONTAL:
        content = [
            item for item in content if isinstance(item, iamraw.TextContainer)
        ]
        return content

    if mode == PTNMode.VERTICAL:
        content = [
            item for item in content
            if isinstance(item, iamraw.VerticalTextContainer)
        ]
        return content
    return content


def fill_empty_navigators(
    navigators: PTNs,
    dimension: iamraw.PageSize,
) -> PTNs:
    """Some documents contain white pages.

    White pages contain no text and therefore no text_positions. The
    document [CONTENT, WHITEPAGE, CONTENT, CONTENT] produces the
    pagetextnavigators page =[0,2,3]. If we assume that some algorithm
    requires a closed row of navigators this can lead to
    problems.Therefore we insert an empty PTN at position
    1 to avoid these problems.
    """
    if not navigators:
        return []
    # require ascending list for while loop below
    navigators = sorted(navigators, key=lambda x: x.page)
    filled = [navigators[0]]
    for item in navigators[1:]:
        # fill empty
        while filled[-1].page + 1 < item.page:
            navigator = PTN(
                pagesize=dimension,
                page=filled[-1].page + 1,
            )
            filled.append(navigator)
        filled.append(item)
    return filled


def create_pagetextcontentnavigators(
    navigators,
    headerfooter,
    sizeandborder,
    horizontals: iamraw.PagesWithHorizontalList = None,
    validate_leftright: bool = True,
    pages: tuple = None,
) -> PTCNs:
    # TODO: require fill_empty?
    result = []
    for navigator in navigators:
        if utila.should_skip(navigator.page, pages):
            continue
        border = determine_border(headerfooter, sizeandborder, navigator.page)
        if border is None:
            # No page border available for text navigator, skip creation.
            # Processing selective pages produces white page navgiators
            # between content. For this white page navgiators, no page
            # content information are available. Therefore we do not add
            # this empty navgiator to list.
            continue
        if horizontals:
            insert_horizontals(navigator, horizontals)
        current = PTCN(
            navigator,
            border,
            validate_leftright=validate_leftright,
        )
        result.append(current)
    return result


HORIZONTAL = '<<<<<<<<<<<<<<<<<<<<HORIZONTAL>>>>>>>>>>>>>>>>>>>>'


def insert_horizontals(ptn: PTN, horizontals):
    selected = utila.select_content(horizontals, ptn.page)
    if not selected:
        return
    for horizontal in selected:  # iamraw.HorizontalLine
        ptn.insert(
            text=HORIZONTAL,
            style=None,
            bounding=horizontal.box,
            sort=insert_position_middle,
        )


def determine_border(headerfooter, sizeandborder, page: int):
    """Determine contentborder out of footer and header information."""
    pagesize = utila.select_page(sizeandborder, page)
    if pagesize is None:
        return pagesize
    border = pagesize.border
    pagesize = pagesize.size
    headerfooter = utila.select_page(headerfooter, page)
    top, bottom = 0, pagesize.height
    if headerfooter and headerfooter.header:
        top = pagesize.height * headerfooter.header.end
    if headerfooter and headerfooter.footer:
        bottom = bottom * headerfooter.footer.begin
    border = iamraw.Border(
        left=border.left,
        right=border.right,
        top=top,
        bottom=bottom,
    )
    return border


def create_pagetextnavigator_fromstr(content: str, fontsize=12.0):
    r"""\
    >>> create_pagetextnavigator_fromstr('I am a\nNavigator\ngood bye.')
    PTN(page=-1, pagesize=(612.0, 792.0), data=[I am a
    , Navigator
    , good bye.
    ], fast={BoundingBox(x0=50, y0=100, x1=200, y1=120): I am a
    , BoundingBox(x0=50, y0=120, x1=200, y1=140): Navigator
    , BoundingBox(x0=50, y0=140, x1=200, y1=160): good bye.
    })
    """
    result = PTN()
    for index, line in enumerate(content.splitlines()):
        bounding = iamraw.BoundingBox(
            x0=50,
            y0=100 + index * 20,
            x1=200,
            y1=100 + (index + 1) * 20,
        )
        content = [texmex.style.CharStyle(
            0,
            len(line),
            fontsize,
            0,
        )]
        style = texmex.style.TextStyle(content=content)
        result.insert(
            text=line,
            bounding=bounding,
            style=style,
        )
    return result


def single(navigators: PTNs) -> PTN:
    """Merge more than one pagenavigators to a single huge navigator to
    detect multi page lists."""
    # TODO: UPDATE PAGESIZE
    if not navigators:
        return None
    if navigators[0]:
        header = navigators[0][0].bounding[1]  # y0
    else:
        # starts on empty page without any content and no header
        header = 0
    y0 = header
    result = []
    for page in navigators:
        offset = y0 - header
        for item in page:
            # avoid side effects to other content
            item = item.copy()
            item.bounding.y0 = utila.roundme(item.bounding.y0 + offset)
            item.bounding.y1 = utila.roundme(item.bounding.y1 + offset)
            result.append(item)
        footer = page.content.bottom
        y0 += footer - header
    # create result
    navigator = texmex.PTN()
    navigator.data = result
    navigator.page = navigators[0].page
    return navigator
