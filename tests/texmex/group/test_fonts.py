# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import power
import pytest
import utilatest

import serializeraw
import texmex


def navigators():
    utilatest.fixture_requires(power.DOCU027_PDF)
    result = serializeraw.ptn_frompath(power.link(power.DOCU027_PDF))
    return result


def test_document_textsize():
    example = navigators()
    size = texmex.document_textsize(example)
    assert size == 9.96, str(size)


@utilatest.requires(power.DOCU027_PDF)
def test_document_textdistance():
    example = navigators()
    borders = serializeraw.load_pageborders(power.link(power.DOCU027_PDF))
    result = texmex.document_textdistance(example, borders)
    # TODO: INVESTIGATE LATER
    # This is not the right result. A change indicates that the algo
    # changed.
    assert result == 17.9, str(result)


@utilatest.requires(power.DOCU027_PDF)
def test_document_textdistance_from_contentnavigators():
    source = power.link(power.DOCU027_PDF)
    data = serializeraw.create_pagetextcontentnavigators_frompath(source)
    result = texmex.document_textdistance_from_contentnavigators(data)
    assert result == 17.9, str(result)


@utilatest.requires(power.DOCU027_PDF)
def test_document_textfeed():
    nav = serializeraw.ptn_frompath(power.link(power.DOCU027_PDF))
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
    (texmex.PageTextNavigatorMode.BOTH, False),
    (texmex.PageTextNavigatorMode.VERTICAL, True),
    (texmex.PageTextNavigatorMode.HORIZONTAL, False),
])
@utilatest.requires(power.DOCU027_PDF)
def test_navigator_filter_mode(mode, empty):
    result = serializeraw.create_pagetextnavigators_frompath(
        power.link(power.DOCU027_PDF),
        mode=mode,
        pages=(0,),
    )
    first = result[0][:]
    assert (not first) == empty, empty
