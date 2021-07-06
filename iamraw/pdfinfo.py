# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import collections
import dataclasses
import enum

PDFVersion = collections.namedtuple('PDFVersion', 'major minor')


class PDFGenerator(enum.Enum):
    UNDEFINED = enum.auto()
    LATEX = enum.auto()
    MSWORD = enum.auto()

    def __str__(self):
        """\
        >>> str(PDFGenerator.MSWORD)
        'msword'
        """
        return str(self.name).lower()


@dataclasses.dataclass
class PDFInfo:
    pages: int = None
    generator: PDFGenerator = None
    version: PDFVersion = None
    meta: dict = None


InvalidPDF = object()


@dataclasses.dataclass
class PDFDate:  # pylint:disable=R0902
    year: int = None
    month: int = None
    day: int = None
    hour: int = None
    minute: int = None
    second: int = None
    utc_hour: int = None
    utc_minute: int = None
