# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================
import functools

import configo
import utila
import yaml

import iamraw
from serializeraw.border import size_fromraw
from serializeraw.border import size_toraw


def dump_document(document: iamraw.Document) -> str:
    """Convert to raw python to have more clear yaml output"""
    assert isinstance(document, iamraw.Document), type(document)
    raw = dumper(document)
    return yaml.dump(raw)


@functools.lru_cache(configo.CACHE_SMALL)
def load_document(content: str, pages: tuple = None) -> iamraw.Document:
    """Load document from raw-string or filepath.

    If document is loaded from file-path, the content is loaded and parsed
    afterwards as raw-string.

    Args:
        content(str): raw-string or file-path
        pages(tuple): select pages to process
    Returns:
        parsed Document
    Raises:
        ValueError if given path does not exists
    """
    content = utila.from_raw_or_path(
        content,
        fname='rawmaker__text_text',
        ftype='yaml',
    )
    loaded = yaml.load(content, Loader=yaml.FullLoader)

    def remove_skipped(loaded, pages):
        """Remove pages which are not part of todo list `pages`"""
        to_process = []
        for item in loaded['pages']:
            pagenumber = int(item['page'])
            if utila.should_skip(pagenumber, pages):
                continue
            to_process.append(item)
        loaded['pages'] = to_process
        return loaded

    loaded = remove_skipped(loaded, pages)

    return loadme(iamraw.Document, loaded)


def _load_pageobject(content: str):
    return iamraw.PageObject(content=content)


def _dump_pageobject(pageobject: iamraw.PageObject):
    return [str(iamraw.PageObject.__name__), pageobject.content]


def _load_page(content):
    pagenumber = content['page']
    children = content['children']

    page = iamraw.Page(pagenumber)
    for class_, item_content in children:
        if class_ == iamraw.TextContainer.__name__:
            loaded = loadme(iamraw.TextContainer, item_content)
            page.append(loaded)

        if class_ == iamraw.PageObject.__name__:
            loaded = loadme(iamraw.PageObject, item_content)
            page.append(loaded)
    return page


def _dump_page(page: iamraw.Page):
    result = {
        'page': page.page,
        'children': [dumper(item) for item in page],
    }
    return result


def _dump_line(line: iamraw.Line) -> str:
    assert len(line) >= 1, line

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
        if isinstance(character, iamraw.VirtualChar):
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


def _load_line(line) -> iamraw.Line:
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
            char = iamraw.Char(
                value=data[index],
                size=float(size) if size is not None else None,
                rise=float(rise) if rise is not None else None,
            )
            chars.append(char)
    return iamraw.Line(chars=chars)


def _dump_textcontainer(container: iamraw.TextContainer):
    assert isinstance(container, iamraw.TextContainer)
    return [
        container.__class__.__name__,
        [_dump_line(line) for line in container.lines],
    ]  # use list for a more human readable format


def _load_textcontainer(content) -> iamraw.TextContainer:
    assert isinstance(content, list), type(content)
    assert all([isinstance(item, list) for item in content]), str(content)
    lines = [loadme(iamraw.Line, item) for item in content]
    return iamraw.TextContainer(lines=lines)


def _load_document(content):
    dimension = size_fromraw(content['dimension'])
    pages = [loadme(iamraw.Page, item) for item in content['pages']]
    result = iamraw.Document(dimension=dimension, pages=pages)
    return result


def _dump_document(document: iamraw.Document) -> dict:
    assert document
    assert document.dimension, str(document.dimension)
    result = {
        'dimension': size_toraw(document.dimension),
        'pages': [dumper(item) for item in document.pages],
    }
    return result


def dumper(content):
    key = content.__class__.__name__
    try:
        dumpy, _ = DUMP_LOAD[key]
    except KeyError as msg:
        utila.error('Could not dump: %s' % msg)
        return None
    else:
        return dumpy(content)


def loadme(structure, data):
    try:
        _, loady = DUMP_LOAD[structure.__name__]
    except KeyError as msg:
        utila.error('Could not load: %s' % msg)
        return None
    else:
        return loady(data)


DUMP_LOAD = {
    iamraw.Document.__name__: (_dump_document, _load_document),
    iamraw.Line.__name__: (_dump_line, _load_line),
    iamraw.Page.__name__: (_dump_page, _load_page),
    iamraw.TextContainer.__name__: (_dump_textcontainer, _load_textcontainer),
    iamraw.PageObject.__name__: (_dump_pageobject, _load_pageobject),
}
