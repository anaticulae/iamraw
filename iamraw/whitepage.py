# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import collections
import enum


class WhitePage(enum.Enum):
    CONTENT = -1
    BLANK = 0  # nothing on the page
    WHITE = 1  # page with footer and/or header


PageContentWhitepage = collections.namedtuple(
    'PageContentWhitepage',
    'content, page',
)

PageContentWhitepages = list[PageContentWhitepage]
