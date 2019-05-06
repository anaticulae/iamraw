# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================o
"""
Dump and load toc to yaml. Ensure loading from raw-string and file-path.
"""

from os.path import join

from pytest import fixture
from pytest import raises
from utila import file_create

from iamraw import Section
from iamraw import Toc
from serializeraw.toc import dump_yaml
from serializeraw.toc import load_yaml
from tests.serializeraw import TOC_YAML


def create_section(level: int, title: str, parent) -> Section:
    """Create section with no parents or children

    Args:
        level(int): level of hierarchy in toc - root(0) chapter(1) subchaper(2)
        title(str): title of level
    Returns:
        Section(level, str)
    """
    return Section(level=level, title=title, parent=parent)


@fixture
def toc_example():
    """Create table of content with 3 headlines"""
    root = Toc()

    first = create_section(1, 'Kapitel 1', root)
    second = create_section(2, 'Kapitel 1.1', first)
    third = create_section(3, 'Kapitel 1.1.1', second)

    root.children.append(first)
    first.children.append(second)
    second.children.append(third)

    return root


def test_load_toc_from_path():
    toc = load_yaml(TOC_YAML)
    assert toc


def test_dump_and_load_toc(toc_example):
    """Serialize toc and load it afterwards"""
    root = toc_example
    content = dump_yaml(root)
    loaded = load_yaml(content)
    assert str(loaded) == str(root)
    assert loaded == root


def test_load_from_filepath(tmpdir, toc_example):
    """Compare loading from raw string and filepath."""

    dumped = dump_yaml(toc_example)

    to_write = join(tmpdir, 'toc.yaml')

    file_create(to_write, dumped)

    from_file = load_yaml(to_write)  # from path
    from_raw = load_yaml(dumped)  # from raw

    assert from_file == toc_example
    assert from_file == from_raw


def test_load_non_existing_toc():
    """Non existing resource leads to ValueError"""
    path = 'C:/iamthepath/toc.yaml'

    with raises(ValueError):
        load_yaml(path)
