#==============================================================================
# Copyright (c) 2019 by Helmut Konrad Fahrendholz (kiwi@derspanier.de).
# All rights reserved. This file is property of Helmut Konrad Fahrendholz. Any
# unauthorized copy, use or distribution is an offensive act against
# international law and may be prosecuted under federal law. Its content is
# company confidential.
#==============================================================================

import utila

from iamraw import Section
from iamraw import create_toc


def create_section(level: int, title: str) -> Section:
    """Create section with no parents or children

    Args:
        level(int): level of hierarchy in toc - root(0) chapter(1) subchaper(2)
        title(str): title of level
    Returns:
        Section(level, str)
    """
    return Section(level=level, title=title)


TOC = [
    create_section(1, 'Kapitel 1'),
    create_section(2, 'Kapitel 1.1'),
    create_section(2, 'Kapitel 1.2'),
    create_section(3, 'Kapitel 1.2.1'),
    create_section(3, 'Kapitel 1.2.2'),
    create_section(3, 'Kapitel 1.2.3'),
    create_section(4, 'Kapitel 1.2.3.2'),
    create_section(2, 'Kapitel 1.3'),
    create_section(1, 'Kapitel 2'),
    create_section(2, 'Kapitel 2.1'),
    create_section(2, 'Kapitel 2.2'),
    create_section(1, 'Kapitel 3'),
]


def test_create_toc():
    """Parse valid toc structure"""
    root = create_toc(TOC)

    assert_children(root, 3)

    first_chapter = root.children[0]  # pylint:disable=E1136
    assert_children(first_chapter, 3)

    first_section = first_chapter.children[0]
    assert_children(first_section, 0)
    second_section = first_chapter.children[1]
    assert_children(second_section, 3)

    second_chapter = root.children[1]  # pylint:disable=E1136
    assert_children(second_chapter, 2)
    third_chapter = root.children[2]  # pylint:disable=E1136
    assert_children(third_chapter, 0)


INVALID_TOC = [
    create_section(3, 'Kapitel 1.2.3'),
    create_section(1, 'Kapitel 1'),
    create_section(2, 'Kapitel 1.2'),
    create_section(4, 'Kapitel 1.2.1.1'),
    create_section(1, 'Kapitel 2'),
]


def test_parse_invalid_toc():
    """Parse invalid toc structure.

    Invalid means, not logical right table of content is expecteds."""
    root = create_toc(INVALID_TOC)

    assert root is not None
    assert_children(root, 3)

    invalid_first_chapter = root.children[0]  # pylint:disable=E1136
    assert_children(invalid_first_chapter, 0)
    assert invalid_first_chapter.title == INVALID_TOC[0].title
    assert invalid_first_chapter.level == INVALID_TOC[0].level

    first_chapter = root.children[1]  # pylint:disable=E1136
    second_chapter = root.children[2]  # pylint:disable=E1136

    assert_children(first_chapter, 1)
    assert_children(second_chapter, 0)

    first_section = first_chapter.children[0]
    assert_children(first_section, 1)

    first_sub_sub_section = first_section.children[0]
    assert_children(first_sub_sub_section, 0)
    assert first_sub_sub_section.title == INVALID_TOC[3].title


def test_toc_minimal():
    outline = [create_section(3, 'Kapitel 1.1.1')]
    root = create_toc(outline)
    assert_children(root, 1)


def test_toc_empty():
    outline = []
    root = create_toc(outline)
    assert_children(root, 0)


def assert_children(component: Section, count: int):
    assert component is not None, component
    assert len(component) == count


WRONG_TOC = [
    create_section(4, 'Kapitel 1.1.1.1'),
    create_section(1, 'Kapitel 1'),
]


def test_wrong_toc():
    root = create_toc(WRONG_TOC)
    assert_children(root, 2)


EXPECTED = """\
Kapitel 1
Kapitel 1.1
Kapitel 1.2
Kapitel 1.2.1
Kapitel 1.2.2
Kapitel 1.2.3
Kapitel 1.2.3.2
Kapitel 1.3
Kapitel 2
Kapitel 2.1
Kapitel 2.2
Kapitel 3
""".strip()


def test_toc_recursive():
    root = create_toc(TOC)
    raw = utila.NEWLINE.join(item[1].title for item in root.recursive())
    assert raw == EXPECTED
