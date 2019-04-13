# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019 by Helmut Konrad Fahrendholz. All rights reserved.
# Tis file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

from pytest import fixture
from tests.serializeraw import TEXT_YAML

from iamraw import Char
from iamraw import Line
from iamraw import Page
from iamraw import TextContainer

from serializeraw import dump_document
from serializeraw import load_document
from serializeraw.text import _dump_line
from serializeraw.text import _dump_page
from serializeraw.text import _dump_textcontainer
from serializeraw.text import _load_line
from serializeraw.text import _load_page
from serializeraw.text import _load_textcontainer


def test_load_document_from_path():
    document = load_document(TEXT_YAML)
    assert document


def test_load_dump_load_document():
    document = load_document(TEXT_YAML)

    dupmed = dump_document(document)

    second_load = load_document(dupmed)
    assert document
    assert second_load == document


def test_load_and_dump_line():
    text = 'I am a Line'

    loaded = _load_line(text)
    assert len(loaded.chars) == len(text)

    dumped = _dump_line(loaded)
    assert dumped[1] == text


def line_from_str(line: str) -> Line:
    result = Line()
    result.chars = [Char(value=item) for item in line]
    return result


@fixture
def simple_textcontainer():
    container = TextContainer()
    container.lines.append(line_from_str('I am a beautiful Line'))
    container.lines.append(line_from_str('I am a more beautiful Line'))
    container.lines.append(line_from_str('I am a the most beautiful Line'))
    return container


@fixture
def simple_page(simple_textcontainer):
    page = Page()

    page.children.append(simple_textcontainer)
    page.children.append(simple_textcontainer)
    page.children.append(simple_textcontainer)

    return page


def test_dump_and_load_textcontainer(simple_textcontainer):
    container = simple_textcontainer

    _, dumped = _dump_textcontainer(container)

    loaded = _load_textcontainer(dumped)

    assert loaded == container


def test_dump_and_load_page(simple_page):
    dumped = _dump_page(simple_page)
    loaded = _load_page(dumped)

    assert loaded == simple_page
