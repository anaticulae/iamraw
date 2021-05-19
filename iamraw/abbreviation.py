# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2021 by Helmut Konrad Fahrendholz. All rights reserved.
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
        return utila.alphabetically(self.short) <= utila.alphabetically(item.short) # yapf:disable


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


ExtractedTextAbbreviation = collections.namedtuple(
    'ExtractedTextAbbreviation',
    'page, content',
)
ExtractedTextAbbreviations = typing.List[ExtractedTextAbbreviation]
