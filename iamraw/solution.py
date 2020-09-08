# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import dataclasses
import enum
import typing


class ProblemStatus(enum.Enum):
    OPEN = enum.auto()  # default status when non-CLOSED problem appears
    HIDDEN = enum.auto()  # user don't want to see this message
    DISAGREE = enum.auto()  # false alarm or user does agree with judgement
    SOLVED = enum.auto()  # user solved this issue in there document
    CLOSED = enum.auto()  # user can not change this state, e.g. pdf read error


@dataclasses.dataclass(unsafe_hash=True)  # pylint:disable=R0903
class Solution:
    number: int = dataclasses.field(compare=False, default=-1)
    msgid: str = None
    status: ProblemStatus = ProblemStatus.OPEN


Solutions = typing.List[Solution]


@dataclasses.dataclass(unsafe_hash=True)  # pylint:disable=R0903
class Text(Solution):
    title: str = None
    description: str = None


@dataclasses.dataclass(unsafe_hash=True)  # pylint:disable=R0903
class Web(Text):

    hyperlinks: list = dataclasses.field(default=list)
    """List of hyperlinks to underline the description."""


@dataclasses.dataclass(unsafe_hash=True)  # pylint:disable=R0903
class Doctails(Text):
    """Describes link to internal documentation database.

    Example:
     * `{writing/manuskript/zitate}`
     * `{writing/user}`
    """
