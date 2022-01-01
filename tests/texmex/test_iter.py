# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import pytest
import utila

import tests.texmex.example.restructured
import texmex


@pytest.mark.parametrize('page,position,expected', [
    (0, [
        (0, 2, 0),
        (1, 1, 0),
        (2, 2, 0),
    ], [
        'The RestructuredText Book\nDocumentation\n',
        'Release 0.1\n',
        'Daniel Greenfeld, Eric Holscher\nSep 27, 2017\n',
    ]),
    (2, [
        (0, 0, 5),
        (1, 1, 0),
        (1, 2, 0),
    ], [
        'Cont',
        'ents\n1 RestructuredText Tutorial 3\n',
        '2 RestructuredText Guide 5\n',
    ]),
])
def test_split_page(page, position, expected):
    """Verify the behavior of the `TextIter` which is produced by `split_range`.

    It is not possible to access elements before the
    iterator. To access elements before iterator, rewinding the iterator
    is nessacary."""
    example = tests.texmex.example.restructured.document()
    current = utila.select_page(example, page)
    result = texmex.split_page(current, position, append_unvisited=False)

    assert result == expected
