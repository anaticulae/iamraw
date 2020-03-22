# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

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
    assert result == 1, str(result)


def test_document_textfeed():
    pagetextcontentnavigators = serializeraw.create_pagetextcontentnavigators_frompath(
        tests.serializeraw.RESTRUCTURED)
    textfeed = texmex.document_textfeed(pagetextcontentnavigators)
    # TODO: HOLY VALUE, INVESTIGATGE LATER
    assert textfeed == 72, str(textfeed)


def test_textsize_frompage():
    example = navigators()[0]
    result = texmex.textsize_frompage(example)
    assert result == 17.22, str(result)
