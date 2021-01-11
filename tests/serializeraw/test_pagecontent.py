# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utila

import iamraw
import serializeraw

CONTENT = [
    iamraw.PageContent(page=4, content=[1, 2, 3, 4, 5]),
    iamraw.PageContent(page=6, content=[4, 4, 4]),
    iamraw.PageContent(page=7, content=[]),
]
DUMPED = serializeraw.dump_pagecontent(CONTENT)


def test_pagecontent_dump_load():
    loaded = serializeraw.load_pagecontent(DUMPED)
    assert loaded == CONTENT


def test_pagecontent_selected():
    loaded = serializeraw.load_pagecontent(DUMPED, pages=(4, 5, 6))
    assert len(loaded) == 2


def test_pagecontent_specific_dumper():

    def dumped(items):
        raw = utila.from_tuple(items)
        return raw

    def loader(raw):
        return utila.numbers(raw.split())

    dumped = serializeraw.dump_pagecontent(CONTENT, pagedumper=dumped)
    loaded = serializeraw.load_pagecontent(dumped, pageloader=loader)
    assert loaded == CONTENT
