# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import abc


class ExtractedMixin:

    def __init__(self, location=None, strategy: str = None):
        self.location = location
        self.strategy = strategy

    @abc.abstractmethod
    def raw(self) -> str:
        """Element in document which is converted to current result."""
