# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================
"""
This module supports dumping and loading a table of content into yaml file
format.

Public methods:

    dump_yaml
    load_yamp

"""
from functools import lru_cache

from configo import CACHE_SMALL
from utila import from_raw_or_path
from yaml import FullLoader
from yaml import dump
from yaml import load

from iamraw import Section
from iamraw import Toc


def dump_yaml(content: Toc) -> str:
    """Convert table of content to raw yaml representation."""
    assert isinstance(content, Toc)
    raw = _dump(content)
    return dump(raw)


@lru_cache(CACHE_SMALL)
def load_yaml(content: str) -> Toc:
    """Load table of content from file or content

    Args:
        content(str): Content can be raw string or a file-path. If passing a
                      file-path, the file is loaded and parsed as a yaml file.
    Returns:
        loaded Toc
    """
    content = from_raw_or_path(content, ftype='yaml')
    loaded = load(content, Loader=FullLoader)
    return _load(loaded, parent=None)


def _dump(current: Section):
    """Convert to raw python to have more clear yaml output"""
    children = [_dump(item) for item in current.children]
    try:
        result = {'level': current.level, 'title': current.title}
    except AttributeError:
        # Toc ROOT node
        result = {'level': 0}

    if children:
        result['children'] = children
    return result


def _load(current: dict, parent: Section):
    """Load from raw python without complex objects"""
    if not isinstance(current, dict):
        raise ValueError('Invalid table of content: %s' % current)
    try:
        result = Section(
            level=current['level'],
            title=current['title'],
            parent=parent,
        )
    except KeyError:
        result = Toc()

    try:
        result.children = [_load(item, result) for item in current['children']]
    except KeyError:
        # A leaf has no children
        pass
    return result
