# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import dataclasses

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
        >>> assert Figure(bounding=(1, 1, 1, 1), page=5).identifier
        """
        return utila.pagebox_hash(page=self.page, box=self.bounding)


Figures = list[Figure]
