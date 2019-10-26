# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

from functools import lru_cache

import utila
from configo import CACHE_SMALL
from utila import error
from utila import from_raw_or_path
from utila import should_skip
from yaml import FullLoader
from yaml import dump
from yaml import load

from iamraw import Char
from iamraw import Document
from iamraw import Line
from iamraw import Page
from iamraw import PageObject
from iamraw import TextContainer
from iamraw import VirtualChar
from serializeraw.border import size_fromraw
from serializeraw.border import size_toraw


def _load_pageobject(content: str):
    return PageObject(content=content)


def _dump_pageobject(pageobject: PageObject):
    return [str(PageObject.__name__), pageobject.content]


def _load_page(content):
    pagenumber = content['page']
    children = content['children']

    page = Page(pagenumber)
    for class_, item_content in children:
        if class_ == TextContainer.__name__:
            page.children.append(loadme(TextContainer, item_content))  # pylint:disable=E1101

        if class_ == PageObject.__name__:
            page.children.append(loadme(PageObject, item_content))  # pylint:disable=E1101
    return page


def _dump_page(page: Page):
    result = {
        'page': page.page,
        'children': [dumper(item) for item in page.children],
    }
    return result


def _dump_line(line: Line) -> str:
    assert len(line) >= 1

    def create_style(start, end, size, rise):
        style = ' '.join([
            f'{start}',
            f'{end}',
            '%.2f' % size if size is not None else 'None',
            '%.2f' % rise if rise is not None else 'None',
        ])
        return style

    styles = []
    start, cursize, currise = 0, line[0].size, line[0].rise
    for end, character in enumerate(line[1:], 1):
        if isinstance(character, VirtualChar):
            continue
        if cursize != character.size or currise != character.rise:
            styles.append(create_style(
                start,
                end,
                cursize,
                currise,
            ))
            start, cursize, currise = end, character.size, character.rise
    if start != len(line):
        styles.append(create_style(
            start,
            len(line),
            cursize,
            currise,
        ))
    content = ''.join([item.value for item in line])

    return [
        content,
        styles,
    ]  # use list for a more human readable format


def _load_line(line) -> Line:
    assert len(line) == 2, line

    data, styles = line
    chars = []
    for style in styles:
        start, end, size, rise = style.split()
        start, end = int(start), int(end)
        if size == 'None':
            size = None
        if rise == 'None':
            rise = None

        for index in range(start, end):
            # TODO: Unicodechar?
            char = Char(
                value=data[index],
                size=float(size) if size is not None else None,
                rise=float(rise) if rise is not None else None,
            )
            chars.append(char)
    return Line(chars=chars)


def _dump_textcontainer(container: TextContainer):
    assert isinstance(container, TextContainer)
    return [
        container.__class__.__name__,
        [_dump_line(line) for line in container.lines],
    ]  # use list for a more human readable format


def _load_textcontainer(content) -> TextContainer:
    assert isinstance(content, list), type(content)
    assert all([isinstance(item, list) for item in content]), str(content)
    lines = [loadme(Line, item) for item in content]
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


def dump_document(document: Document) -> str:
    """Convert to raw python to have more clear yaml output"""
    assert isinstance(document, Document), type(document)
    raw = dumper(document)
    return dump(raw)


@lru_cache(CACHE_SMALL)
def load_document(content: str, pages=None) -> Document:
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

    def remove_skipped(loaded, pages):
        """Remove pages which are not part of todo list `pages`"""
        to_process = []
        for item in loaded['pages']:
            pagenumber = int(item['page'])
            if should_skip(pagenumber, pages):
                continue
            to_process.append(item)
        loaded['pages'] = to_process
        return loaded

    loaded = remove_skipped(loaded, pages)

    return loadme(Document, loaded)


def dumper(content):
    key = content.__class__.__name__
    try:
        dumpy, _ = DUMP_LOAD[key]
    except KeyError as msg:
        error('Could not dump: %s' % msg)
        return None
    else:
        return dumpy(content)


def loadme(structure, data):
    try:
        _, loady = DUMP_LOAD[structure.__name__]
    except KeyError as msg:
        error('Could not load: %s' % msg)
        return None
    else:
        return loady(data)


DUMP_LOAD = {
    Document.__name__: (_dump_document, _load_document),
    Line.__name__: (_dump_line, _load_line),
    Page.__name__: (_dump_page, _load_page),
    TextContainer.__name__: (_dump_textcontainer, _load_textcontainer),
    PageObject.__name__: (_dump_pageobject, _load_pageobject),
}
