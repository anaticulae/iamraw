# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import collections
import dataclasses
import typing

import utila


@dataclasses.dataclass
class AbbreviationPosition:
    page: int = None
    sentence: int = None
    word: int = None


@dataclasses.dataclass
class Abbreviation:
    short: str = None
    description: str = None
    position: AbbreviationPosition = None

    def __lt__(self, item):
        if utila.alphabetically(self.short) <= utila.alphabetically(item.short):
            return True
        return False


Abbreviations = typing.List[Abbreviation]


@dataclasses.dataclass
class AbbreviationResult:

    abbreviations: Abbreviations = dataclasses.field(default_factory=list)

    def append(self, item):
        self.abbreviations.append(item)  # pylint:disable=E1101

    def __getitem__(self, index):
        return self.abbreviations[index]  # pylint:disable=E1136

    def __len__(self):
        return len(self.abbreviations)

    def short_inside(self, abbrev: str) -> bool:
        """\
        >>> AbbreviationResult().short_inside('')
        False
        """
        for item in self.abbreviations:
            if item.short.lower() == abbrev:
                return True
        return False


ExtractedTextAbbreviation = collections.namedtuple(
    'ExtractedTextAbbreviation',
    'page, content',
)
ExtractedTextAbbreviations = typing.List[ExtractedTextAbbreviation]


@dataclasses.dataclass
class AbbreviationList:
    data: set = dataclasses.field(default_factory=set)

    def append(self, item):
        self.data.add(item)  # pylint:disable=E1101

    def __contains__(self, item):
        return item in self.data  # pylint:disable=unsupported-membership-test


AbbreviationLists = typing.List[AbbreviationList]


@dataclasses.dataclass
class AbbreviationListLookup:
    table: AbbreviationList = dataclasses.field(default=AbbreviationList)
    other: AbbreviationLists = dataclasses.field(default_factory=list)

    def __contains__(self, item):
        if item in self.table:
            return True
        if self.other:
            for table in self.other:
                if item in table:
                    return True
        return False

    @classmethod
    def fromparsed(cls, parsed=None, other=None):
        assert parsed or other, 'empty input'
        if parsed is None:
            parsed = AbbreviationList()
        lookup = cls(table=parsed, other=other)
        return lookup
