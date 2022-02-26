# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import power
import pytest
import utila
import utilatest

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
    assert '!!python/object' not in dumped, 'we do not want yaml-bib here'
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
    note = iamraw.FootNoteRaw(number=1, text='hello', raw='1 hello')
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
        ),
    )
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


def test_dump_mergednote():
    data = iamraw.PageContentFooterHeader(
        header=None,
        footer=iamraw.MovingFooterInformation(
            begin=0.76,
            end=1.0,
            page=None,
            notes=[
                iamraw.FootNoteRaw(
                    number='3',
                    text='Eclipse ist eine Gemeinschaft die sich mit ',
                    raw='3Eclipse ist eine Gemeinschaft die sich mit ',
                ),
                iamraw.FootNoteRaw(
                    number='4',
                    text='Java Standard Edition',
                    raw='4Java Standard Edition',
                ),
                iamraw.FootNoteRaw(
                    number='5',
                    text='Software Development Kit',
                    raw='5Software Development Kit',
                )
            ],
        ),
        page=10,
    )
    before = hash(str(data))
    dumped = utila.simplify(data)
    assert dumped
    assert hash(str(data)) == before, 'data changed due simplify'


@utilatest.requires(power.MASTER072_PDF)
def test_footer_load():
    source = power.link(power.MASTER072_PDF)
    loaded = serializeraw.load_headerfooter(source)
    assert len(loaded) == 7  # seven pages


@utilatest.requires(power.MASTER072_PDF)
def test_footnotes_load():
    source = power.link(power.MASTER072_PDF)
    loaded = serializeraw.load_footnotes(source)
    assert len(loaded) == 5  # five footnotes
