# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================
r"""Multiline
    ---------

    This module aims to group/collect text depending on size and style
    into greater chunks. The first use case is to support multiple line
    headlines.

    .. code-block :: none

        font-size
        font-distance: y1[next] - y1[current]
        text-feed

    Remove high notes before starting analysis.
"""

import dataclasses
import math

import configo
import utila

import texmex
from texmex.group.fonts import feeddistance
from texmex.group.fonts import fontdistance
from texmex.navigator import PTN
from texmex.navigator import PTNs
from texmex.text import TextBoundsInfo
from texmex.text import TextBoundsInfos


@dataclasses.dataclass
class PageContentMultiLine:
    page: int = None
    content: list = dataclasses.field(default_factory=list)

    def __getitem__(self, index):
        return self.content[index]  # pylint:disable=E1136

    def __len__(self):
        return len(self.content)


PageContentMultiLines = list[PageContentMultiLine]


@dataclasses.dataclass
class MultilineGroup:
    """Group of following text lines with equal properties.

    Public Attributes:
        text: content as a list of following texmex.TextInfo.
        size: font size of common content.

    Ensure that MultilineGroup is hashable:
    >>> assert hash(MultilineGroup())
    """
    text: list = dataclasses.field(default_factory=list)
    size: float = None
    firstid: int = None
    bounding: tuple = None

    def append(self, item):
        self.text.append(item)  # pylint:disable=E1101

    def __getitem__(self, index):
        return self.text[index]  # pylint:disable=E1136

    def __len__(self):
        return len(self.text)

    def content_and_index(self):
        assert self.firstid is not None, 'create MultilineGroup with firstid'
        for index, item in enumerate(self, start=self.firstid):
            yield index, item

    def __hash__(self):
        return hash(str(self))


MultilineGroups = list[MultilineGroup]


def group_pages_by_fontsize(
    pagetextnavigators: PTNs,
    sizediff: float = 0.0,
) -> PageContentMultiLines:
    """Iterate thru different pages of `pagetextnavigators` and extract
    `MultilineGroups`s of the same font size.

    Args:
        pagetextnavigators: list of page content
        sizediff(float): maximum difference of 2 elements of extracted group.
    Returns:
        List of extracted `PageContentMultiLine`
    """
    assert sizediff >= 0.0
    result = [
        group_page_by_fontsize(page, sizediff=sizediff)
        for page in pagetextnavigators
    ]
    return result


def group_page_by_fontsize(
    pagetextnavigator: PTN,
    sizediff: float = 0.0,
) -> PageContentMultiLine:
    """Group text lines by `sizediff`.

    Args:
        pagetextnavigator(content): content of page to group
        sizediff(float): maximal font size difference between 2 text lines
    Returns:
        grouped `PageContentMultiLine`
    """
    assert sizediff >= 0.0
    current = []
    style, size = None, None
    for containerid, item in enumerate(pagetextnavigator):
        line = texmex.style_without_highnotes(item, merge=True)
        style = line.content[0]  # pylint:disable=E1136
        currentsize = style.size
        if size is None:
            # TODO: FIRST ITEM - MOVE BEFORE LOOP?
            size = currentsize
            current.append(
                MultilineGroup(
                    text=[item],
                    size=size,
                    firstid=containerid,
                ))
            continue
        if math.fabs(size - currentsize) > sizediff:
            size = currentsize
            current.append(
                MultilineGroup(
                    text=[],
                    size=size,
                    firstid=containerid,
                ))
        current[-1].append(item)
    return PageContentMultiLine(
        page=pagetextnavigator.page,
        content=current,
    )


def groupby_linedistance(page: PageContentMultiLine) -> PageContentMultiLine:
    flatten = utila.flat(page)
    distances = linedistances(flatten)
    grouped = group_linedistances(distances)
    content = unite_groups(page.content, grouped)
    result = PageContentMultiLine(page=page.page, content=content)
    return result


def linedistance(index, pagetextnavigator) -> float:
    current = pagetextnavigator[index]
    try:
        after = pagetextnavigator[index + 1]
    except IndexError:
        return None
    else:
        return utila.roundme(after.bounding.y1 - current.bounding.y1)


def linedistances(pagetextnavigator, noneatend=True):
    ending = len(pagetextnavigator)
    if not noneatend:
        ending = ending - 1
    return [
        linedistance(index, pagetextnavigator) for index in range(0, ending)
    ]


def group_linedistances(
    items: list[float],
    maxdiff: float = 0.0,
) -> list[int]:
    """Group items and return for every group with at least 2 members at
    list of indexes.

    Args:
        items: list of linedistances
        maxdiff(float): limit for gradient to be in same group
    Returns:
        list of list with indexs of grouped lines

    Content               linedistance
    Hallo - Headline      50

    Text                  10
    Text                  10
    Text                  30

    Pagenumber            None

    Prepare computing gradient: Duplicate first element and replace
    `None`-distance with distance before

                                    Gradient
                          50        0
    Hallo - Headline      50        -40

    Text                  10        0
    Text                  10        0
    Text                  30        20

    Pagenumber            30        0

    TODO: Extend documentation

    """
    assert items
    items = items[:]  # avoid side effects
    items = [items[0]] + items[:-1] + [items[-2]]
    grad = gradient(items)
    result = []
    current = []
    # TODO: THIS APPROACH DOES NOT WORK RIGHT NOW
    for index, diff in enumerate(grad, start=0):
        diff = diff if math.fabs(diff) > maxdiff else 0
        if diff == 0:  # pylint:disable=C2001
            current.append(index)
        # TODO: THINK ABOUT DIFF<0 and DIFF>0
        if diff < 0.0:
            if current:
                result.append(current)
            current = [index]
        if diff > 0.0:
            current.append(index)
            result.append(current)
            current = []
    if current:
        result.append(current)
    return result


SIZEDIFF_MAX = configo.HV_FLOAT_PLUS(default=1.0)

DISTANCE_MAX = configo.HolyTable(
    items=(
        (0, 22.0),
        (12.0, 22.0),
        (14.5, 30.0),
        (15.96, 35.0),
        (16.0, 50.0),
    ),
    strategy=utila.Strategy.UPPER,
)


def maxdistance(fontsize: float) -> float:
    return DISTANCE_MAX(fontsize)


def xdistances(content) -> list:
    r"""Determine changes in distance to left page border.

    >>> xdistances(texmex.ptn_fromstr('First\nSecond\nThird\nFourth\nFifth'))
    [None, 0.0, 0.0, 0.0, 0.0]

    Regression
    ----------
    Do not convert data type while rounding:
    >>> import texmex
    >>> xdistances(texmex.ptn_fromstr('First\n\Second'))
    [None, 0.0]

    Do not fail on too few items
    >>> xdistances(texmex.ptn_fromstr('First'))
    []
    """
    if len(content) <= 1:
        return []
    result = [None]
    diffs = utila.diffs([line.bounding[0] for line in content])
    diffs: list = utila.roundme(diffs, convert=False)
    result += diffs
    return result


def group_page_by_size_distance(
    content: PTN,
    distance_max: callable = maxdistance,
    sizediff_max: float = SIZEDIFF_MAX,
    xdist_max: float = None,
) -> MultilineGroups:
    assert isinstance(content, texmex.NavigatorMixin), type(content)
    grouped = texmex.group_linedistances_complex(
        content,
        distance_max=distance_max,
        sizediff_max=sizediff_max,
        xdist_max=xdist_max,
    )
    result = []
    for group in grouped:
        groupcontent = [content[index] for index in group]
        # TODO: make container more pythonic
        size = groupcontent[0].style.content[0].size
        firstid = group[0]
        bounding = utila.rect_max([item.bounding for item in groupcontent])
        result.append(
            MultilineGroup(
                bounding=bounding,
                firstid=firstid,
                size=size,
                text=groupcontent,
            ))
    return result


def gradient(items):
    # TODO: MOVE TO MORE GENERAL PLACE
    result = [
        (after - current) for current, after in zip(items[0:-1], items[1:])
    ]
    result = [utila.roundme(item) for item in result]
    return result


# NOTE: Statistical approach for group_linedistances, think about later
# grouped = []
# current = [(0, items[0])]
# for index, item in enumerate(items[1:-1], start=1):
#     mean = statistics.mean([var[1] for var in current])
#     if item is not None:
#         diff = math.fabs(item - mean)
#     else:
#         # last item has no text distance
#         diff = 0.0
#     if diff > maxdiff:
#         grouped.append(current)
#         current = []
#     current.append((index, item))
# if current:
#     grouped.append(current)
# print(grouped)
# # cluster requires at least two items
# grouped = [item for item in grouped if len(item) >= 1]
# print(grouped)
# # filter index
# grouped = [[index for index, _ in group] for group in grouped]
# print(grouped)
# return grouped


def unite_groups(content, indexs):
    # TODO: MOVE TO MORE GENERAL PLACE
    # TODO: DIRTY CODE :|
    result = []
    for items in indexs:
        current = content[0]
        if len(current) == len(items):
            result.append(current)
            content = content[1:]
        elif len(current) > len(items):
            result.append(current[:len(items)])
            content[0] = current[len(items):]
            if not content[0]:
                content = content[1:]
        else:
            removecount = len(items)
            removecount = removecount - len(current)
            content = content[1:]
            while removecount:
                current = content[0]
                removecount = removecount - len(current)
                if removecount:
                    content = content[1:]
                else:
                    content[0] = current[len(current):]
                    if not content[0]:
                        content = content[1:]
    return result


# Merge lines with lower distance to one text chunk.
MERGE_DISTANCE_MAX = configo.HV_FLOAT_PLUS(default=3.55)
MERGE_HORIZONTALY_MAX = configo.HV_FLOAT_PLUS(default=14.0)


def merge_content(  # pylint:disable=R0914
    text: TextBoundsInfos,
    max_x_merge=MERGE_HORIZONTALY_MAX,
    max_y_merge=MERGE_DISTANCE_MAX,
    uindex=None,
) -> TextBoundsInfos:
    """Merge content blocks to create greater content blocks depending on
    merge strategy.

    Args:
        text: chunk with iamraw.BoundingBox to merge
        max_x_merge(float): feed distance between the two left sides
        max_y_merge(float): vertical distance between 2 BoundingBoxes to
                            merge them into one
        uindex(list[int]): undefined index to link text(TextBoundsInfos) with
                           text-source if uindex is None, the `uindex` is an
                           ascending list starting with zero.
    Returns:
        (result, merged) - result is the merged content, merged - stores the
                           uindex which are merged together
    """
    if not text:
        # Nothing to merge
        return []
    # TODO: MERGE WITH GROUP_LINEDISTANCES_COMPLEX???
    # ensure input
    assert all(isinstance(item, TextBoundsInfo) for item in text), str(text)
    uindex = list(range(len(text))) if uindex is None else uindex
    bounds = [item.bounds for item in text]
    font_distance = fontdistance(bounds)
    feed_distance = feeddistance(bounds)
    # copy element
    result = [(text[0].bounds, [text[0].text])]
    merged = [[uindex[0]]]
    lines = zip(font_distance, feed_distance)
    for index, (fontdist, feeddist) in enumerate(lines, start=1):
        current_bounds, current_text = text[index].bounds, text[index].text
        if fontdist > max_y_merge:
            # new entree
            result.append((current_bounds, [current_text]))
            merged.append([uindex[index]])
            continue
        if abs(feeddist) > max_x_merge:
            # new entree
            result.append((current_bounds, [current_text]))
            merged.append([uindex[index]])
            continue
        # Merge me
        member_location, member_content = result[-1]
        merger_location, merger_content = text[index].bounds, text[index].text
        member_content.append(merger_content)
        merged[-1].append(uindex[index])
        # merged items together and save them as last item
        result[-1] = (
            utila.rect_max([member_location, merger_location]),
            member_content,
        )
    result = [TextBoundsInfo(
        text=item[1],
        bounds=item[0],
    ) for item in result]
    return result, merged


def merge_content_join(result):
    result = [
        TextBoundsInfo(
            text=utila.NEWLINE.join(item.text),
            bounds=item.bounds,
        ) for item in result
    ]
    return result
