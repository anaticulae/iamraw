# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import pytest

import serializeraw
import tests.serializeraw
import texmex


def navigators():
    result = serializeraw.create_pagetextnavigators_frompath(
        tests.serializeraw.RESTRUCTURED)
    return result


def test_document_textsize():
    example = navigators()
    size = texmex.document_textsize(example)
    assert size == 9.96, str(size)


def test_document_textdistance():
    example = navigators()
    borders = serializeraw.load_pageborders(tests.serializeraw.RESTRUCTURED)
    result = texmex.document_textdistance(example, borders)
    # TODO: INVESTIGATE LATER
    # This is not the right result. A change indicates that the algo
    # changed.
    assert result == 17.9, str(result)


def test_document_textfeed():
    nav = serializeraw.create_pagetextnavigators_frompath(
        tests.serializeraw.RESTRUCTURED)
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
def test_navigator_filter_mode(mode, empty):
    result = serializeraw.create_pagetextnavigators_frompath(
        tests.serializeraw.RESTRUCTURED,
        mode=mode,
        pages=(0,),
    )
    first = result[0][:]
    assert (not first) == empty, empty
