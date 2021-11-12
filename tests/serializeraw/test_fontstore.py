# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import power
import pytest
import utilatest

import iamraw
import serializeraw


@pytest.fixture
def restructured_fontstore() -> iamraw.FontStore:
    """Loaded restructured FontStore.

    Regenerate data due:

        rawmaker -i power/power/repository/docu/restructuredtext.pdf
        --pages=0:11 --char_margin 5.0 --boxes_flow 1.0 --line_margin 0.3
    """
    utilatest.fixture_requires(power.DOCU027_PDF)
    result = serializeraw.create_fontstore_frompath(
        power.link(power.DOCU027_PDF))
    return result


FIRST_FONT = iamraw.Font(
    pdfref='WLXADN+NimbusSanL-Bold',
    name='NimbusSanL',
    scale=18.5,
    weight=iamraw.Weight.BOLD,
    flags=(iamraw.FontFlag.SYMBOLIC,),
)

SECOND_FONT = iamraw.Font(
    pdfref='AJOVIH+NimbusSanL-BoldItal',
    name='NimbusSanL',
    scale=12.85,
    weight=iamraw.Weight.BOLD,
    style=iamraw.Style.ITALIC,
    flags=(iamraw.FontFlag.SYMBOLIC,),
)
THIRD_FONT = iamraw.Font(
    pdfref='WLXADN+NimbusSanL-Bold',
    name='NimbusSanL',
    scale=12.85,
    weight=iamraw.Weight.BOLD,
    flags=(iamraw.FontFlag.SYMBOLIC,),
)

FORTH_FONT = iamraw.Font(
    pdfref='WLXADN+NimbusSanL-Bold',
    name='NimbusSanL',
    scale=8.93,
    weight=iamraw.Weight.BOLD,
    flags=(iamraw.FontFlag.SYMBOLIC,),
)

FIFTH_FONT = iamraw.Font(
    pdfref='WNIDNY+NimbusSanL-Regu',
    name='NimbusSanL',
    scale=10.71,
    weight=iamraw.Weight.LIGHT,
    style=iamraw.Style.NORMAL,
    stretch=iamraw.Stretch.REGULAR,
    flags=(iamraw.FontFlag.SYMBOLIC,),
)


@pytest.mark.parametrize('page,container,line,char,expected', [
    (0, 0, 1, 5, FIRST_FONT),
    (0, 2, 0, 5, SECOND_FONT),
    (0, 2, 0, 10, SECOND_FONT),
    (0, 3, 0, 11, THIRD_FONT),
    (0, 4, 0, 0, FORTH_FONT),
    (0, 4, 0, 12, FORTH_FONT),
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
    fontstore = restructured_fontstore
    fontid = fontstore.fontid(page, container, line, char)
    assert expected == fontstore[fontid]


@pytest.mark.parametrize('page,container,line,char', [
    (0, 4, 1, 0),
    (0, 4, 200, 0),
    (0, 5, 0, 0),
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
            'from that it’s considered a revision and reinterpreta-')
    # \ntion of'
    # ' two other markup languages, Setext and StructuredText.')
    first = iamraw.Font(
        pdfref='OUYNTX+NimbusRomNo9L-Regu',
        name='NimbusRomNo9L',
        scale=7.43,
        weight=iamraw.Weight.LIGHT,
        style=iamraw.Style.NORMAL,
        stretch=iamraw.Stretch.REGULAR,
        flags=(iamraw.FontFlag.SYMBOLIC,),
    )
    bold = iamraw.Font(  # pylint:disable=W0612
        name='NimbusRomNo9L',
        scale=7.43,
        weight=iamraw.Weight.MEDIUM,
        style=iamraw.Style.NORMAL,
        stretch=iamraw.Stretch.REGULAR,
        flags=(iamraw.FontFlag.SYMBOLIC,),
    )
    expected = [
        iamraw.FontChunk(content=text[0:154], font=first),
        # iamraw.FontChunk(content=text[154:161], font=bold),
        # iamraw.FontChunk(content=text[161:165], font=first),
        # iamraw.FontChunk(content=text[165:179], font=bold),
        # iamraw.FontChunk(content=text[179:], font=first),
    ]
    page = 4

    return (text, page, expected)


def test_fontstore_from_str(restructured_fontstore: iamraw.FontStore):  # pylint:disable=W0621
    """Determine fonts via text input and start of text sequence."""
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


@utilatest.requires(power.DOCU027_PDF)
def test_fontstore_font_access():
    loaded = serializeraw.create_fontstore_frompath(
        power.link(power.DOCU027_PDF))
    fontid = loaded.fontid(0, 0, 0, 0)
    font = loaded.font(0, 0, 0, 0)
    assert loaded[fontid] == font
