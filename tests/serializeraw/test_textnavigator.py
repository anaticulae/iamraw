# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import iamraw.path
import serializeraw
import tests.serializeraw


def test_create_pagetextnavigator_frompath():
    loaded = serializeraw.create_pagetextnavigators_frompath(
        tests.serializeraw.RESTRUCTURED)
    for page in loaded:
        for line in page:
            assert line.text


def test_create_pagetextcontentnavigator_frompath():
    loaded = serializeraw.create_pagetextcontentnavigators_frompath(
        tests.serializeraw.RESTRUCTURED)
    for page in loaded:
        for line in page:
            assert line.text


def test_create_pagetextcontentnavigator_fromfile():
    source = tests.serializeraw.RESTRUCTURED
    text = iamraw.path.text(source)
    textpositions = iamraw.path.textposition(source)
    sizeandborderpath = iamraw.path.sizeandborder(source)
    headerfooterpath = iamraw.path.headerfooters(source)
    fontheader = iamraw.path.fontheader(source)
    fontcontent = iamraw.path.fontcontent(source)
    loaded = serializeraw.create_pagetextcontentnavigators_fromfile(
        text,
        textpositions,
        sizeandborderpath,
        headerfooterpath,
        fontheader,
        fontcontent,
    )
    assert len(loaded) == 11
