# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import iamraw


def test_iterable():
    """Create empty `Sections` and iterate over `Sections` and `AreaItem`s"""
    document = iamraw.Sections()
    for section in document:
        len(section)
        for item in section:  #pylint:disable=unused-variable
            pass
