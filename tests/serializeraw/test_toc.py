# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================o
"""Testing dump and load table of content to yaml.

- Ensure loading from raw string and file path.
"""

import functools
import os

import pytest
import utila

import iamraw
import serializeraw
import tests.serializeraw


def create_section(
        level: int,
        title: str,
        parent: iamraw.toc.TocLinkMixin,
        raw: bool = False,
) -> iamraw.Section:
    """Create section with no parents or children

    Args:
        level(int): level of hierarchy in toc - root(0) chapter(1) subchaper(2)
        title(str): title of level
        parent: parent item of current `Section`.
        raw(bool): use SectionRaw data type
    Returns:
        SectionRaw if raw else Section(level, str)
    """
    section = iamraw.Section(level=level, title=title, parent=parent)
    if raw:
        section = iamraw.tosectionraw(section)  # pylint:disable=R0204
    return section


def toc_example(dump_raw: bool = False):
    """Create table of content with 3 headlines."""
    root = iamraw.Toc()

    create = functools.partial(create_section, raw=dump_raw)

    first = create(1, 'Kapitel 1', root)
    second = create(2, 'Kapitel 1.1', first)
    third = create(3, 'Kapitel 1.1.1', second)

    root.append(first)
    first.append(second)
    second.append(third)

    return root


def test_load_toc_from_path():
    toc = serializeraw.load_toc(tests.serializeraw.TOC_YAML)
    assert toc


EXPECTED = """\
Kapitel 1
    Kapitel 1.1
        Kapitel 1.1.1"""


def test_toc_str():
    example = toc_example(dump_raw=True)
    raw = str(example)
    assert raw == EXPECTED
    assert iamraw.merge_toc(example) == EXPECTED


@pytest.mark.parametrize('dump_raw', [True, False])
def test_dump_and_load_toc(dump_raw):  # pylint:disable=W0621
    """Serialize toc and load it afterwards."""
    root = toc_example(dump_raw)
    content = serializeraw.dump_toc(root, dump_raw=dump_raw)
    loaded = serializeraw.load_toc(content, load_raw=dump_raw)
    assert str(loaded) == str(root)
    assert loaded == root


@pytest.mark.parametrize('dump_raw', [True, False])
def test_load_from_filepath(dump_raw, tmpdir):  # pylint:disable=W0621
    """Compare loading from raw string and filepath."""
    root = toc_example(dump_raw)

    dumped = serializeraw.dump_toc(root, dump_raw=dump_raw)

    to_write = os.path.join(tmpdir, 'toc.yaml')

    utila.file_create(to_write, dumped)

    from_file = serializeraw.load_toc(to_write, load_raw=dump_raw)  # from path
    from_raw = serializeraw.load_toc(dumped, load_raw=dump_raw)  # from raw

    assert from_file == root
    assert from_file == from_raw


def test_load_non_existing_toc():
    """None existing resource leads to ValueError."""
    path = 'C:/iamthepath/toc.yaml'

    with pytest.raises(FileNotFoundError):
        serializeraw.load_toc(path)


@pytest.mark.parametrize('dump_raw', [True, False])
def test_toc_iterate_children(dump_raw):  # pylint:disable=W0621
    example = toc_example(dump_raw)
    for items in example:
        assert items
        for item in items:
            assert item


def test_section_to_sectionraw():
    source = iamraw.Section(title='Title test')
    raw = iamraw.tosectionraw(source)
    source_converted = iamraw.tosection(raw)
    assert source_converted == source
