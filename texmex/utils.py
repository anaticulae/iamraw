# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utilo

import iamraw


def topbottom(size: iamraw.PageSize, contentborder: iamraw.Border):
    """Determine percentage start of coordinate. The origin of the
    coordinate starts on the top left position.

    >>> topbottom(iamraw.PageSize(1024,768), iamraw.Border(left=0, right=0, top=128, bottom=680))
    (0.1667, 0.8854)
    """
    top, bottom = contentborder.top, contentborder.bottom
    top = contentborder.top / size.height
    bottom = contentborder.bottom / size.height
    top, bottom = utilo.roundme(top, bottom, digits=4)
    return top, bottom
