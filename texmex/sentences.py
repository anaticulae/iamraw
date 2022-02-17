# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import enum


class SentenceType(enum.Enum):
    """\
    >>> SentenceType.QUOT.name
    'QUOT'
    """
    # no special sentence
    NORMAL = enum.auto()
    # lists
    LIST_SEPA = enum.auto()
    LIST_ITEM = enum.auto()
    # formulas
    FORMULA = enum.auto()
    # quotation
    QUOT = enum.auto()
    QUOT_START = enum.auto()
    QUOT_END = enum.auto()
    QUOT_QUOT = enum.auto()  # quotation inside quotation
    QUOT_QUOT_START = enum.auto()
    QUOT_QUOT_END = enum.auto()
