# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
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
import functools

import configo
import utila

import iamraw


def dump_toc(content: iamraw.Toc, dump_raw: bool = True) -> str:
    """Convert table of content to raw yaml representation."""
    assert isinstance(content, iamraw.Toc), type(content)
    raw = _dump(content, dump_raw)
    return utila.yaml_dump(raw)


@functools.lru_cache(configo.CACHE_SMALL)
def load_toc(content: str, load_raw: bool = True) -> iamraw.Toc:
    """Load table of content from file or content

    Args:
        content(str): Content can be raw string or a file-path. If passing a
                      file-path, the file is loaded and parsed as a yaml file.
        load_raw(bool): Load additonal toc extraction information
    Returns:
        loaded iamraw.Toc
    """
    loaded = utila.yaml_load(
        content,
        fname='groupme__toc_toc',
        safe=False,
    )
    return _load(loaded, parent=None, load_raw=load_raw)


def _dump(current: iamraw.Section, dump_raw: bool):
    """Convert to raw python to have more clear yaml output"""
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
    except AttributeError:
        # iamraw.Toc ROOT node
        result = dict(
            level=current.level,
            style=current.style,
        )
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
        with contextlib.suppress(KeyError):
            result.page = current['page']
    except KeyError:
        result: iamraw.Toc = iamraw.Toc(
            level=current.get('level', 0),
            style=current.get('style', None),
        )
    with contextlib.suppress(KeyError):
        # A leaf has no children
        result.children = [
            _load(item, result, load_raw) for item in current['children']
        ]
    return result
