# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import contextlib
import dataclasses
import typing

import iamraw


@dataclasses.dataclass(unsafe_hash=True)
class BibliographyReference:  # pylint:disable=R0902

    title: str = None
    reference: str = None

    data: str = None

    page: int = None
    pageend: int = None

    year: int = None
    yearend: int = None

    hyperlink: str = None
    accessed: str = None

    # a,b,c... to differentiate item in the same year
    number: str = None
    authors: typing.List[str] = dataclasses.field(default_factory=list)

    publisher: str = None

    raw: str = dataclasses.field(default=None, compare=False)
    raw_pdfpage: int = None

    @classmethod
    def create(cls, author: str, title: str = '', year: int = 2000):
        author = author.split(' ', maxsplit=1)
        author = iamraw.Person(name=author[0], firstname=author[1])
        with contextlib.suppress(TypeError):
            year = int(year)
        return cls(authors=[author], title=title, year=year)

    @property
    def author(self) -> str:
        """Return family of first author."""
        with contextlib.suppress(IndexError, AttributeError):
            # IndexError: No author parsed
            # AttributeError: NoPerson parsed
            return self.authors[0].name  # pylint:disable=E1136
        return None


BibliographyReferences = typing.List[BibliographyReference]
