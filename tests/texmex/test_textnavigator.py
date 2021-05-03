# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import iamraw
import texmex


def test_insert_order(navigator):
    for before, after in zip(navigator[:-1], navigator[1:]):
        before = before.bounding
        after = after.bounding
        assert before.y0 <= after.y0
        if before.y0 == after.y0:
            assert before.x0 <= after.x0

    current_order = [item.text for item in navigator]

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
    assert all([isinstance(item, iamraw.BoundingBox) for item in result])


def test_hey_navigator_find():
    navigator = texmex.PageTextNavigator()
    location = iamraw.BoundingBox.from_str('10.0 12.0 15 20')
    navigator.insert('me', bounding=location, style=None)
    location = iamraw.BoundingBox.from_str('100.0 120.0 150 200')
    navigator.insert('hello', bounding=location, style=None)

    located = navigator.find(location)
    assert located.text == 'hello'


def test_textnavigator_before(navigator):
    assert navigator.between(0, 0.5)
