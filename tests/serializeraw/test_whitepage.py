# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================
import iamraw
import serializeraw

EXAMPLE = [
    iamraw.PageContentWhitepage(content=iamraw.WhitePage.CONTENT, page=0),
    iamraw.PageContentWhitepage(content=iamraw.WhitePage.BLANK, page=1),
    iamraw.PageContentWhitepage(content=iamraw.WhitePage.CONTENT, page=2),
    iamraw.PageContentWhitepage(content=iamraw.WhitePage.WHITE, page=7),
    iamraw.PageContentWhitepage(content=iamraw.WhitePage.CONTENT, page=8),
    iamraw.PageContentWhitepage(content=iamraw.WhitePage.CONTENT, page=9),
    iamraw.PageContentWhitepage(content=iamraw.WhitePage.CONTENT, page=10),
    iamraw.PageContentWhitepage(content=iamraw.WhitePage.WHITE, page=11),
    iamraw.PageContentWhitepage(content=iamraw.WhitePage.CONTENT, page=12),
    iamraw.PageContentWhitepage(content=iamraw.WhitePage.CONTENT, page=18),
    iamraw.PageContentWhitepage(content=iamraw.WhitePage.WHITE, page=19),
    iamraw.PageContentWhitepage(content=iamraw.WhitePage.CONTENT, page=20),
    iamraw.PageContentWhitepage(content=iamraw.WhitePage.WHITE, page=21),
    iamraw.PageContentWhitepage(content=iamraw.WhitePage.CONTENT, page=22),
    iamraw.PageContentWhitepage(content=iamraw.WhitePage.WHITE, page=23),
    iamraw.PageContentWhitepage(content=iamraw.WhitePage.CONTENT, page=26),
]


def test_whitepage_dump_and_load():
    dumped = serializeraw.dump_whitepages(EXAMPLE)
    assert len(dumped) > 100, str(dumped)
    loaded = serializeraw.load_whitepages(dumped)
    assert loaded == EXAMPLE


def test_whitepage_dump_and_load_pages():
    """Test skipping pages."""
    dumped = serializeraw.dump_whitepages(EXAMPLE)
    assert len(dumped) > 100, str(dumped)
    loaded = serializeraw.load_whitepages(dumped, tuple(range(5, 30)))
    assert loaded == EXAMPLE[3:]
