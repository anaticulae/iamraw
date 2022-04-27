# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import dataclasses
import typing

import utila


@dataclasses.dataclass
class Figure:
    data: 'PIL.Image.Image' = None
    bounding: tuple = None
    page: int = None
    index: int = None

    @property
    def identifier(self) -> int:
        """\
        >>> Figure(bounding=(1, 1, 1, 1), page=5).identifier
        900150000000000000000001111
        """
        return utila.pagebox_hash(page=self.page, box=self.bounding)


Figures = typing.List[Figure]
