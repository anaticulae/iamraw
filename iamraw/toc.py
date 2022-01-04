#==============================================================================
# C O P Y R I G H T
#------------------------------------------------------------------------------
# Copyright (c) 2019-2022 by Helmut Konrad Fahrendholz. All rights reserved.
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

import configo
import utila


class TocLinkMixin(abc.ABC):

    @abc.abstractmethod
    def append(self, item):
        """Append `item` as children."""

    @abc.abstractmethod
    def __getitem__(self, index):
        """Access children at `index`"""


TocLinkMixins = typing.List[TocLinkMixin]


@dataclasses.dataclass
class Section(TocLinkMixin):
    level: int = None
    title: str = None
    page: int = None  # pdf representation
    args: typing.Dict[str, str] = dataclasses.field(default_factory=dict)
    # compare = False to avoid recursive lookups
    parent: TocLinkMixin = dataclasses.field(default=None, compare=False)
    children: TocLinkMixins = dataclasses.field(default_factory=list)

    def append(self, item):
        self.children.append(item)  # pylint:disable=E1101

    def __getitem__(self, index):
        return self.children[index]  # pylint:disable=E1136

    def __len__(self):
        return len(self.children)


@dataclasses.dataclass
class SectionRaw(Section):
    # Extend Section with data where information was crafted
    raw: str = None
    raw_location: int = None
    raw_level: str = None
    raw_page: str = None

    def __str__(self):
        result = (
            f'SectionRaw(raw="{self.raw}", raw_location={self.raw_location}, '
            f'raw_level="{self.raw_level}", raw_page="{self.raw_page}", '
            f'level={self.level})')
        return result


def tosectionraw(item: Section) -> SectionRaw:
    assert isinstance(item, Section), type(item)
    return SectionRaw(**vars(item))


def tosection(item: SectionRaw) -> Section:
    assert isinstance(item, SectionRaw), type(item)
    data = vars(item)
    del data['raw']
    del data['raw_level']
    del data['raw_location']
    del data['raw_page']
    return Section(**data)


SectionList = typing.List[Section]


@dataclasses.dataclass
class Toc(TocLinkMixin):
    level: int = 0  # level must alsways be 0
    # distinguish between numbered and stepped toc
    numbered: bool = True
    children: SectionList = dataclasses.field(default_factory=list)

    def append(self, item):
        self.children.append(item)  # pylint:disable=E1101

    def __getitem__(self, index):
        return self.children[index]  # pylint:disable=E1136

    def __len__(self):
        return len(self.children)

    def __str__(self) -> str:
        return merge_toc(self)


def create_toc(
    outlines: SectionList,
    numbered: bool = True,
    *,
    remove_rawinfo: bool = False,
) -> Toc:
    """Extract toc out of pdf-outlines.

    The highest level is 0 the document root. Higher number level means
    more distance to root.

    Args:
        outlines: flat list to create toc
        numbered(bool): distinguish between numbered and stepped toc
        remove_rawinfo(bool): if True, do not store information where
                              data was collected.
    Returns:
        Hierarchical table of content.
    """
    root = Toc(numbered=numbered)
    current = root
    for item in outlines:
        level = item.level
        if level == current.level:
            # Content is on the same level, therefore they have the same
            # parent together.
            new_one = SectionRaw(
                parent=current.parent,  # pylint:disable=E1101
                level=item.level,
                page=item.page,
                raw=getattr(item, 'raw', ''),
                raw_level=getattr(item, 'raw_level', ''),
                raw_location=getattr(item, 'raw_location', ''),
                raw_page=getattr(item, 'raw_page', ''),
                title=item.title,
            )
            new_one = tosection(new_one) if remove_rawinfo else new_one
            current.parent.append(new_one)  # pylint:disable=E1101
        elif level > current.level:
            # The level of the item to add is higher than the current item in
            # table of content, therefore add the new one as a paranet of
            # current.
            new_one = SectionRaw(
                parent=current,
                level=item.level,
                page=item.page,
                raw=getattr(item, 'raw', ''),
                raw_level=getattr(item, 'raw_level', ''),
                raw_location=getattr(item, 'raw_location', ''),
                raw_page=getattr(item, 'raw_page', ''),
                title=item.title,
            )
            new_one = tosection(new_one) if remove_rawinfo else new_one
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
            new_one = SectionRaw(
                parent=current,
                level=item.level,
                page=item.page,
                raw=getattr(item, 'raw', ''),
                raw_level=getattr(item, 'raw_level', ''),
                raw_location=getattr(item, 'raw_location', ''),
                raw_page=getattr(item, 'raw_page', ''),
                title=item.title,
            )
            new_one = tosection(new_one) if remove_rawinfo else new_one
            current.append(new_one)
        current = new_one  # pylint:disable=redefined-variable-type
    return root


def merge_toc(toc: Toc) -> str:
    """Convert `table of content` to string."""
    result = []

    def recursive(item, level):
        result = []
        result.append('    ' * level + item.title)
        if item.children:
            for child in item.children:
                result.extend(recursive(child, level + 1))
        return result

    for item in toc:
        result.extend(recursive(item, level=0))
    titles = utila.NEWLINE.join(result)
    return titles


@dataclasses.dataclass
class Level:
    # TODO: MOVE TO IAMRAW
    value: int = None
    raw: str = dataclasses.field(compare=False, default=None)

    def __int__(self):
        return self.value


class RomanLevel(Level):
    pass


class StepLevel(Level):
    pass


@dataclasses.dataclass
class AppendixLevel(Level):
    """\
    Example::
        A.1.1
    """
    character: str = None

    def __int__(self):
        return APPENDIX_LEVEL


APPENDIX_LEVEL = configo.HV_INT_PLUS(default=100)
