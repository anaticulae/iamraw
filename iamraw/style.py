# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import dataclasses

import utila


@dataclasses.dataclass(unsafe_hash=True)
class PageTextProperties:
    length: int = None
    hashed: int = None
    sizes: float = None
    fonts: int = None
    distances: float = None
    ypos: float = None
    left: float = None
    right: float = None
    page: int = None


@dataclasses.dataclass(unsafe_hash=True)
class TextProperty:
    length: int = None
    hashed: str = None
    size: float = None
    font: int = None
    before: float = None
    after: float = None
    top: float = None
    bottom: float = None
    left: float = None
    right: float = None
    page: int = None


PageTextPropertiesList = list[PageTextProperties]
TextProperties = list[TextProperty]


@dataclasses.dataclass
class DocTextStyle:
    text_size: float = None
    text_distance: float = None
    text_family: int = None

    text_left: float = None
    text_right: float = None
    text_width: float = None
    text_width_min: float = None
    text_width_max: float = None
    text_alignment: int = None

    h1_size: float = None
    h1_before: float = None
    h1_after: float = None
    h1_family: int = None

    h2_size: float = None
    h2_before: float = None
    h2_after: float = None
    h2_family: int = None

    h3_size: float = None
    h3_before: float = None
    h3_after: float = None
    h3_family: int = None

    h4_size: float = None
    h4_before: float = None
    h4_after: float = None
    h4_family: int = None

    pagenumber_size: float = None
    pagenumber_family: int = None

    footnote_size: float = None
    footnote_distance: float = None
    footnote_family: int = None

    list_size: float = None
    list_before: float = None  # distance to text
    list_distance: float = None  # distance in list items
    list_after: float = None  # distance to text
    list_family: int = None

    block_size: float = None
    block_before: float = None  # distance to text
    block_distance: float = None  # distance in list items
    block_after: float = None  # distance to text
    block_family: int = None
    block_left: float = None
    block_right: float = None

    page_width: float = None
    page_height: float = None

    page_rotated_width: float = None
    page_rotated_height: float = None

    content_left: float = None
    content_right: float = None
    content_top: float = None
    content_bottom: float = None

    content_rotated_left: float = None
    content_rotated_right: float = None
    content_rotated_top: float = None
    content_rotated_bottom: float = None

    def __str__(self):
        r"""\
        >>> str(DocTextStyle(text_size=12.2, h2_family=101221223))
        'text_size                 12.2\nh2_family                 101221223'
        """
        collected = [
            '{:<25} {}'.format(key, value)
            for key, value in dataclasses.asdict(self).items()
            if value is not None
        ]
        result = utila.NEWLINE.join(collected)
        return result
