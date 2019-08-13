# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

from iamraw import Font
from iamraw import Stretch
from iamraw import Style
from iamraw import Weight


def test_fonts_repr():
    """Test that to_str generates valid python code to ease writing tests"""
    helvetica = Font(name='Helvetica', scale=12.0)

    required = {
        'Weight': Weight,
        'Style': Style,
        'Stretch': Stretch,
        'Font': Font
    }
    # pylint:disable=eval-used
    assert eval(str(helvetica), required) == helvetica
