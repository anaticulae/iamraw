# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================
"""\
>>> Layout.STANDARD | Layout.DOUBLECOLUMN
<Layout.STANDARD|DOUBLECOLUMN: 9>
"""

import enum


class Layout(enum.Flag):
    # const page border width
    STANDARD = enum.auto()
    # alternating page border width
    LEFTRIGHT = enum.auto()
    # single text page
    SINGLE = enum.auto()
    # double column text page
    DOUBLECOLUMN = enum.auto()
    # double column block content
    DOUBLECOLUMN_HIGHDENSITY = enum.auto()
    # no information extractable
    UNDEFINED = enum.auto()


Layouts = list[Layout]
