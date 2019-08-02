# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

from collections import namedtuple

from utila import error

Border = namedtuple('Border', 'left right top bottom')


def validate(items) -> bool:
    """Iterate throw elements and check if some element contains a negative
    element.

    Args:
        items(List[Border/PageSize]): list or single item is supported
    Returns:
        True if all elements are positive, False if at least one is not
    """
    valid = True
    if not isinstance(items, list):
        items = [items]
    for index, item in enumerate(items):
        for itemindex, check in enumerate(item):
            if check is not None and check < 0:
                msg = 'invalid field(%d, %d): %r' % (index, itemindex, check)
                error(msg)
                valid = False
    return valid
