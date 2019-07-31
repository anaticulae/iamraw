# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

from functools import lru_cache

from configo import CACHE_SMALL
from utila import error
from utila import from_raw_or_path
from yaml import FullLoader
from yaml import dump
from yaml import load

from iamraw import Char
from iamraw import Document
from iamraw import Line
from iamraw import Page
from iamraw import PageObject
from iamraw import TextContainer
from serializeraw.border import size_fromraw
from serializeraw.border import size_toraw


def _load_pageobject(content: str):
    return PageObject(content=content)


def _dump_pageobject(pageobject: PageObject):
    return [str(PageObject.__name__), pageobject.content]


def _load_char(value) -> Char:
    return Char(value=value)


def _dump_char(value: Char) -> str:
    return value.value


def _load_page(content):
    number = content['number']
    children = content['children']

    page = Page(number)
    for class_, item_content in children:

        if class_ == TextContainer.__name__:
            page.children.append(loadme(TextContainer, item_content))

        if class_ == PageObject.__name__:
            page.children.append(loadme(PageObject, item_content))
    return page


def _dump_page(page: Page):
    result = {
        'number': page.number,
        'children': [dumper(item) for item in page.children],
    }
    return result


def _dump_line(line: Line) -> str:
    return [Line.__class__.__name__, line.text]


def _load_line(line: str) -> Line:
    chars = []
    for char in line:
        chars.append(_load_char(value=char))
    return Line(chars=chars)


def _dump_textcontainer(container: TextContainer):
    return [
        str(container.__class__.__name__),
        [item.text for item in container.lines]
    ]


def _load_textcontainer(content) -> TextContainer:
    lines = [_load_line(item) for item in content]
    return TextContainer(lines=lines)


def _load_document(content):
    dimension = size_fromraw(content['dimension'])
    pages = [loadme(Page, item) for item in content['pages']]
    result = Document(dimension=dimension, pages=pages)
    return result


def _dump_document(document: Document) -> dict:
    assert document
    assert document.dimension, str(document.dimension)
    result = {
        'dimension': size_toraw(document.dimension),
        'pages': [dumper(item) for item in document.pages],
    }
    return result


def dump_yaml(document: Document) -> str:
    """Convert to raw python to have more clear yaml output"""
    assert isinstance(document, Document), type(document)
    raw = dumper(document)
    return dump(raw)


@lru_cache(CACHE_SMALL)
def load_yaml(content: str) -> Document:
    """Load document from raw-string or filepath.

    If document is loaded from file-path, the content is loaded and parsed
    afterwards as raw-string.

    Args:
        content(str): raw-string or file-path
    Returns:
        parsed Document
    Raises:
        ValueError if given path does not exists
    """
    content = from_raw_or_path(content, ftype='yaml')
    loaded = load(content, Loader=FullLoader)
    return loadme(Document, loaded)


def dumper(content):
    key = content.__class__.__name__
    try:
        dumpy, _ = DUMP_LOAD[key]
    except KeyError as error:
        error('Could not dump %s' % error)
        return None
    else:
        return dumpy(content)


def loadme(structure, data):
    try:
        _, loady = DUMP_LOAD[structure.__name__]
    except KeyError as error:
        error('Could not load %s' % error)
        return None
    else:
        return loady(data)


DUMP_LOAD = {
    Char.__name__: (_dump_char, _load_char),
    Document.__name__: (_dump_document, _load_document),
    Line.__name__: (_dump_line, _load_line),
    Page.__name__: (_dump_page, _load_page),
    TextContainer.__name__: (_dump_textcontainer, _load_textcontainer),
    PageObject.__name__: (_dump_pageobject, _load_pageobject),
}
