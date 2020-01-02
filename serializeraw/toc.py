# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2020 by Helmut Konrad Fahrendholz. All rights reserved.
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
import yaml

import iamraw


def dump_toc(content: iamraw.Toc) -> str:
    """Convert table of content to raw yaml representation."""
    assert isinstance(content, iamraw.Toc)
    raw = _dump(content)
    return yaml.dump(raw)


@functools.lru_cache(configo.CACHE_SMALL)
def load_toc(content: str) -> iamraw.Toc:
    """Load table of content from file or content

    Args:
        content(str): Content can be raw string or a file-path. If passing a
                      file-path, the file is loaded and parsed as a yaml file.
    Returns:
        loaded iamraw.Toc
    """
    content = utila.from_raw_or_path(content, ftype='yaml')
    loaded = yaml.load(content, Loader=yaml.FullLoader)
    return _load(loaded, parent=None)


def _dump(current: iamraw.Section):
    """Convert to raw python to have more clear yaml output"""
    children = [_dump(item) for item in current.children]
    try:
        result = {
            'level': current.level,
            'page': current.page,
            'raw': current.raw,
            'title': current.title,
        }
    except AttributeError:
        # iamraw.Toc ROOT node
        result = {'level': 0}

    if children:
        result['children'] = children
    return result


def _load(current: dict, parent: iamraw.Section):
    """Load from raw python without complex objects"""
    assert isinstance(current, dict), type(current)
    try:
        result = iamraw.Section(
            level=current['level'],
            title=current['title'],
            parent=parent,
        )
        with contextlib.suppress(KeyError):
            result.raw = current['raw']
        with contextlib.suppress(KeyError):
            result.page = current['page']
    except KeyError:
        result = iamraw.Toc()  # pylint:disable=redefined-variable-type

    with contextlib.suppress(KeyError):
        # A leaf has no children
        result.children = [_load(item, result) for item in current['children']]
    return result
