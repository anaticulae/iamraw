# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import functools

import configo
import utila
import yaml

import iamraw
import serializeraw


def dump_textpositions(items: iamraw.PageContentTextPositions) -> str:
    result = []
    for page in items:
        pagenumber = page.page
        content = page.content
        if not content:
            continue
        raw = [
            f'{key} {raw_bounding(bounding)} {mean}'
            for key, (bounding, mean) in content.items()
        ]
        result.append({
            'content': raw,
            'page': pagenumber,
        })
    dumped = yaml.dump(result)
    dumped = serializeraw.dump_yamlpages(dumped)
    return dumped


@functools.lru_cache(configo.CACHE_SMALL)
def load_textpositions(
    content: str,
    pages=None,
) -> iamraw.PageContentTextPositions:
    fname = 'rawmaker__text_positions'
    content = serializeraw.load_yamlpages(
        content,
        pages=pages,
        fname=fname,
    )
    loaded = utila.yaml_load(
        content,
        fname=fname,
        safe=False,
    )
    result = []
    if not loaded:
        # if yamlpages selected no content, it is possible that loaded is
        # None.
        return result
    for page in loaded:
        pagenumber = int(page['page'])
        if utila.should_skip(pagenumber, pages):
            continue
        pagedata = {}
        for item in page['content']:
            key, data = item.split(maxsplit=1)
            bounding, mean = data.rsplit(maxsplit=1)
            mean = float(mean)
            pagedata[int(key)] = (iamraw.BoundingBox.from_str(bounding), mean)
        if not content:
            continue
        textposition = iamraw.PageContentTextPosition(
            content=pagedata,
            page=pagenumber,
        )
        result.append(textposition)
    return result


def raw_bounding(bounding) -> str:
    """Convert BoundingBox or tuple to str representation."""
    if isinstance(bounding, tuple):
        assert len(bounding) == 4
        return utila.from_tuple(bounding)
    # iamraw.BoundingBox
    return str(bounding)
