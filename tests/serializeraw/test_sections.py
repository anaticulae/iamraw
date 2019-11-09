# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

from serializeraw import dump_sections
from serializeraw import load_sections
# pylint:disable=W0611
from tests.serializeraw.examples.sections import restructured_sections_manual


def test_dump_and_load_sections(
        restructured_sections_manual,  # pylint:disable=W0621
):
    data = restructured_sections_manual
    dumped = dump_sections(data)
    assert dumped

    loaded = load_sections(dumped)
    assert loaded

    assert loaded == data


def test_dump_and_load_sections_pages(restructured_sections_manual):  # pylint:disable=W0621
    """Test loading some pages with shrinked section container"""
    data = restructured_sections_manual
    dumped = dump_sections(data)
    assert dumped

    loaded = load_sections(dumped, pages=(2, 3))
    document_section = loaded[0]
    assert document_section.start == 2
    assert document_section.end == 3
    assert document_section.content
