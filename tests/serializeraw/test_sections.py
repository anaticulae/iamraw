# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import iamraw
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


def example():

    class New(iamraw.AreaItem):
        pass

    class Wrapped(iamraw.AreaItem):
        pass

    def wrapper(name: str):
        if name == 'Wrapped':
            return Wrapped
        if name == 'New':
            return New
        return None

    section = iamraw.Sections()
    first = iamraw.DocumentSection(start=0, end=1)
    section.append(first)
    # TODO: SUPPORT FLOATING PAGE NUMBER
    # first.append(New(0, 1.0, trust=1.0))
    first.append(New(0, 1, trust=1.0))
    first.append(Wrapped(1, 2, trust=1.0))
    return section, wrapper


def test_dump_and_load_sections_notimplemented():
    section, _ = example()
    dumped = dump_sections(section)
    assert dumped, str(dumped)
    # do not use `replacement` loader, use default NotImplementedItem
    loaded = load_sections(dumped, onerror=None)
    assert len(loaded) == len(section), str(loaded)


def test_dump_and_load_sections_onerror():
    section, wrapper = example()
    dumped = dump_sections(section)
    assert dumped, str(dumped)
    loaded = load_sections(dumped, onerror=wrapper)
    assert loaded == section, str(loaded)
