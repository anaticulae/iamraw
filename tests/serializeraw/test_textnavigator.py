# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import hoverpower
import utilotest

import iamraw.path
import serializeraw


@utilotest.requires(hoverpower.DOCU027_PDF)
def test_create_pagetextnavigator_frompath():
    loaded = serializeraw.ptn_frompath(hoverpower.link(hoverpower.DOCU027_PDF))
    for page in loaded:
        for line in page:
            assert line.text


@utilotest.requires(hoverpower.DOCU027_PDF)
def test_create_pagetextcontentnavigator_frompath():
    loaded = serializeraw.ptcn_frompath(hoverpower.link(hoverpower.DOCU027_PDF))
    for page in loaded:
        for line in page:
            assert line.text


@utilotest.requires(hoverpower.DOCU027_PDF)
def test_create_pagetextcontentnavigator_fromfile():
    source = hoverpower.link(hoverpower.DOCU027_PDF)
    text = iamraw.path.text(source)
    textpositions = iamraw.path.textposition(source)
    sizeandborder = iamraw.path.sizeandborder(source)
    headerfooter = iamraw.path.headerfooters(source)
    fontheader = iamraw.path.fontheader(source)
    fontcontent = iamraw.path.fontcontent(source)
    loaded = serializeraw.ptcn_fromfile(
        text,
        textpositions,
        sizeandborder,
        headerfooter,
        fontheader,
        fontcontent,
    )
    assert len(loaded) == 27


@utilotest.requires(hoverpower.DOCU027_PDF)
def test_load_dump_ptn():
    source = hoverpower.link(hoverpower.DOCU027_PDF)
    ptns = serializeraw.ptn_frompath(source)
    fontstore = serializeraw.fs_frompath(source)
    dumped = serializeraw.dump_ptn(
        ptns=ptns,
        fontstore=fontstore,
    )
    assert dumped[0]  # document
    assert dumped[1]  # position
