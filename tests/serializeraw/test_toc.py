# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================o
"""Testing dump and load table of content to yaml.

- Ensure loading from raw string and file path.
"""

import os

import pytest
import utila

import iamraw
import serializeraw
import tests.serializeraw


def create_section(
        level: int,
        title: str,
        parent: iamraw.toc.TocLink,
) -> iamraw.Section:
    """Create section with no parents or children

    Args:
        level(int): level of hierarchy in toc - root(0) chapter(1) subchaper(2)
        title(str): title of level
        parent: parent item of current `Section`.
    Returns:
        Section(level, str)
    """
    return iamraw.Section(level=level, title=title, parent=parent)


@pytest.fixture
def toc_example():
    """Create table of content with 3 headlines."""
    root = iamraw.Toc()

    first = create_section(1, 'Kapitel 1', root)
    second = create_section(2, 'Kapitel 1.1', first)
    third = create_section(3, 'Kapitel 1.1.1', second)

    root.append(first)
    first.append(second)
    second.append(third)

    return root


def test_load_toc_from_path():
    toc = serializeraw.load_toc(tests.serializeraw.TOC_YAML)
    assert toc


def test_dump_and_load_toc(toc_example):  # pylint:disable=W0621
    """Serialize toc and load it afterwards."""
    root = toc_example
    content = serializeraw.dump_toc(root)
    loaded = serializeraw.load_toc(content)
    assert str(loaded) == str(root)
    assert loaded == root


def test_load_from_filepath(tmpdir, toc_example):  # pylint:disable=W0621
    """Compare loading from raw string and filepath."""

    dumped = serializeraw.dump_toc(toc_example)

    to_write = os.path.join(tmpdir, 'toc.yaml')

    utila.file_create(to_write, dumped)

    from_file = serializeraw.load_toc(to_write)  # from path
    from_raw = serializeraw.load_toc(dumped)  # from raw

    assert from_file == toc_example
    assert from_file == from_raw


def test_load_non_existing_toc():
    """None existing resource leads to ValueError."""
    path = 'C:/iamthepath/toc.yaml'

    with pytest.raises(ValueError):
        serializeraw.load_toc(path)
