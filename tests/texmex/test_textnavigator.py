# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import power
import utila
import utilatest

import iamraw
import serializeraw
import texmex


def test_insert_order(navigator):
    for before, after in zip(navigator[:-1], navigator[1:]):
        before = before.bounding
        after = after.bounding
        assert before.y0 <= after.y0
        if before.y0 == after.y0:
            assert before.x0 <= after.x0
    current_order = [int(item.text) for item in navigator]
    # items are sorted in ascending
    assert current_order == list(range(len(navigator))), current_order


def test_after(navigator):
    # Bottom footer
    after = 0.8  # from 80% to 100%
    # greater than 563
    # 1 item in this example
    result = navigator.after(after)
    assert len(result) == 4, result


def test_before(navigator):
    # Top footer
    # smaller than 158.4
    before = 0.2  # from 20% to 0%
    # 2 items in this example
    result = navigator.before(before)
    assert len(result) == 1, before


def test_fonts_navigator_to_bounds(navigator):
    result = texmex.navigator_to_bounds(navigator)
    assert all(isinstance(item, iamraw.BoundingBox) for item in result)


def sample():
    navigator = texmex.PTN()
    location = iamraw.BoundingBox.from_str('10.0 12.0 15 20')
    navigator.insert('me', bounding=location, style=None)
    location = iamraw.BoundingBox.from_str('100.0 120.0 150 200')
    navigator.insert('hello', bounding=location, style=None)
    return navigator


def test_hey_navigator_find():
    navigator = sample()
    location = iamraw.BoundingBox.from_str('100.0 120.0 150 200')
    located = navigator.find(location)
    assert located.text == 'hello'


def test_navigator_print_debug(capsys):
    navigator = sample()
    navigator.print_debug()
    expected = 'page: -1 size: (612.0, 792.0)\nme\nhello\n'
    current = utilatest.stdout(capsys)
    assert current == expected


def test_textnavigator_before(navigator):
    assert navigator.between(0, 0.5)


def test_textnavigator_roate_left(navigator):
    before = list(navigator)
    rotated = texmex.rotate_left(navigator)
    after = list(rotated)
    assert after != before


@utilatest.requires(power.DOCU027_PDF)
def test_textnavigator_inserthorizontals():
    source = power.link(power.DOCU027_PDF)
    ptn = serializeraw.ptcn_frompath(
        source,
        horizontals=True,
        pages=utila.rtuple(5),
    )
    counted = 0
    for page in ptn:
        for line in page:
            if line.text == texmex.HORIZONTAL:
                counted += 1
    # depending on pdf parser, horizontals varies
    assert 3 <= counted <= 7


@utilatest.requires(power.DOCU027_PDF)
def test_ptn_single():
    source = power.link(power.DOCU027_PDF)
    ptns = serializeraw.ptcn_frompath(source)
    merged = texmex.single(ptns)
    assert isinstance(merged, texmex.PTN)
