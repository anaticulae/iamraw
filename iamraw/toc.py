#==============================================================================
# C O P Y R I G H T
#------------------------------------------------------------------------------
# Copyright (c) 2019 by Helmut Konrad Fahrendholz. All rights reserved.
# Tis file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
#==============================================================================
"""Table of content.

Basic structure of get_outlines: (level, title, args, children)
"""

from dataclasses import dataclass
from dataclasses import field
from typing import Any
from typing import Dict
from typing import List


@dataclass
class Section:
    level: int
    title: str
    args: Dict[str, str] = field(default_factory=dict)
    # compare = False to avoid recursive lookups
    parent: Any = field(default=None, compare=False)
    children: List[Any] = field(default_factory=list)


@dataclass
class Toc:
    children: List[Section] = field(default_factory=list)
