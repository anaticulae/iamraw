# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import power
import utilatest

import iamraw.path
import serializeraw


@utilatest.requires(power.DOCU27_PDF)
def test_create_pagetextnavigator_frompath():
    loaded = serializeraw.ptn_frompath(power.link(power.DOCU27_PDF))
    for page in loaded:
        for line in page:
            assert line.text


@utilatest.requires(power.DOCU27_PDF)
def test_create_pagetextcontentnavigator_frompath():
    loaded = serializeraw.ptcn_frompath(power.link(power.DOCU27_PDF))
    for page in loaded:
        for line in page:
            assert line.text


@utilatest.requires(power.DOCU27_PDF)
def test_create_pagetextcontentnavigator_fromfile():
    source = power.link(power.DOCU27_PDF)
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
    assert len(loaded) == 27
