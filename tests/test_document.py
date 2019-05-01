# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019 by Helmut Konrad Fahrendholz. All rights reserved.
# Tis file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

from pytest import fixture
from utila import NEWLINE

from iamraw.document.document import Document
from iamraw.document.page import Char
from iamraw.document.page import Line
from iamraw.document.page import Page
from iamraw.document.page import TextContainer


def line_from_str(line: str) -> Line:
    # Line must ends with NEWLINE
    if not line[-1] == NEWLINE:
        line += NEWLINE
    chars = [Char(value=item) for item in line]
    return Line(chars=chars)


@fixture
def textcontainer() -> TextContainer:
    container: TextContainer = TextContainer()
    append = container.lines.append
    append(line_from_str('First'))
    append(line_from_str('Second'))
    append(line_from_str('Third Third Third'))
    return container


@fixture
def page(textcontainer) -> Page:
    page: Page = Page()
    append = page.children.append
    append(textcontainer)
    append(textcontainer)
    append(textcontainer)
    return page


def test_page_text(page: Page):
    content = page.text
    assert len(content.splitlines()) == 9


def test_textcontainer_iter(textcontainer: TextContainer):
    assert len(textcontainer) == 3
    assert len(textcontainer.text.splitlines()) == len(textcontainer)


def test_textcontainer_loop(textcontainer: TextContainer):
    for item in textcontainer:
        assert item


def test_document_text(page: Page):
    document: Document = Document(pages=[page])
    assert document.page_count == 1
    assert document.text
