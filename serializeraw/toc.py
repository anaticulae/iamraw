# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================
"""This module supports dumping and loading a table of content into yaml
file format.

Public methods:

    dump_yaml
    load_yamp

"""

import contextlib

import configo
import utilo

import iamraw


def dump_toc(content: iamraw.Toc, dump_raw: bool = True) -> str:
    """Convert table of content to raw yaml representation."""
    assert isinstance(content, iamraw.Toc), type(content)
    raw = _dump(content, dump_raw)
    return utilo.yaml_dump(raw)


@configo.cache_small
def load_toc(content: str, load_raw: bool = True) -> iamraw.Toc:
    """Load table of content from file or content

    Args:
        content(str): Content can be raw string or a file-path. If passing a
                      file-path, the file is loaded and parsed as a yaml file.
        load_raw(bool): Load additonal toc extraction information
    Returns:
        loaded iamraw.Toc
    """
    loaded = utilo.yaml_load(
        content,
        fname=('reftable__toc_toc', 'groupme__toc_toc'),
        safe=False,
    )
    return _load(loaded, parent=None, load_raw=load_raw)


def _dump(current: iamraw.Section, dump_raw: bool):
    """Convert to raw python to have more clear yaml output.

    >>> toc = iamraw.Toc()
    >>> toc.__strategy__='Master'
    >>> _dump(toc, dump_raw=True)
    {...'__strategy__': 'Master'}

    """
    children = [_dump(item, dump_raw) for item in current.children]
    try:
        result = {
            'level': current.level,
            'page': current.page,
            'title': current.title,
        }
        with contextlib.suppress(AttributeError):
            if dump_raw:
                result['raw'] = current.raw
                result['raw_location'] = current.raw_location
                result['raw_page'] = current.raw_page
                result['raw_level'] = current.raw_level
    except AttributeError:
        # iamraw.Toc ROOT node
        result = dict(
            level=current.level,
            style=current.style.name if current.style else None,
        )
        with contextlib.suppress(AttributeError):
            if current.__strategy__:
                result['__strategy__'] = current.__strategy__
    if children:
        result['children'] = children
    return result


def _load(current: dict, parent: iamraw.Section, load_raw: bool):
    """Load from raw python without complex objects"""
    assert isinstance(current, dict), type(current)
    ctor = iamraw.SectionRaw if load_raw else iamraw.Section
    try:
        result = ctor(
            parent=parent,
            level=current['level'],
            title=current['title'],
        )
        with contextlib.suppress(KeyError):
            if load_raw:
                result.raw = current['raw']
                result.raw_location = current['raw_location']
                result.raw_level = current['raw_level']
                result.raw_page = current['raw_page']
        with contextlib.suppress(KeyError):
            result.page = current['page']
    except KeyError:
        tocstyle = current.get('style', None)
        if tocstyle:
            tocstyle = iamraw.TocStyle[tocstyle]
        result: iamraw.Toc = iamraw.Toc(
            level=current.get('level', 0),
            style=tocstyle,
        )
        result.__strategy__ = current.get('__strategy__', None)
    with contextlib.suppress(KeyError):
        # A leaf has no children
        result.children = [
            _load(item, result, load_raw) for item in current['children']
        ]
    return result
