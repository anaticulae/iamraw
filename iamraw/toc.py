#==============================================================================
# C O P Y R I G H T
#------------------------------------------------------------------------------
# Copyright (c) 2019 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
#==============================================================================
"""Table of content
================

Basic structure of get_outlines: (level, title, args, children)
"""
import abc
import dataclasses
import typing


class TocLinkMixin(abc.ABC):

    @abc.abstractmethod
    def append(self, item):
        """Append `item` as children."""

    @abc.abstractmethod
    def __getitem__(self, index):
        """Access children at `index`"""


@dataclasses.dataclass
class Section(TocLinkMixin):
    level: int
    title: str
    page: int = None
    raw: str = None
    args: typing.Dict[str, str] = dataclasses.field(default_factory=dict)
    # compare = False to avoid recursive lookups
    parent: typing.Any = dataclasses.field(default=None, compare=False)
    children: typing.List[typing.Any] = dataclasses.field(default_factory=list)

    def append(self, item):
        self.children.append(item)  # pylint:disable=E1101

    def __getitem__(self, index):
        return self.children[index]  # pylint:disable=E1136


@dataclasses.dataclass
class Toc(TocLinkMixin):
    level: int = 0  # level must alsways be 0
    children: typing.List[Section] = dataclasses.field(default_factory=list)

    def append(self, item):
        self.children.append(item)  # pylint:disable=E1101

    def __getitem__(self, index):
        return self.children[index]  # pylint:disable=E1136


def create_toc(outlines: typing.List[Section]):
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
            current.parent.append(new_one)  # pylint:disable=E1101
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
            current.append(new_one)
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
            current.append(new_one)
        current = new_one  # pylint:disable=redefined-variable-type
    return root
