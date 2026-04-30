# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

# TODO: RENAME LATER

import hoverpower
import pytest
import utilo
import utilotest

import serializeraw
import texmex

NO_GROUP = [[18], [31], [29], [35]]  # number of items per page


def example():
    utilotest.fixture_requires(hoverpower.MASTER072_PDF)
    source = hoverpower.link(hoverpower.MASTER072_PDF)
    pages = utilo.rtuple(5, 9)
    navigators = serializeraw.create_pagetextnavigators_frompath(
        source,
        pages=pages,
    )
    return navigators


@pytest.mark.xfail(reason='grouping is too soft')
def test_multiline_group_page_no_group():
    navigators = example()
    grouped = texmex.group_pages_by_fontsize(navigators)
    grouped = [texmex.groupby_linedistance(item) for item in grouped]

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
        utilo.rlist(30),
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
        sizediff_max=0.0,
        distance_max=lambda x: 0.0,
    )
    assert len(grouped) == 18


@utilotest.requires(hoverpower.DOCU007_PDF)
def test_merge_content():  # pylint:disable=W0621
    navigator = serializeraw.create_pagetextnavigators_frompath(
        hoverpower.link(hoverpower.DOCU007_PDF))
    navigator = utilo.select_page(navigator, page=1)
    content = texmex.navigator_to_content(navigator)
    merged, _ = texmex.merge_content(content)
    merged = texmex.merge_content_join(merged)

    content = texmex.navigator_to_content(navigator)
    merged, _ = texmex.merge_content(content)  # split content and merge_ids
    # NOTE: Dependens on `MAX_MERGE_DISTANCE`, not a good test?
    #     paragraph_after_merge = 8
    #     assert len(merged) == paragraph_after_merge
    merged_content = texmex.merge_content_join(merged)

    expectend_content = utilo.NEWLINE.join([item.text for item in content])
    merged_content = utilo.NEWLINE.join([item.text for item in merged_content])

    assert merged_content == expectend_content
    content_count = len(expectend_content)
    merged_count = len(merged_content)
    # ensure that no data is lost while merging
    assert content_count == merged_count


@utilotest.requires(hoverpower.BACHELOR111_PDF)
def test_create_pagetextcontent_navigator_frompath():
    loaded = serializeraw.create_pagetextcontentnavigators_frompath(
        hoverpower.link(hoverpower.BACHELOR111_PDF),
        pages=(1, 2, 3, 4),
        prefix='oneline',
    )
    first = loaded[0]
    lasttext = first[-1].text
    # no newline at end
    assert lasttext == 'i', lasttext
