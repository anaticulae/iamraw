# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================
from dataclasses import dataclass
from dataclasses import field
from typing import List


@dataclass
class Headline:
    text: str
    level: int = field(default=0)
    rawlevel: str = field(default=None, compare=False)
    page: int = field(default=-1)
    container: int = field(default=None)


PagesHeadlineList = List[List[Headline]]
