# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import iamraw
import iamraw.fonts


def test_fonts_repr():
    """Test that to_str generates valid python code to ease writing tests"""
    expected = iamraw.Font(name='Helvetica', scale=12.0)

    # required imports for eval
    required = {
        'Font': iamraw.Font,
        'iamraw': iamraw,
        'iamraw.fonts': iamraw.fonts,
    }
    created = eval(str(expected), required)  # pylint:disable=eval-used

    assert created == expected
