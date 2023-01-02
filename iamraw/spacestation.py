# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import dataclasses


@dataclasses.dataclass
class DocumentCharDist:
    mode: dict = dataclasses.field(default_factory=dict)
    mean: dict = dataclasses.field(default_factory=dict)
    median: dict = dataclasses.field(default_factory=dict)
    maxx: dict = dataclasses.field(default_factory=dict)
    minn: dict = dataclasses.field(default_factory=dict)
    count: dict = dataclasses.field(default_factory=dict)


@dataclasses.dataclass
class DocumentWordDist:
    mode: dict = dataclasses.field(default_factory=dict)
    mean: dict = dataclasses.field(default_factory=dict)
    median: dict = dataclasses.field(default_factory=dict)
    maxx: dict = dataclasses.field(default_factory=dict)
    minn: dict = dataclasses.field(default_factory=dict)
    count: dict = dataclasses.field(default_factory=dict)
