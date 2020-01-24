# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

from pytest import fixture

from iamraw import Char
from iamraw import Line
from iamraw import Page
from iamraw import TextContainer
from serializeraw import dump_document
from serializeraw import load_document
from serializeraw.document import _dump_line
from serializeraw.document import _dump_page
from serializeraw.document import _dump_textcontainer
from serializeraw.document import _load_line
from serializeraw.document import _load_page
from serializeraw.document import _load_textcontainer
from tests.serializeraw import TEXT_YAML


def test_load_document_from_path():
    document = load_document(TEXT_YAML)
    assert document

    document = load_document(TEXT_YAML, (1, 2))
    assert len(document) == 2


def test_load_dump_load_document():
    document = load_document(TEXT_YAML)

    dupmed = dump_document(document)

    second_load = load_document(dupmed)
    assert document
    assert second_load == document


def test_load_and_dump_line():
    text = 'I am a Line'
    style = [f'0 {len(text)} 12.00 15.00']
    expected = [text, style]
    loaded = _load_line(expected)
    assert len(loaded.chars) == len(text)

    dumped = _dump_line(loaded)
    assert dumped == expected, dumped


def line_from_str(line: str) -> Line:
    result = Line()
    result.chars = [Char(value=item) for item in line]
    return result


@fixture
def simple_textcontainer():
    container = TextContainer()
    # pylint:disable=E1101
    container.lines.append(line_from_str('I am a beautiful Line'))
    container.lines.append(line_from_str('I am a more beautiful Line'))
    container.lines.append(line_from_str('I am a the most beautiful Line'))
    return container


# TODO: define regex which ignores:
# def simple_page(simple_textcontainer):  # pylint:disable=W0621
# in general


@fixture
def simple_page(simple_textcontainer):  # pylint:disable=W0621
    page = Page()
    assert page.empty()
    page.append(simple_textcontainer)
    page.append(simple_textcontainer)
    page.append(simple_textcontainer)
    assert len(page) == 3

    return page


def test_dump_and_load_textcontainer(simple_textcontainer):  # pylint:disable=W0621
    container = simple_textcontainer

    _, dumped = _dump_textcontainer(container)

    loaded = _load_textcontainer(dumped)

    assert loaded == container


def test_document_dump_and_load_page(simple_page):  # pylint:disable=W0621
    dumped = _dump_page(simple_page)
    loaded = _load_page(dumped)

    assert loaded.text == simple_page.text

    for current, expected in zip(loaded, simple_page):
        assert current == expected
    assert len(loaded) == len(simple_page)
    assert loaded.children == simple_page.children
    assert loaded == simple_page


def test_document_page_repr():
    """Ensure that repr works."""
    page = Page()
    raw = str(page)
    assert 'page=0' in raw, raw
