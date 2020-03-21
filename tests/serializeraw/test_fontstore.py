# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import pytest

import iamraw
import serializeraw
import tests.serializeraw


@pytest.fixture
def restructured_fontstore() -> iamraw.FontStore:
    result = serializeraw.create_fontstore_frompath(
        tests.serializeraw.RESTRUCTURED)
    return result


FIRST_FONT = iamraw.Font(
    name='NimbusSanL',
    scale=18.5,
    weight=iamraw.Weight.BOLD,
)

SECOND_FONT = iamraw.Font(
    name='NimbusSanL',
    scale=12.85,
    weight=iamraw.Weight.BOLD,
    style=iamraw.Style.ITALIC,
)
THIRD_FONT = iamraw.Font(
    name='NimbusSanL',
    scale=12.85,
    weight=iamraw.Weight.BOLD,
)

FORTH_FONT = iamraw.Font(
    name='NimbusSanL',
    scale=8.93,
    weight=iamraw.Weight.BOLD,
)

FIFTH_FONT = iamraw.Font(
    name='NimbusSanL',
    scale=10.71,
    weight=iamraw.Weight.LIGHT,
    style=iamraw.Style.NORMAL,
    stretch=iamraw.Stretch.REGULAR,
)


@pytest.mark.parametrize('page,container,line,char,expected', [
    (0, 0, 1, 5, FIRST_FONT),
    (0, 1, 0, 5, SECOND_FONT),
    (0, 1, 0, 10, SECOND_FONT),
    (0, 2, 0, 11, THIRD_FONT),
    (0, 3, 0, 0, FORTH_FONT),
    (0, 3, 0, 12, FORTH_FONT),
    (2, 0, 0, 0, FIFTH_FONT),
    (2, 0, 0, 7, FIFTH_FONT),
])
def test_fontstore_access_font_id(
        restructured_fontstore: iamraw.FontStore,  # pylint:disable=W0621
        page,
        container,
        line,
        char,
        expected,
):
    expected_fontid = hash(expected)
    fontstore = restructured_fontstore
    fontid = fontstore.fontid(page, container, line, char)
    if expected == iamraw.NO_FONT:
        expected_fontid = iamraw.NO_FONT
    assert fontid == expected_fontid


@pytest.mark.parametrize('page,container,line,char', [
    (0, 3, 1, 0),
    (0, 3, 200, 0),
    (0, 4, 0, 0),
    (1, 0, 0, 0),
])
def test_fontstore_access_out_of_bounds(
        restructured_fontstore: iamraw.FontStore,  # pylint:disable=W0621
        page,
        container,
        line,
        char,
):
    """Notes: (1,0,0,0): empty page"""
    fontstore = restructured_fontstore
    fontid = fontstore.fontid(page, container, line, char)
    assert fontid == iamraw.NO_FONT


def expected_result():
    text = ('RestructuredText (reST) is a markup language, it’s name coming '
            'from that it’s considered a revision and reinterpreta-\ntion of'
            ' two other markup languages, Setext and StructuredText.')
    first = iamraw.Font(
        name='NimbusRomNo9L',
        scale=7.43,
        weight=iamraw.Weight.LIGHT,
        style=iamraw.Style.NORMAL,
        stretch=iamraw.Stretch.REGULAR,
    )
    bold = iamraw.Font(
        name='NimbusRomNo9L',
        scale=7.43,
        weight=iamraw.Weight.MEDIUM,
        style=iamraw.Style.NORMAL,
        stretch=iamraw.Stretch.REGULAR,
    )
    expected = [
        iamraw.FontChunk(content=text[0:154], font=first),
        iamraw.FontChunk(content=text[154:161], font=bold),
        iamraw.FontChunk(content=text[161:165], font=first),
        iamraw.FontChunk(content=text[165:179], font=bold),
        iamraw.FontChunk(content=text[179:], font=first),
    ]
    page = 4

    return (text, page, expected)


def test_fontstore_from_str(
        restructured_fontstore: iamraw.FontStore,  # pylint:disable=W0621
):
    """Determine fonts via text input and start of text sequence"""
    fontstore = restructured_fontstore
    (text, page, expected) = expected_result()
    result = fontstore.fromstr(page, 1, 0, text)

    assert len(result) == len(expected), str(result)
    for (res, exp) in zip(result, expected):
        assert res == exp
    assert result == expected, str(result)


def test_fontstore_font_to_fontid():
    # prepare sample font store
    # pylint:disable=C0103
    f0 = iamraw.Font(name='SuperFont', scale=12.5)
    f1 = iamraw.Font(name='Arial', scale=12.5)
    f2 = iamraw.Font(name='Verdana', scale=17.5)
    f3 = iamraw.Font(name='Times', scale=5)
    f4 = iamraw.Font(name='Arial', scale=20)
    f5 = iamraw.Font(name='Arial', scale=5)
    header = [f0, f1, f2, f3, f4, f5]
    content = [iamraw.PageFontContent(content=[], page=0)]

    store = iamraw.FontStore(header, content)
    assert store.font_to_fontid(f4) == hash(f4)
    assert store.font_to_fontid(f3) == hash(f3)
    assert store.font_to_fontid(f3) == hash(f3)
    assert store.font_to_fontid(f0) == hash(f0)
    assert store.font_to_fontid(f5) == hash(f5)


def test_fontstore_font_access():
    loaded = serializeraw.create_fontstore_frompath(
        tests.serializeraw.RESTRUCTURED)
    fontid = loaded.fontid(0, 0, 0, 0)
    font = loaded.font(0, 0, 0, 0)
    assert loaded[fontid] == font
