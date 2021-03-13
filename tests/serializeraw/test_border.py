# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utila
from pytest import mark

import serializeraw
from iamraw import Border
from iamraw import PageSize
from iamraw.border import validate
from serializeraw import dump_pageborders
from serializeraw import load_pageborders
from serializeraw.border import border_fromraw
from serializeraw.border import border_toraw
from serializeraw.border import size_fromraw
from serializeraw.border import size_toraw


def test_border_work(boxdata_from_pdf):
    assert len(boxdata_from_pdf) == 2


def test_border_dump_and_load_pageborder(boxdata_from_pdf):
    sizeandborders, _ = boxdata_from_pdf

    dumped = dump_pageborders(sizeandborders)

    loaded_sizeandborders = load_pageborders(dumped)
    assert loaded_sizeandborders == sizeandborders

    loaded_sizeandborders = load_pageborders(dumped, pages=(1, 2, 3))
    assert len(loaded_sizeandborders) == 3


@mark.parametrize('size', [
    PageSize(10.5, 5.0),
    PageSize(1, 1),
    PageSize(None, None),
])
def test_convert_size(size):
    raw = size_toraw(size)
    assert size_fromraw(raw) == size


@mark.parametrize('border', [
    Border(1, 2, 3, 4),
    Border(None, None, None, None),
])
def test_convert_border(border):
    raw = border_toraw(border)
    assert border_fromraw(raw) == border


def test_border_validate_border_and_pages(boxdata_from_pdf):
    sizeandborder, _ = boxdata_from_pdf

    size = [item.size for item in sizeandborder]
    border = [item.border for item in sizeandborder]

    valid_size = validate(size)
    valid_border = validate(border)

    invalid_border = Border(-1, 0, 100, 200)
    valid = validate(invalid_border)

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
