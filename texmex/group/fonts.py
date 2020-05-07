# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import collections
import statistics

import utila

import iamraw
import texmex
from texmex.navigator import PageTextNavigator
from texmex.navigator import PageTextNavigators
from texmex.text import FontOccurrences
from texmex.text import TextBounds
from texmex.text import TextBoundsInfos
from texmex.text import TextBoundsList


def fontdistance(bounds: iamraw.BoundingBoxes) -> utila.Floats:
    """Describes the difference between two content lines"""
    distance = [
        utila.roundme(second.y0 - first.y1)
        for (first), (second) in zip(bounds[0:], bounds[1:])
    ]
    return distance


def feeddistance(bounds: iamraw.BoundingBoxes) -> utila.Floats:
    """The text feed describes the distance from the left content border to
    the first content. The feeddistance describes the difference of two
    items"""
    distance = [
        utila.roundme(second.x0 - first.x0)
        for (first), (second) in zip(bounds[0:], bounds[1:])
    ]
    return distance


def fontdistance_textbounds(bounds: TextBoundsList) -> utila.Floats:
    assert isinstance(bounds, list)
    assert all(isinstance(item, TextBounds) for item in bounds)
    distance = [
        utila.roundme(first.bottomdist - second.bottomdist)
        for (first), (second) in zip(bounds[0:], bounds[1:])
    ]
    if bounds:
        # add distance from first content to page start
        # xdist, ydist(1), width, height, fontsize
        distance.insert(0, 0)
    distance.append(0)  # TODO: CHECK AGAIN
    return distance


NONE_BORDER = iamraw.Border(None, None, None, None)


def bounds_to_textbounds(
        bounds: iamraw.BoundingBox,
        contentborder: iamraw.Border = None,
) -> TextBounds:
    """Compute distance to page `contentborder` and determine font size

    Args:
        bounds(iamraw.BoundingBox): BoundingBox of item
        contentborder(Border): the border of page content if None (0,0) is used
    Returns:
        computed `TextBounds`
    """
    assert contentborder, contentborder
    x0, y0, x1, y1 = bounds
    return TextBounds(
        int(x0 - contentborder.left),
        int(contentborder.right - x1),
        int(y0 - contentborder.top),
        int(contentborder.bottom - y1),
    )


def textbounds(
        navigator: PageTextNavigator,
        contentborder: iamraw.Border,
) -> TextBoundsInfos:
    assert isinstance(navigator, texmex.NavigatorMixin), type(navigator)

    # ensure that order of items has no effect
    cb = contentborder  # pylint:disable=C0103
    __x0, __y0, __x1, __y1 = cb.left, cb.top, cb.right, cb.bottom
    if not navigator:
        return []

    result = [
        texmex.TextBoundsInfo(
            text=item.text,
            bounds=bounds_to_textbounds(item.bounding, contentborder),
        ) for item in navigator
    ]
    return result


def textsize(occurrences: FontOccurrences) -> int:
    """Compute size of text"""
    mostly = sorted(occurrences, key=lambda item: item[1], reverse=True)
    if not mostly:
        return None
    most_font_item = mostly[0]
    size = most_font_item[0]
    return size


def textsize_frompage(navigator: PageTextNavigator) -> float:
    assert isinstance(navigator, PageTextNavigator), type(navigator)
    collected = []
    for line in navigator:
        fontsizes = texmex.TextStyle.textsizes(
            line.style,
            method=lambda x: x,  # do not filter anything
        )
        collected.extend(fontsizes)
    return utila.mode(collected, minimize=True)


def document_textfeed(
        navigators: PageTextNavigators,
        count: int = 1,
        left: bool = True,
) -> utila.Ints:
    assert count >= 1, f'require none negative count, got: {count}'
    counter = collections.Counter()
    for navigator in navigators:
        for item in navigator:
            if not item.text.strip():
                continue
            if left:
                counter[item.bounding[0]] += 1
            else:
                right = navigator.width - item.bounding[2]
                counter[right] += 1
    result = counter.most_common(count)
    result = [item for item, _ in result]
    if count == 1:
        return result[0]
    return result[0:count]


def document_textsize(navigators) -> float:
    """Determine the most common text size"""
    collected = []
    for navigator in navigators:
        for line in navigator:
            fontsizes = texmex.TextStyle.textsizes(
                line.style,
                method=lambda x: x,  # do not filter anything
            )
            collected.extend(fontsizes)
    return statistics.mode(collected)


def document_textdistance(navigators, borders: iamraw.Borders) -> int:
    """Determine the most common text distance"""
    result = []
    for _, (navigator, contentborder) in utila.sync_pages([navigators, borders]): # yapf:disable
        if not navigator:
            # empty page
            continue
        bounds = texmex.textbounds(navigator, contentborder.border)
        # ignore empty content
        bounds = [item.bounds for item in bounds if len(item.text)]
        ydist = [item.bottomdist for item in bounds]
        for yfirst, ysecond in zip(ydist[:-1], ydist[1:]):
            distance = yfirst - ysecond
            result.append(distance)
    mode = utila.modes(result)
    return mode
