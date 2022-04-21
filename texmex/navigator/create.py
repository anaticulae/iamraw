# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import enum

import utila

import iamraw
import texmex.navigator
import texmex.style


class PTNMode(enum.Enum):
    BOTH = enum.auto()
    HORIZONTAL = enum.auto()
    VERTICAL = enum.auto()


@utila.rename(text_positions='textpositions')
def create_pagetextnavigators(
    text: iamraw.Document,
    textpositions: iamraw.PageContentTextPositions,
    fontstore: iamraw.FontStore = None,
    fill_empty: bool = True,
    mode=PTNMode.BOTH,
    sort: bool = True,
    state: 'TextState' = texmex.style.TextState.VISIBLE,
) -> texmex.navigator.PTNs:
    result = []
    for textposition in textpositions:
        page = textposition.page
        content = utila.select_page(text, page)
        if content.width is not None:
            pagesize = (content.width, content.height)
        else:
            # TODO: OUTDATED, REMOVE LATER
            pagesize = text.dimension
        navigator = texmex.navigator.PTN(
            pagesize=pagesize,
            page=page,
        )
        # remove horizontal or vertical text container
        content = select_textcontainer(content, mode=mode)
        fill_navigator(
            content,
            navigator,
            textposition,
            fontstore,
            sort,
            state,
        )
        result.append(navigator)
    if fill_empty:
        result = fill_empty_navigators(
            result,
            dimension=text.dimension,
        )
    return result


def fill_navigator(  # pylint:disable=R0914
    content,
    navigator,
    textposition,
    fontstore,
    sort,
    state: 'TextState' = texmex.style.TextState.VISIBLE,
):
    textid = 0
    for item in content:
        try:
            lines = item.lines
        except AttributeError:
            continue
        if skip(expected=state, current=item.state):
            continue
        pos, mean = textposition.content[textid]
        for index, line in enumerate(lines):
            bounding = iamraw.split_y(pos, index, len(lines))
            if fontstore:
                for char_number, char in enumerate(line.chars):
                    fontid = fontstore.fontid(
                        textposition.page,
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
                state=item.state,
            )
        textid += 1


def skip(expected, current) -> bool:
    if expected is None:
        return False
    if current is None:
        return False
    return expected != current


def create_pagetextcontentnavigators(
    navigators,
    headerfooter,
    sizeandborder,
    horizontals: iamraw.PagesWithHorizontalList = None,
    validate_leftright: bool = True,
    pages: tuple = None,
) -> texmex.navigator.PTCNs:
    # TODO: require fill_empty?
    result = []
    for navigator in navigators:
        if utila.should_skip(navigator.page, pages):
            continue
        border = determine_border(
            headerfooter,
            sizeandborder,
            navigator.page,
        )
        if border is None:
            # No page border available for text navigator, skip creation.
            # Processing selective pages produces white page navgiators
            # between content. For this white page navgiators, no page
            # content information are available. Therefore we do not add
            # this empty navgiator to list.
            continue
        if horizontals:
            insert_horizontals(navigator, horizontals)
        current = texmex.navigator.PTCN(
            navigator,
            border,
            validate_leftright=validate_leftright,
        )
        result.append(current)
    return result


def ptn_fromstr(content: str, fontsize=12.0):
    r"""\
    >>> ptn_fromstr('I am a\nNavigator\ngood bye.')
    PTN(page=-1, pagesize=(612.0, 792.0), data=[I am a
    , Navigator
    , good bye.
    ], fast={BoundingBox(x0=50, y0=100, x1=200, y1=120): I am a
    , BoundingBox(x0=50, y0=120, x1=200, y1=140): Navigator
    , BoundingBox(x0=50, y0=140, x1=200, y1=160): good bye.
    })
    """
    result = texmex.navigator.PTN()
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


def fill_empty_navigators(
    navigators: texmex.navigator.PTNs,
    dimension: iamraw.PageSize,
) -> texmex.navigator.PTNs:
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
            navigator = texmex.navigator.PTN(
                pagesize=dimension,
                page=filled[-1].page + 1,
            )
            filled.append(navigator)
        filled.append(item)
    return filled


HORIZONTAL = '<<<<<<<<<<<<<<<<<<<<HORIZONTAL>>>>>>>>>>>>>>>>>>>>'


def insert_horizontals(ptn: texmex.navigator.PTN, horizontals):
    selected = utila.select_content(horizontals, ptn.page)
    if not selected:
        return
    for horizontal in selected:  # iamraw.HorizontalLine
        ptn.insert(
            text=HORIZONTAL,
            style=None,
            bounding=horizontal.box,
            sort=texmex.navigator.insert_position_middle,
        )


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
