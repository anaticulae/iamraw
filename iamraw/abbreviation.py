# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import collections
import dataclasses

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


Abbreviations = list[Abbreviation]


@dataclasses.dataclass
class AbbreviationResult:

    abbreviations: Abbreviations = dataclasses.field(default_factory=list)
    pdfpages: list = dataclasses.field(default_factory=list)

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
        return any((item.short.lower() == abbrev for item in self.abbreviations))  # yapf:disable


ExtractedTextAbbreviation = collections.namedtuple(
    'ExtractedTextAbbreviation',
    'page, content',
)
ExtractedTextAbbreviations = list[ExtractedTextAbbreviation]


@dataclasses.dataclass
class AbbreviationList:
    data: set = dataclasses.field(default_factory=set)

    def append(self, item):
        self.data.add(item)  # pylint:disable=E1101

    def __contains__(self, item):
        return item in self.data  # pylint:disable=unsupported-membership-test


AbbreviationLists = list[AbbreviationList]


@dataclasses.dataclass
class AbbreviationListLookup:
    table: AbbreviationList = dataclasses.field(default=AbbreviationList)
    other: AbbreviationLists = dataclasses.field(default_factory=list)

    def __contains__(self, item):
        if item in self.table:  # pylint:disable=E1135
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
