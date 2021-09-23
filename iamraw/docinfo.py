# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import dataclasses
import enum


class DocumentType(enum.Enum):
    NONE = enum.auto()
    HOMEWORK = enum.auto()
    BACHELOR = enum.auto()
    MASTER = enum.auto()
    DISS = enum.auto()
    HABIL = enum.auto()
    BOOK = enum.auto()
    PAPER = enum.auto()


class Generator(enum.Enum):
    UNDEFINED = enum.auto()
    LATEX = enum.auto()
    MSWORD = enum.auto()

    def __str__(self):
        """\
        >>> str(Generator.MSWORD)
        'msword'
        """
        return str(self.name).lower()


@dataclasses.dataclass
class DocInfo:
    pages: int = None
    doctype: DocumentType = None
    generator: Generator = None
    sections: 'SectionLookup' = None
    """Skip findings which do not pass sections check."""


class SectionLookup:

    def __init__(self, sections: 'iamraw.Sections'):
        self.sections = sections

    def __call__(self, location: 'iamraw.Location', only=None, skip=None):
        """Return False if section is excluded via only or skip definition."""
        page = location.page
        selected = self.current(page)
        assert selected is not None
        classes = selected.__class__
        if skip and classes in skip:
            return False
        if only and classes not in only:
            return False
        return True

    def current(self, page: int):
        # TODO: USE IMPROVE SELECTOR, REDUCE LINEAR EFFORT
        for section in self.sections:
            if not section.start <= page <= section.end:
                continue
            for item in section:
                if not item.start <= page <= item.end:
                    continue
                return item
        return None
