# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import iamraw

FIRST = """\
The RestructuredText Book
Documentation

Release 0.1

Daniel Greenfeld, Eric Holscher
Sep 27, 2017
"""

THIRD = """\
Contents

1 RestructuredText Tutorial 3
2 RestructuredText Guide 5

2.1 Basics .  . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
2.2 Blockquotes .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
2.3 Code: Block . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6

3 RestructuredText Customizations 7
4 Sphinx Tutorial 9
4.1 Step 1 . . . . . . . . . . . . . . . . . . . 9
4.2 Step 2 . . . . . . . . . . . . . . . . . . . 13

5 Sphinx Guide 15
6 Sphinx Customizations 17
7 Testing your Documentation 19
8 Indices and tables 21


i
"""


def document() -> iamraw.Document:
    result = iamraw.Document()

    for number, content in [
        (0, FIRST),
        (1, ''),
        (2, THIRD),
    ]:
        page = iamraw.Page(page=number)
        for container in content.split('\n\n'):
            page.append(iamraw.TextContainer.fromstr(container))
        result.append(page)
    return result
