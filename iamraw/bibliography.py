# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import contextlib
import dataclasses
import typing


@dataclasses.dataclass(unsafe_hash=True)
class BibliographyReference:

    title: str = None
    reference: str = None

    data: str = None

    page: int = None
    pageend: int = None

    year: int = None
    yearend: int = None

    hyperlink: str = None

    # a,b,c... to differentiate item in the same year
    number: str = None
    authors: typing.List[str] = dataclasses.field(default_factory=list)

    publisher: str = None

    raw: str = None

    @classmethod
    def create(cls, author: str, title: str = '', year: int = 2000):
        author = tuple(author.split(' ', maxsplit=1))
        with contextlib.suppress(TypeError):
            year = int(year)
        return cls(authors=[author], title=title, year=year)

    @property
    def author(self) -> str:
        """Return family of first author."""
        with contextlib.suppress(IndexError):
            return self.authors[0][0]  # pylint:disable=E1136
        return None


BibliographyReferences = typing.List[BibliographyReference]
