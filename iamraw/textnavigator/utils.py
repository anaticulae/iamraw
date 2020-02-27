# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================
from iamraw import Border
from iamraw import PageSize


def topbottom(size: PageSize, contentborder: Border):
    height = size.height
    top, bottom = contentborder.top, contentborder.bottom
    top = percent_from_pagesize(height, top)
    bottom = percent_from_pagesize(height, bottom)
    return top, bottom


def percent_to_pagesize(
        size: float,
        percent: float,
) -> float:
    """Convert a percent value to page coordinates

    The top coordinate starts with 0.0 and ends on the bottom with 1.0.

    Args:
        size(float): paper height/width
        percent(float): [0.0; 1.0] of used size
    Returns:
        percentage page height/width value
    """
    assert size >= 0.0
    assert 0.0 <= percent <= 1.0

    result = (1.0 - percent) * size
    return result


def percent_from_pagesize(size, current) -> float:
    """Determine the percentage value of a pagesize

    Args:
        size(float): size of current page
        current(float): position on page
    Returns:
        value in percent in range of [0.0, 1.0]

    Example:
        size    500
        current 100
        return  0.8%

    Hint:
        The max size start at the top of the page.
    """
    assert size > 0
    assert size >= current
    return current / size
