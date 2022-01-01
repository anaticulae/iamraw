# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================
"""\
Compare ImageInformation `hashedimage` independent:
>>> hash(ImageInformation(hashedimage='first')) == hash(ImageInformation(hashedimage='second'))
True
>>> ImageInformation(hashedimage='first') == ImageInformation(hashedimage='second')
True
"""

import collections
import dataclasses
import typing

PageContentImageInfo = collections.namedtuple(
    'PageContentImageInfo',
    'content page',
)
PageContentImageInfos = typing.List[PageContentImageInfo]


@dataclasses.dataclass(unsafe_hash=True)
class ImageInformation:
    width: int = None
    height: int = None
    page: int = None
    dpi: tuple = None
    bounding: tuple = None
    hashedimage: str = dataclasses.field(default=None, hash=None, compare=False)
    figure: bool = False
    hidden: bool = False
    """Disable image to avoid further processing."""


ImageInformations = typing.List[ImageInformation]
