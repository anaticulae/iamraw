# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import functools

import configo
import utila

import iamraw
import serializeraw
import serializeraw.border
import texmex


def dump_document(document: iamraw.Document, fast: bool = True) -> str:
    """Convert to raw python to have more clear yaml output"""
    assert isinstance(document, iamraw.Document), type(document)
    raw = dumper(document)
    dumped = utila.yaml_dump(raw)
    if fast:
        dumped = serializeraw.dump_yamlpages(dumped)
    return dumped


@functools.lru_cache(configo.CACHE_SMALL)
def load_document(
    content: str,
    pages: tuple = None,
    fast: bool = True,
) -> iamraw.Document:
    """Load document from raw-string or filepath.

    If document is loaded from file-path, the content is loaded and parsed
    afterwards as raw-string.

    Args:
        content(str): raw-string or file-path
        pages(tuple): select pages to process
        fast(bool): use yamlpages
    Returns:
        parsed Document
    Raises:
        ValueError if given path does not exists
    """
    if fast:
        content = serializeraw.load_yamlpages(
            content,
            pages=pages,
            fname='rawmaker__text_text',
        )
    loaded = utila.yaml_load(
        content,
        fname='rawmaker__text_text',
    )

    def remove_skipped(loaded, pages):
        """Remove pages which are not part of todo list `pages`"""
        if not loaded['pages']:
            # if yamlpages selected no content, it is possible that
            # loaded['pages] is None.
            loaded['pages'] = []
            return loaded
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


CTOR = {
    item.__name__: item for item in (
        iamraw.PageObject,
        iamraw.TextContainer,
        iamraw.VerticalTextContainer,
    )
}
KEYS = set(CTOR.keys())


def _load_page(content: dict) -> iamraw.Page:
    pagenumber = content['page']
    childrens = content['children']
    dimension = content.get('dimension', None)
    if dimension:
        if len(dimension.split()) == 2:
            # TODO: REMOVE HACK AFTER CHANING BOUNDING BOX TO (width,
            # height)-tuple
            dimension = f'0 0 {dimension}'
        dimension = iamraw.BoundingBox.from_str(dimension)
    page = iamraw.Page(page=pagenumber, dimension=dimension)
    for children in childrens:
        state = None
        vertical = children[0] == 'VerticalTextContainer'
        if vertical:
            classname, item_content = 'VerticalTextContainer', children[1]
        else:
            classname = iamraw.TextContainer.__name__
        if len(children) >= 2 and isinstance(children[1], int):
            state = children[1]
            item_content = children[0]
        else:
            item_content = children
        loaded = loadme(CTOR[classname], item_content)
        if state is not None:
            loaded.state = state
        page.append(loaded)
    return page


def _dump_page(page: iamraw.Page) -> dict:
    result = dict(
        page=page.page,
        children=[dumper(item) for item in page],
    )
    if page.dimension:
        dimension = utila.from_tuple(page.dimension)
        result['dimension'] = dimension
    return result


def _dump_line(line: iamraw.Line) -> str:
    assert len(line) >= 1, line
    styles = []
    start = 0
    cursize, currise, curunder = line[0].size, line[0].rise, line[0].underline
    for end, character in enumerate(line[1:], start=1):
        if isinstance(character, iamraw.VirtualChar):
            continue
        if cursize != character.size or currise != character.rise or curunder != character.underline:
            styles.append(create_style(
                start,
                end,
                cursize,
                currise,
                curunder,
            ))
            start = end
            cursize, currise, curunder = character.size, character.rise, character.underline
    if start != len(line):
        styles.append(
            create_style(
                start,
                len(line),
                cursize,
                currise,
                curunder,
            ))
    content = ''.join([item.value for item in line])
    # use list for a more human readable format
    result = [
        content,
        styles,
    ]
    return result


def create_style(start, end, size, rise, underline):
    style = ' '.join((
        f'{start}',
        f'{end}',
        '%.2f' % size if size is not None else 'None',
        '%.2f' % rise if rise is not None else 'None',
        'T' if underline else 'F',
    ))
    return style


def _load_line(line) -> iamraw.Line:
    assert len(line) == 2, line
    data, styles = line
    chars = []
    for style in styles:
        try:
            start, end, size, rise, underline = style.split()
        except ValueError:
            # TODO: REMOVE AFTER INCREASING MAJOR VERSION
            start, end, size, rise, underline = *style.split(), 'F'
        start, end = int(start), int(end)
        if size == 'None':
            size = None
        if rise == 'None':
            rise = None
        if underline == 'None':
            underline = None
        else:
            underline = underline == 'T'
        for index in range(start, end):
            # TODO: Unicodechar?
            char = iamraw.Char(
                value=data[index],
                size=float(size) if size is not None else None,
                rise=float(rise) if rise is not None else None,
                underline=underline,
            )
            chars.append(char)
    return iamraw.Line(chars=chars)


def _dump_textcontainer(container: iamraw.TextContainer):
    r"""\
    >>> _dump_textcontainer(iamraw.TextContainer.fromstr('this is a line',
    ...     state=texmex.TextState.HIDDEN))
    ([['this is a line\n', ['0 15 None None F']]], 0)
    >>> _dump_textcontainer(iamraw.VerticalTextContainer.fromstr('this is a line',
    ...     state=texmex.TextState.HIDDEN))
    ('VerticalTextContainer', [['this is a line\n', ['0 15 None None F']]], 0)
    """
    assert isinstance(container, iamraw.TextContainer), type(container)
    result = (
        container.__class__.__name__,
        [_dump_line(line) for line in container.lines],
        int(container.textstate),
    )  # use list for a more human readable format
    if container.__class__.__name__ == iamraw.TextContainer.__name__:
        # default class
        result = result[1:]
    if container.visible:
        # default state
        result = result[:-1]
    if len(result) == 1:
        # default class and default state
        result = result[0]
    return result


def _load_textcontainer(content) -> iamraw.TextContainer:
    r"""\
    >>> _load_textcontainer(([['this is a line\n', ['0 15 None None F']]],
    ...     texmex.TextState.HIDDEN.value))
    TextContainer(box=None, lines=[Line(text="this is a line")], state=<TextState.HIDDEN:...>)
    """
    assert isinstance(content, (list, tuple)), type(content)
    state = texmex.TextState.VISIBLE
    if len(content) >= 2 and isinstance(content[1], int):
        state = texmex.TextState(content[1])
        content = content[0]
    try:
        outdated = content[0] in 'TextContainer VerticalTextContainer'
    except TypeError:
        outdated = False
    if outdated:
        # TODO: REMOVE WITH NEXT MAJOR
        content = content[1]
    assert all(isinstance(item, list) for item in content), str(content)
    lines = [loadme(iamraw.Line, item) for item in content]
    result = iamraw.TextContainer(
        lines=lines,
        state=state,
    )
    return result


def _load_verticaltextcontainer(content) -> iamraw.VerticalTextContainer:
    """\
    >>> _load_verticaltextcontainer(_dump_textcontainer(iamraw.VerticalTextContainer.fromstr('this is a line')))
    VerticalTextContainer(box=None, lines=[Line(text="this is a line")], state=<TextState.VISIBLE:...)
    """
    content = _load_textcontainer(content)
    # TODO: USE KEYWARGS **?
    result = iamraw.VerticalTextContainer(
        lines=content.lines,
        state=content.state,
    )
    return result


def _load_document(content):
    dimension = serializeraw.border.size_fromraw(content['dimension'])
    pages = [loadme(iamraw.Page, item) for item in content['pages']]
    result = iamraw.Document(dimension=dimension, pages=pages)
    return result


def _dump_document(document: iamraw.Document) -> dict:
    assert document.dimension, str(document.dimension)
    result = {
        'dimension': serializeraw.border.size_toraw(document.dimension),
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


# yapf:disable
DUMP_LOAD = {
    iamraw.Document.__name__: (_dump_document, _load_document),
    iamraw.Line.__name__: (_dump_line, _load_line),
    iamraw.Page.__name__: (_dump_page, _load_page),
    iamraw.TextContainer.__name__: (_dump_textcontainer, _load_textcontainer),
    iamraw.VerticalTextContainer.__name__: (_dump_textcontainer, _load_verticaltextcontainer),
    iamraw.PageObject.__name__: (_dump_pageobject, _load_pageobject),
}
# yapf:enable
