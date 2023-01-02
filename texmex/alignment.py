# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import enum


class TextAlignment(enum.Enum):
    # TODO: Think about smart sorting order
    LEFT = 0
    CENTER = 1
    RIGHT = 2
    BLOCK = 4
    BLOCK_CENTER = 8
    BLOCK_END = 16
    UNDEFINED = -1

    def __lt__(self, item):
        """Support sorting TextAlignment, this is required, causes
        `modes` computation of used alignments requires to sort them to
        solve ambigious results."""
        # TODO: REPLACE pylint disable with correct one
        return self.value < item.value  # pylint:disable=all

    def __str__(self):
        """\
        >>> str(TextAlignment.RIGHT)
        'rechts'
        """
        if self == TextAlignment.LEFT:
            return 'links'
        if self == TextAlignment.CENTER:
            return 'zentriert'
        if self == TextAlignment.RIGHT:
            return 'rechts'
        if self == TextAlignment.BLOCK:
            return 'Blocksatz'
        if self == TextAlignment.BLOCK_CENTER:
            return 'Blocksatz zentriert'
        if self == TextAlignment.BLOCK_END:
            # TODO: VERIFY THIS
            return 'Blocksatz ?'
        return 'undefiniert'


TextAlignments = list[TextAlignment]
