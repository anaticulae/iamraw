# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import texmex


def test_textinfo_hash():
    """Ensure that more than `text` is included in hash computation."""
    first = texmex.TextInfo('first', style=texmex.TextStyle())
    second = texmex.TextInfo('first')
    assert hash(first) != hash(second)
