#==============================================================================
# C O P Y R I G H T
#------------------------------------------------------------------------------
# Copyright (c) 2019 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
#==============================================================================
"""Table of content.

Basic structure of get_outlines: (level, title, args, children)
"""

from dataclasses import dataclass
from dataclasses import field
from typing import Any
from typing import Dict
from typing import List


class TocLink:
    pass


@dataclass
class Section(TocLink):
    level: int
    title: str
    page: int = None
    raw: str = None
    args: Dict[str, str] = field(default_factory=dict)
    # compare = False to avoid recursive lookups
    parent: Any = field(default=None, compare=False)
    children: List[Any] = field(default_factory=list)

    def append(self, item):
        self.children.append(item)  # pylint:disable=E1101


@dataclass
class Toc(TocLink):
    level: int = 0  # level must alsways be 0
    children: List[Section] = field(default_factory=list)

    def append(self, item):
        self.children.append(item)  # pylint:disable=E1101


def create_toc(outlines: List[Section]):
    """Extract toc out of pdf-outlines

    The highest level is 0 the document root. Higher number level means more
    distance to root.
    """
    root = Toc()
    current = root
    for item in outlines:
        level = item.level
        if level == current.level:
            # Content is on the same level, therefore they have the same
            # parent together.
            new_one = Section(
                parent=current.parent,  # pylint:disable=E1101
                level=item.level,
                page=item.page,
                raw=item.raw,
                title=item.title,
            )
            add_children(current.parent, new_one)  # pylint:disable=E1101
        elif level > current.level:
            # The level of the item to add is higher than the current item in
            # table of content, therefore add the new one as a paranet of
            # current.
            new_one = Section(
                parent=current,
                level=item.level,
                page=item.page,
                raw=item.raw,
                title=item.title,
            )
            add_children(current, new_one)
        else:
            # The level of the `new_one` is lower than the item in index. That
            # means that the distance of the item to add to the index is
            # samller as the current one.
            # For example: Current = 1.4.4.2
            #              item    = 1.5
            # We have to go up in the tree to find a common parent of both
            # and add item.
            while level <= current.level:
                current = current.parent  # pylint:disable=E1101
            new_one = Section(
                parent=current,
                level=item.level,
                page=item.page,
                raw=item.raw,
                title=item.title,
            )
            add_children(current, new_one)
        current = new_one  # pylint:disable=redefined-variable-type
    return root


def add_children(section: Section, item):
    assert section, item
    section.children.append(item)
