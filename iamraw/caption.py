# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import collections
import dataclasses
import typing


@dataclasses.dataclass
class Caption:
    line: int = None
    lineend: int = None
    raw: str = None
    # 0 top, 1 right, 2 bottom, 3 left
    position: float = None
    # TODO: ADD BOUNDING?


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
    return result
