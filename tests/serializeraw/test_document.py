# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import power

from iamraw import Char
from iamraw import Document
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


def simple_textcontainer():
    container = TextContainer()
    for line in [
            'I am a beautiful Line\n',
            'I am a more beautiful Line\n',
            'I am a the most beautiful Line\n',
    ]:
        container.append(Line(chars=[Char(value=item) for item in line]))
    return container


def simple_page():
    page = Page()
    assert page.empty()
    page.append(simple_textcontainer())
    page.append(simple_textcontainer())
    page.append(simple_textcontainer())
    assert len(page) == 3
    return page


def simple_document():
    document = Document()
    document.append(simple_page())
    document.append(simple_page())
    assert len(document) == 2
    return document


def test_load_document_from_path():
    document = load_document(power.link(power.DOCU07_PDF))
    assert document

    document = load_document(power.link(power.DOCU07_PDF), (1, 2))
    assert len(document) == 2


def test_load_dump_load_document():
    document = load_document(power.link(power.DOCU07_PDF))

    dumped = dump_document(document)
    second_load = load_document(dumped)

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


def test_dump_and_load_textcontainer():
    container = simple_textcontainer()
    _, dumped = _dump_textcontainer(container)
    loaded = _load_textcontainer(dumped)

    assert loaded == container


def test_document_dump_and_load_page():
    expected = simple_page()
    dumped = _dump_page(expected)
    loaded = _load_page(dumped)

    assert loaded.text == expected.text

    for current, required in zip(loaded, expected):
        assert current == required

    assert len(loaded) == len(expected)
    assert loaded.children == expected.children
    assert loaded == expected


def test_document_page_repr():
    """Ensure that repr works."""
    page = Page()
    raw = str(page)
    assert 'page=0' in raw, raw


def test_document_document_repr():
    document = simple_document()
    raw = str(document)
    assert 'Document: pages=2' in raw, raw
