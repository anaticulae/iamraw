# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import iamraw
import serializeraw


def test_titlepage_dump_and_load_titlepage():
    # TODO: Improve later
    titlepage = iamraw.TitlePage(
        title='The first one',
        thesis=iamraw.DocumentType.BOOK,
        date=iamraw.TitleDate(
            2019,
            10,
            28,
            'Berlin',
            True,
            'Berlin den 28.10.2019',
        ),
        author=iamraw.Person('Prof.', 'Mullur', 'John', 'Prof. John Mullur'),
    )
    dumped = serializeraw.dump_titlepage(titlepage)
    loaded = serializeraw.load_titlepage(dumped)
    assert loaded == titlepage
