# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

from dataclasses import dataclass

from utila import INF


@dataclass
class BoundingBox:
    x_bottom: float = -INF
    y_bottom: float = -INF

    x_top: float = INF
    y_top: float = INF


@dataclass
class PageObject:
    """Object to store every unsupported type"""
    box: BoundingBox = None
    content: str = None
