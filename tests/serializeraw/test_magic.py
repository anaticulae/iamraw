# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import iamraw
import serializeraw


def test_dump_and_load_magic():
    data = [
        iamraw.PageContentContentType(
            page=5,
            content=[
                (1, iamraw.PageContentType.UNDEFINED),
                (2, iamraw.PageContentType.TEXT),
            ],
        ),
        iamraw.PageContentContentType(
            page=6,
            content=[
                (5, iamraw.PageContentType.LIST),
                (6, iamraw.PageContentType.TEXT),
            ],
        )
    ]
    dumped = serializeraw.dump_types(data)
    loaded = serializeraw.load_types(dumped)
    assert loaded == data
