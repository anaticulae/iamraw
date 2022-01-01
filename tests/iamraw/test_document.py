# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

from pytest import fixture

from iamraw.document import Char
from iamraw.document import Document
from iamraw.document import Line
from iamraw.document import Page
from iamraw.document import TextContainer


@fixture
def textcontainer() -> TextContainer:
    container = TextContainer()
    for line in ['First\n', 'Second\n', 'Thrid Third Third\n']:
        container.append(Line(chars=[Char(value=item) for item in line]))
    return container


@fixture
def page(textcontainer) -> Page:  # pylint:disable=W0621
    result = Page()
    result.append(textcontainer)
    result.append(textcontainer)
    result.append(textcontainer)
    return result


def test_page_text(page: Page):  # pylint:disable=W0621
    content = page.text
    assert len(content.splitlines()) == 9


def test_textcontainer_iter(textcontainer: TextContainer):  # pylint:disable=W0621
    assert len(textcontainer) == 3
    assert len(textcontainer.text.splitlines()) == len(textcontainer)


def test_textcontainer_loop(textcontainer: TextContainer):  # pylint:disable=W0621
    for item in textcontainer:
        assert item


def test_document_text(page: Page):  # pylint:disable=W0621
    document: Document = Document(pages=[page])
    assert len(document) == 1
    assert document.text
