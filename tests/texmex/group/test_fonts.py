# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import hoverpower
import pytest
import utilotest

import serializeraw
import texmex


def navigators():
    utilotest.fixture_requires(hoverpower.DOCU027_PDF)
    result = serializeraw.ptn_frompath(hoverpower.link(hoverpower.DOCU027_PDF))
    return result


def test_document_textsize():
    example = navigators()
    size = texmex.document_textsize(example)
    assert size == 9.96, str(size)


@utilotest.requires(hoverpower.DOCU027_PDF)
def test_document_textdistance():
    example = navigators()
    borders = serializeraw.load_pageborders(
        hoverpower.link(hoverpower.DOCU027_PDF))
    result = texmex.document_textdistance(example, borders)
    # TODO: INVESTIGATE LATER
    # This is not the right result. A change indicates that the algo
    # changed.
    assert result == 17.9, str(result)


@utilotest.requires(hoverpower.DOCU027_PDF)
def test_document_textdist_from_ptcns():
    source = hoverpower.link(hoverpower.DOCU027_PDF)
    data = serializeraw.ptcn_frompath(source)
    result = texmex.document_textdist_from_ptcns(data)
    assert result == 17.9, str(result)


@utilotest.requires(hoverpower.DOCU027_PDF)
def test_document_textfeed():
    nav = serializeraw.ptn_frompath(hoverpower.link(hoverpower.DOCU027_PDF))
    leftfeed = texmex.document_textfeed(nav, left=True)
    assert leftfeed == 72.0, str(leftfeed)
    # distance of x1 to right page border
    rightfeed = texmex.document_textfeed(nav, left=False)
    assert rightfeed == 72.0, str(rightfeed)


def test_textsize_frompage():
    example = navigators()[0]
    result = texmex.textsize_frompage(example)
    assert result == 17.22, str(result)


@pytest.mark.parametrize('mode, empty', [
    (texmex.PTNMode.BOTH, False),
    (texmex.PTNMode.VERTICAL, True),
    (texmex.PTNMode.HORIZONTAL, False),
])
@utilotest.requires(hoverpower.DOCU027_PDF)
def test_navigator_filter_mode(mode, empty):
    result = serializeraw.ptn_frompath(
        hoverpower.link(hoverpower.DOCU027_PDF),
        mode=mode,
        pages=(0,),
    )
    first = result[0][:]
    assert (not first) == empty, empty
