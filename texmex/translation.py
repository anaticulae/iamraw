# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import dataclasses
import typing


@dataclasses.dataclass
class Translation:
    """\
    >>> trans = Translation().add(10, 15).add(13, 16)
    >>> trans(16)
    13
    """
    page: int = None
    data: dict = dataclasses.field(default_factory=dict)

    def add(self, source, dest):
        self.data[dest] = source
        return self

    def __call__(self, dest):
        try:
            return self.data[dest]
        except KeyError:
            # no translation required
            return dest


Translations = typing.List[Translation]
