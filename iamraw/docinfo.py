# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

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
    BASE = enum.auto()
    LATEX = enum.auto()
    MSWORD = enum.auto()
