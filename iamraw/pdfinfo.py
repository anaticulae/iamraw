# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import collections
import dataclasses

import iamraw

PDFVersion = collections.namedtuple('PDFVersion', 'major minor')


@dataclasses.dataclass
class PDFInfo:
    pages: int = None
    generator: iamraw.Generator = None
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
