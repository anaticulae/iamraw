# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
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

PageContentImageInfo = collections.namedtuple(
    'PageContentImageInfo',
    'content page',
)
PageContentImageInfos = list[PageContentImageInfo]


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


ImageInformations = list[ImageInformation]
