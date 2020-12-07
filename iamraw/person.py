# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import dataclasses
import typing


@dataclasses.dataclass
class Person:
    name: str = None
    firstname: str = None
    title: str = None
    confidence: float = None
    raw: str = None


@dataclasses.dataclass
class NoPerson:
    """Negative result of person parsing."""
    confidence: float = None
    raw: str = None


Persons = typing.List[Person]
