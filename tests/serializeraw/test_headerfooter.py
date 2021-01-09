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
import serializeraw
import tests.serializeraw.examples.footnotes
import tests.serializeraw.examples.headerfooter


def test_footnotes_dump_and_load():
    notes = tests.serializeraw.examples.footnotes.FOOTNOTES

    for note in notes:
        dumped = serializeraw.dump_footnote(note)
        loaded = serializeraw.load_footnote(dumped)
        assert loaded == note


@pytest.mark.parametrize('example', [
    tests.serializeraw.examples.headerfooter.FOOTER_HEADER,
    tests.serializeraw.examples.headerfooter.SECOND,
    tests.serializeraw.examples.headerfooter.THIRD,
    tests.serializeraw.examples.headerfooter.FOURTH,
])
def test_footerheader_dump_and_load(example):
    dumped = serializeraw.dump_headerfooter(example)
    loaded = serializeraw.load_headerfooter(dumped)
    assert example == loaded


def test_footerheader_dump_invalid_list():
    duplication = []
    duplication.extend(tests.serializeraw.examples.headerfooter.FOOTER_HEADER)
    duplication.extend(tests.serializeraw.examples.headerfooter.FOOTER_HEADER)

    with pytest.raises(ValueError):
        serializeraw.dump_headerfooter(duplication)


def test_footerheader_movingfooterinformation():
    footer = iamraw.MovingFooterInformation()
    note = iamraw.FootRawNote(number=1, text='hello', raw='1 hello')
    assert not footer
    footer.append(note)
    assert len(footer) == 1
    assert footer[0] == note


def test_footerheader_footer_extend():
    footer = iamraw.MovingFooterInformation()
    footer.extend(begin=0.2)
    assert footer.begin == 0.2
    footer.extend(begin=0.3)
    assert footer.begin == 0.2

    footer.extend(end=0.2)
    assert footer.begin == 0.2
    footer.extend(end=0.3)
    assert footer.begin == 0.2


def test_footerheader_header_extend():
    header = iamraw.HeaderInformation()
    header.extend(begin=0.2)
    assert header.begin == 0.2
    header.extend(begin=0.3)
    assert header.begin == 0.2

    header.extend(end=0.2)
    assert header.begin == 0.2
    header.extend(end=0.3)
    assert header.end == 0.3
    header.extend(end=0.2)
    assert header.end == 0.3
    header.extend(end=0.5)
    assert header.end == 0.5
    assert header.begin == 0.2


def test_footerheader_footer_dump():
    footer = iamraw.PagesFooterInformation(
        page_location=iamraw.BoundingBox(10, 20, 50, 60),
        page=iamraw.PageInformation(
            value=1,
            raw='-1-',
        ))
    footers = [
        iamraw.PageContentFooterHeader(
            header=None,
            footer=footer,
            page=1,
        )
    ]
    dumped = serializeraw.dump_headerfooter(footers)
    assert '!!python/object' not in dumped, 'we do not want yaml-bib here'
    loaded = serializeraw.load_headerfooter(dumped)
    assert loaded == footers, loaded
