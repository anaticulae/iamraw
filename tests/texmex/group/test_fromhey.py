# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

# TODO: RENAME LATER

import power
import pytest
import utila
import utilatest

import serializeraw
import texmex

NO_GROUP = [[18], [31], [29], [35]]  # number of items per page


def example():
    utilatest.fixture_requires(power.MASTER072_PDF)
    source = power.link(power.MASTER072_PDF)
    pages = utila.rtuple(5, 9)
    navigators = serializeraw.create_pagetextnavigators_frompath(
        source,
        pages=pages,
    )
    return navigators


@pytest.mark.xfail(reason='grouping is too soft')
def test_multiline_group_page_no_group():
    navigators = example()
    grouped = texmex.group_pages_by_fontsize(navigators)
    grouped = [texmex.group_by_linedistance(item) for item in grouped]

    count = [[len(item) for item in items] for items in grouped]
    assert count == NO_GROUP


def test_multiline_group_page_by_fontsize():
    navigators = example()
    grouped = texmex.group_pages_by_fontsize(navigators)
    count = [[len(item) for item in items] for items in grouped]
    expected = [
        [1, 16, 1],  # page 5, 3 MultilineGroups with `text` content
        [3, 7, 2, 13, 5, 1],
        [26, 2, 1],
        [30, 4, 1],  # page 8
    ]
    assert count == expected


def test_multiline_group_page_by_maxdistance():
    navigators = example()
    grouped = texmex.group_pages_by_fontsize(navigators)
    count = [[len(item) for item in items] for items in grouped]
    expected = [
        [1, 16, 1],  # page 5, 3 MultilineGroups with `text` content
        [3, 7, 2, 13, 5, 1],
        [26, 2, 1],
        [30, 4, 1],  # page 8
    ]
    assert count == expected


@pytest.mark.parametrize('page, expected', [
    (0, [
        [0],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
        [17],
    ]),
    (1, [
        [0, 1, 2],
        [3, 4, 5, 6, 7, 8, 9],
        [10, 11],
        [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],
        [25, 26, 27, 28, 29],
        [30],
    ]),
    (2, [
        [0, 1],
        [2, 3, 4, 5],
        [6, 7, 8],
        [9, 10],
        [11, 12, 13],
        [14, 15, 16],
        [17, 18],
        [19, 20, 21],
        [22, 23, 24, 25],
        [26, 27],
        [28],
    ]),
    (3, [
        utila.rlist(30),
        [30, 31, 32, 33],
        [34],
    ]),
])
def test_multiline_group_linedistances_page(page, expected):
    navigators = example()
    content = navigators[page]
    grouped = texmex.group_linedistances_complex(content)
    assert grouped == expected


def test_multiline_group_linedistances_page_zero_tolerance():
    navigators = example()
    content = navigators[0]
    grouped = texmex.group_linedistances_complex(
        content,
        max_sizediff=0.0,
        max_distance=lambda x: 0.0,
    )
    assert len(grouped) == 18


def test_merge_content():  # pylint:disable=W0621
    navigator = serializeraw.create_pagetextnavigators_frompath(
        power.link(power.DOCU007_PDF))
    navigator = utila.select_page(navigator, page=1)
    content = texmex.navigator_to_content(navigator)
    merged, _ = texmex.merge_content(content)
    merged = texmex.merge_content_join(merged)

    content = texmex.navigator_to_content(navigator)
    merged, _ = texmex.merge_content(content)  # split content and merge_ids
    # NOTE: Dependens on `MAX_MERGE_DISTANCE`, not a good test?
    #     paragraph_after_merge = 8
    #     assert len(merged) == paragraph_after_merge
    merged_content = texmex.merge_content_join(merged)

    expectend_content = utila.NEWLINE.join([item.text for item in content])
    merged_content = utila.NEWLINE.join([item.text for item in merged_content])

    assert merged_content == expectend_content
    content_count = len(expectend_content)
    merged_count = len(merged_content)
    # ensure that no data is lost while merging
    assert content_count == merged_count


def test_create_pagetextcontent_navigator_frompath():
    loaded = serializeraw.create_pagetextcontentnavigators_frompath(
        power.link(power.BACHELOR111_PDF),
        pages=(1, 2, 3, 4),
        prefix='oneline',
    )
    first = loaded[0]
    lasttext = first[-1].text
    assert lasttext != 'i', lasttext
