# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import pytest

import iamraw
import iamraw.border
import serializeraw
import serializeraw.border


def test_border_work(boxdata_from_pdf):
    assert len(boxdata_from_pdf) == 2


def test_border_dump_and_load_pageborder(boxdata_from_pdf):
    sizeandborders, _ = boxdata_from_pdf

    dumped = serializeraw.dump_pageborders(sizeandborders)

    loaded_sizeandborders = serializeraw.load_pageborders(dumped)
    assert loaded_sizeandborders == sizeandborders

    loaded_sizeandborders = serializeraw.load_pageborders(dumped,
                                                          pages=(1, 2, 3))
    assert len(loaded_sizeandborders) == 3


@pytest.mark.parametrize('size', [
    iamraw.PageSize(10.5, 5.0),
    iamraw.PageSize(1, 1),
    iamraw.PageSize(None, None),
])
def test_convert_size(size):
    raw = serializeraw.border.size_toraw(size)
    assert serializeraw.border.size_fromraw(raw) == size


@pytest.mark.parametrize('border', [
    iamraw.Border(1, 2, 3, 4),
    iamraw.Border(None, None, None, None),
])
def test_convert_border(border):
    raw = serializeraw.border.border_toraw(border)
    assert serializeraw.border.border_fromraw(raw) == border


def test_border_validate_border_and_pages(boxdata_from_pdf):
    sizeandborder, _ = boxdata_from_pdf

    size = [item.size for item in sizeandborder]
    border = [item.border for item in sizeandborder]

    valid_size = iamraw.border.validate(size)
    valid_border = iamraw.border.validate(border)

    invalid_border = iamraw.Border(-1, 0, 100, 200)
    valid = iamraw.border.validate(invalid_border)

    assert valid_size
    assert valid_border
    assert not valid


def test_dump_load_leftright_border():
    borders = [
        (0, 10, 10, 20, 20),
        (2, 0, 0, 50, 50),
        (3, 0, 0, 50, 50),
        (2, -15, -15, 50, 50),
    ]
    expected = {page: tuple(border) for page, *border in borders}
    dumped = serializeraw.dump_leftright_border(borders)
    loaded = serializeraw.load_leftright_border(dumped)
    assert loaded == expected
