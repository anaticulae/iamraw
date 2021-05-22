# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import power

import serializeraw
import texmex


def test_group_page_by_size_distance():
    navigator = serializeraw.create_pagetextnavigators_frompath(
        power.link(power.DOCU27_PDF))[0]
    result = texmex.group_page_by_size_distance(navigator)
    assert len(result) == 4, str(result)


def test_group_pages_by_fontsize():
    navigators = serializeraw.create_pagetextnavigators_frompath(
        power.link(power.DOCU27_PDF))
    result = texmex.group_pages_by_fontsize(navigators)
    # remove empty page
    result = [item for item in result if item]
    assert len(result) == 10, str(result)


def test_multiline_unite_groups():
    content = [['A'], ['W'] * 16, ['C'], ['D'], ['E'], ['G']]
    index = [
        [0],
        [1, 2],
        [3, 4],
        [5, 6],
        [7, 8],
        [9, 10],
        [11, 12, 13],
        [14, 15],
        [16],
        [17],
        [18, 19],
        [20],
    ]
    expected = [
        ['A'],
        ['W', 'W'],
        ['W', 'W'],
        ['W', 'W'],
        ['W', 'W'],
        ['W', 'W'],
        ['W', 'W', 'W'],
        ['W', 'W'],
        ['W'],
        ['C'],
        ['G'],
    ]
    united = texmex.unite_groups(content, index)
    assert united == expected
