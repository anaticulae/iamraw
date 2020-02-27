# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================
import typing

import utila

import iamraw.textnavigator.style
import iamraw.textnavigator.utils
from iamraw.border import Border
from iamraw.bounding import BoundingBox
from iamraw.bounding import BoundingBoxes
from iamraw.document import Document
from iamraw.document import PageSize
from iamraw.fontstore import FontStore

START = 0.0
END = 1.0

DISABLE_VALIDATION = END * 2


class NavigatorMixin:
    pass


class PageTextNavigator(NavigatorMixin):
    """The PageTextNavigator eases to navigate through the textual
    content of a Page. The text is processed from top to down and left
    to right.

    To fill navigator with content use `insert`. Acessing the data is
    possible trough `between`, `before`, `after` or __getitem__.
    """

    def __init__(self, size=None, page=-1):
        """Initialize PageTextNavigator with maximal `size`

        Args:
            size(tuple): maximal width/height of PageTextNavigator
            page(int): page number of PageTextNavigator-instance

        Sizes:
            A4: 210 x 297 mm, 8.26 x 11.69 inch, 595 x 842pt
                                                 612 x 792pt
        """
        if size is None:
            size = (612.0, 792.0)
        self.page = page
        self.data = []
        self.width, self.height = size

    def insert(
            self,
            text: str,
            style: iamraw.textnavigator.style.TextStyle,
            bounding: BoundingBox,
    ):
        """Insert text element top to bottom and left to right.

        Args:
            text(str): content of text chunk
            style: style for every character of `text`
            bounding(iamraw.BoundingBox): position and dimension of text area
        """
        x0, y0, x1, y1 = bounding

        assert 0 <= x0 <= x1, f'0<={x0}<={x1}'
        assert 0 <= y0 <= y1, f'0<={y0}<={y1}'
        # TODO: Substract border to move starting text to (0,0)?. If not,
        # x1 is sometimes higher than self.width.

        if (x1 - x0) > self.width:
            utila.error(f'page: {self.page} width: {x1-x0} < {self.width}')
        # assert (x1 - x0) < self.width, f'{x1-x0} < {self.width}'
        if (y1 - y0) > self.height:
            utila.error(f'page: {self.page} height: {y1-y0} < {self.height}')
        # assert (y1 - y0) < self.height, f'{y1-y0} < {self.height}'

        position = 0
        for item in self.data:
            pos = item.bounding
            if int(pos.y0) == int(y0):
                if int(x0) <= int(pos.x0):
                    break
            elif y0 <= pos.y0:
                break
            position += 1
        datum = iamraw.textnavigator.style.TextInfo(
            text=text,
            bounding=bounding,
            style=style,
        )
        self.data.insert(position, datum)

    def between(
            self,
            top: float,
            bottom: float,
            left: float = START,
            right: float = END,
    ) -> list:
        """Return content between to and bottom and left to right in
        range [top(0.0), bottom(1.0)] and [left(0.0), right(1.0)].

        Args:
            top(float): accepted content after top mark
            bottom(float): accepted content before bottom mark
            left(float): accepted content after left mark
            right(float): accepted content before right mark
        Returns:
            list of `TextInfo`
        """
        assert START <= top <= bottom <= END, (
            f'{START}<={top}<={bottom}<={END}')
        assert START <= left <= right <= DISABLE_VALIDATION, (
            f'{START}<={left}<={right}<={DISABLE_VALIDATION}')

        before = top * self.height
        after = bottom * self.height
        beforeleft = left * self.width
        afterright = right * self.width

        result = []
        for item in self.data:
            bounding = item.bounding
            # before and after are pixel coordinates
            if not before <= bounding.y0 <= bounding.y1 <= after:
                continue
            # TODO: ACTIVATE AFTER FIXING CONTENT BORDER OF MASTER_72
            # THERE ARE SOME SPACES WHICH MOVES CONTENT OVER THE PAGES,
            # THEREFORE 3.1. is ignored
            if not beforeleft <= bounding.x0 <= bounding.x1 <= afterright:
                continue
            result.append(item.copy())
        return result

    def __getitem__(self, index) -> iamraw.textnavigator.style.TextInfo:
        return self.data[index]

    def __len__(self) -> int:
        """Count text chunks"""
        return len(self.data)

    def __iter__(self):
        return iter(self.data)

    @property
    def dimension(self):
        return PageSize(width=self.width, height=self.height)

    def before(self, height: float, width: float = END) -> list:
        """Determine elements on the top of the document

        Args:
            height(float[0.0,1.0]): 0.0 is top, 1.0 is bottom
            width: marker from left to right, return elements [0.0 width]
        Returns:
            list of `TextInfo`
        """
        result = self.between(START, height, left=START, right=width)
        return result

    def after(self, height, width=START):
        """Determine elements after `height` till the bottom of the
        page. Additonal shrink from left to right with `width`."""
        result = self.between(height, END, width, END)
        return result

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

    def find(self, location: BoundingBox):
        # TODO: VERY SLOW
        for item in self.data:
            if location == item.bounding:
                return item
        raise ValueError(f'could not find {location}')


class PageTextContentNavigator(NavigatorMixin):
    """Iterate over page content without footer and header.

    See: :class:`hey.textnavigator.navigator.PageTextNavigator`.
    """

    def __init__(
            self,
            textnavigator: PageTextNavigator,
            content: Border,
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
        msg = 'require `PageTextNavigator` got: %s' % type(textnavigator)
        assert isinstance(textnavigator, PageTextNavigator), msg
        msg = 'require `Border` got: %s' % type(content)
        assert isinstance(content, Border), msg
        pagesize = PageSize(
            width=textnavigator.width,
            height=textnavigator.height,
        )
        self.content = content
        assert content.bottom >= 100, str(content)  # ensure that are pixel
        top, bottom = iamraw.textnavigator.utils.topbottom(pagesize, content)
        assert 0 <= top <= bottom <= 1.0, str(top) + str(bottom)
        self._page = textnavigator.page

        # disable validation if required
        right = END if validate_leftright else DISABLE_VALIDATION

        self.data = textnavigator.between(top, bottom, right=right)
        self._offset = textnavigator.offset(top, bottom)

    @property
    def offset(self):
        return self._offset

    @property
    def page(self):
        return self._page

    @property
    def width(self):
        # TODO: adjust dimension to content border
        return self.content.right

    @property
    def height(self):
        # TODO: adjust dimension to content border
        return self.content.bottom - self.content.top

    def __getitem__(self, index):
        return self.data[index]

    def __len__(self):
        return len(self.data)


PageTextNavigators = typing.List[PageTextNavigator]
PageTextContentNavigators = typing.List[PageTextContentNavigator]

# def navigator_to_content(navigator: PageTextNavigator,
#               ) -> hey.textnavigator.TextBoundsList:
#     result = []
#     for item in navigator:
#         info = hey.textnavigator.TextBoundsInfo(
#             bounds=item.bounding,
#             text=item.text,
#         )
#         result.append(info)
#     return result


def navigator_to_bounds(navigator: PageTextNavigator) -> BoundingBoxes:
    """Extract list of `BoundingBox` from `PageTextNavigator`."""
    assert isinstance(navigator, NavigatorMixin), type(navigator)
    return [item.bounding for item in navigator]


def create_pagetextnavigators(  # pylint:disable=R0914
        text: Document,
        text_positions,
        fontstore: FontStore = None,
) -> PageTextNavigators:
    result = []
    for textposition in text_positions:
        page = textposition.page
        navigator = PageTextNavigator(
            size=text.dimension,
            page=page,
        )
        textid = 0
        content = utila.select_page(text, page)
        for item in content:
            try:
                lines = item.lines
            except AttributeError:
                continue
            pos = textposition.content[textid]
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
                style = iamraw.textnavigator.style.create_textstyle(line.chars)
                # TODO: Remove strip after container is fixed
                if not line.text.strip():
                    # skip bad removed rawmaker extraction
                    continue
                navigator.insert(
                    text=line.text,  #.strip(),
                    style=style,
                    bounding=bounding,
                )
            textid += 1
        result.append(navigator)

    result = fill_empty_navigators(result, dimension=text.dimension)
    return result


def fill_empty_navigators(
        navigators: PageTextNavigators,
        dimension: iamraw.PageSize,
) -> PageTextNavigators:
    """Some documents contain white pages. White pages contain no
    text and therefore no text_positions. The document [CONTENT,
    WHITEPAGE, CONTENT, CONTENT] produces the pagetextnavigators
    page =[0,2,3]. If we assume that some algorithm requires a
    closed row of navigators this can lead to problems.Therefore we
    insert an empty PageTextNavigator at position 1 to avoid these
    problems.
    """
    if not navigators:
        return []
    # require ascending list for while loop below
    navigators = sorted(navigators, key=lambda x: x.page)
    filled = [navigators[0]]
    for item in navigators[1:]:
        # fill empty
        while filled[-1].page + 1 < item.page:
            navigator = PageTextNavigator(
                size=dimension,
                page=filled[-1].page + 1,
            )
            filled.append(navigator)
        filled.append(item)
    return filled


def create_pagetextcontentnavigators(
        navigators,
        headerfooter,
        sizeandborder,
        validate_leftright: bool = True,
        pages: tuple = None,
) -> PageTextContentNavigators:
    result = []
    for navigator in navigators:
        if utila.should_skip(navigator.page, pages):
            continue
        border = determine_border(headerfooter, sizeandborder, navigator.page)
        result.append(
            PageTextContentNavigator(
                navigator,
                border,
                validate_leftright=validate_leftright,
            ))
    return result


def determine_border(headerfooter, sizeandborder, page: int):
    """Determine contentborder out of footer and header information."""
    pagesize = utila.select_page(sizeandborder, page).size
    headerfooter = utila.select_page(headerfooter, page)
    top, bottom = 0, pagesize.height
    if headerfooter and headerfooter.header:
        top = pagesize.height * headerfooter.header.end
    if headerfooter and headerfooter.footer:
        bottom = bottom * headerfooter.footer.begin
    border = Border(
        left=0,
        right=pagesize.width,  # TODO: INVESTIGATE HERE
        top=top,
        bottom=bottom,
    )
    return border


def create_pagetextnavigator_fromstr(content: str, fontsize=12.0):
    result = PageTextNavigator()
    for index, line in enumerate(content.splitlines()):
        bounding = BoundingBox(
            x0=50,
            y0=100 + index * 20,
            x1=200,
            y1=100 + (index + 1) * 20,
        )
        content = [
            iamraw.textnavigator.style.CharStyle(
                0,
                len(line),
                fontsize,
                0,
            )
        ]
        style = iamraw.textnavigator.style.TextStyle(content=content)
        result.insert(
            text=line,
            bounding=bounding,
            style=style,
        )
    return result
