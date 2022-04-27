# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import collections
import dataclasses
import enum
import typing


class CaptionType(enum.Enum):
    CODE = enum.auto()
    FIGURE = enum.auto()
    TABLE = enum.auto()
    UNDEFINED = enum.auto()


@dataclasses.dataclass
class Caption:
    line: int = None
    lineend: int = None
    number: int = None
    label: str = None
    text: str = None
    raw: str = None
    # 0 top, 1 right, 2 bottom, 3 left
    position: float = None
    typ: CaptionType = None
    pdfpage: int = None
    """Caption is printed on next page."""
    overlap: bool = False
    bounding: 'BoundingBox' = None
    """Table, Figure or Codeblock where caption references."""
    reference: int = None


Captions = typing.List[Caption]

PageContentCaption = collections.namedtuple(
    'PageContentCaption',
    'page content',
)
PageContentCaptions = typing.List[PageContentCaption]


def pagecaptions_toraw(pagecaptions: PageContentCaptions) -> list:
    result = []
    for item in pagecaptions:
        pagecontent = item.content
        if not pagecontent:
            continue
        collected = [caption_toraw(it) for it in pagecontent]
        result.append({
            'page': item.page,
            'captions': collected,
        })
    return result


def caption_toraw(caption: Caption) -> dict:
    """\
    >>> caption_toraw(Caption(line=3, lineend=5, raw='I am a caption'))
    {'line': 3, 'raw': 'I am a caption', 'lineend': 5}
    """
    assert caption.line is not None
    result = {
        'line': caption.line,
        'raw': caption.raw,
    }
    if caption.lineend is not None:
        result['lineend'] = caption.lineend
    if caption.position is not None:
        result['position'] = caption.position
    if caption.bounding is not None:
        result['bounding'] = str(caption.bounding)
    if caption.reference is not None:
        result['reference'] = str(caption.reference)
    return result
