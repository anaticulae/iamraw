# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import pytest

import iamraw


@pytest.mark.parametrize('location, expected', [
    ('p10', iamraw.Location(page=10, shortcut='p')),
    ('w100p13', iamraw.Location(page=13, shortcut='w', value=100)),
    ('sec3p5', iamraw.Location(page=5, shortcut='sec', value=3)),
])
def test_finding_location_fromstr(location, expected):
    created = iamraw.Location.fromstr(location)
    assert created == expected


@pytest.mark.parametrize('location', [
    iamraw.Location(page=10, shortcut='p'),
    iamraw.Location(page=13, shortcut='w', value=100),
    iamraw.Location(page=5, shortcut='sec', value=3),
])
def test_finding_location_fromstr_raw(location):
    raw = location.raw()
    assert raw

    parsed = iamraw.Location.fromstr(raw)
    assert parsed == location, str(parsed)


@pytest.mark.parametrize('raw', [
    'notworking',
    '',
])
def test_finding_location_fromstr_raw_none(raw):
    constructed = iamraw.Location.fromstr(raw)
    assert constructed is None, constructed


def test_finding_hashing_location():
    location = iamraw.Location.fromstr('p10')
    hashed = hash(location)
    assert hashed


def test_finding_location_from_ctor():
    page12 = iamraw.Location(page=12, shortcut='p')
    page12ctor = iamraw.Location.from_page(12)
    assert page12ctor == page12, str(page12ctor)

    chapter4page20 = iamraw.Location(page=20, shortcut='c', value=4)
    chapter4page20ctor = iamraw.Location.from_chapter(chapter=4, page=20)
    assert chapter4page20ctor == chapter4page20, str(chapter4page20ctor)

    oneline1page5 = iamraw.Location(page=5, shortcut='ol', value=1)
    oneline1page5ctor = iamraw.Location.from_oneline(line=1, page=5)
    assert oneline1page5ctor == oneline1page5, str(oneline1page5ctor)


@pytest.mark.parametrize('location, expected', [
    ('p10_12~l6_9~t5_19', iamraw.RangedLocation(10, 12, 6, 9, 5, 19)),
    ('p10_12~l6~t5', iamraw.RangedLocation(10, 12, line=6, token=5)),
    ('p10~l6', iamraw.RangedLocation(page=10, line=6)),
    ('p5', iamraw.RangedLocation(page=5)),
    ('p5~t17', iamraw.RangedLocation(page=5, token=17)),
])
def test_finding_rangedlocation_fromstr(location, expected):
    location = iamraw.RangedLocation.fromstr(location)
    assert location == expected


@pytest.mark.parametrize('location', [
    'p10_12~l6_9~t5_19',
    'p10_12~l6~t5',
    'p10~l6',
    'p5',
])
def test_finding_rangedlocation_str_obj_str(location):
    parsed = iamraw.RangedLocation.fromstr(location)
    tostring = parsed.raw()
    assert tostring == location
