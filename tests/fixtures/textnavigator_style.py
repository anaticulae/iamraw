# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import iamraw
import texmex

EXAMPLE = texmex.TextInfo(
    text=('aller Internetnutzer1 waren im Jahr 2013'
          ' auf entsprechenden Seiten angemeldet und'),
    bounding=iamraw.BoundingBox(x0=113.42, y0=163.65, x1=527.52, y1=177.33),
    style=texmex.TextStyle(
        content=[
            texmex.CharStyle(start=0, end=20, size=12.0, rise=0.0),
            texmex.CharStyle(start=20, end=21, size=8.04, rise=6.37),
            texmex.CharStyle(start=21, end=82, size=12.0, rise=0.0),
            # high standing `d` of `und`
            texmex.CharStyle(start=82, end=83, size=12.0, rise=6.0),
        ],),
)
