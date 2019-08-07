# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

from functools import lru_cache

from configo import CACHE_MEDIUM
from utila import from_raw_or_path
from yaml import FullLoader
from yaml import dump
from yaml import load

from iamraw import BoundingBox
from iamraw import HyperLink
from iamraw import PageAnnotation
from iamraw import PageAnnotations
from iamraw import PageLink


def dump_annotations(annotations: PageAnnotations) -> str:
    """Convert PageAnnotations to raw data

    Write list with one PageAnnotation per Page when Page contains any
    Annotation.

    Args:
        annotations(PageAnnotations): list of PageAnnotation
    Returns:
        dumped raw data

    """
    raw = []
    for page in annotations:
        if not page.pagelinks and not page.hyperlinks:
            # skip empty pages
            continue
        rawpage = [{
            'goto': link.goal,
            'bounds': str(link.bounds),
        } for link in page.pagelinks]

        rawhyper = [{
            'href': link.goal,
            'bounds': str(link.bounds),
        } for link in page.hyperlinks]

        raw.append({
            'data': [
                rawpage,
                rawhyper,
            ],
            'page': page.page
        })
    dumped = dump(raw)
    return dumped


@lru_cache(CACHE_MEDIUM)
def load_annotations(content: str) -> PageAnnotations:
    """Load annotations from dumped raw data.

    Args:
        content(str): dumped raw data
    Returns:
        loaded PageAnnotations
    """
    content = from_raw_or_path(content, ftype='yaml')
    loaded = load(content, Loader=FullLoader)
    result = []
    for page in loaded:
        pagelinks = [
            PageLink(
                goal=item['goto'], bounds=BoundingBox.from_str(item['bounds']))
            for item in page['data'][0]
        ]
        hyperlinks = [
            HyperLink(
                goal=item['href'], bounds=BoundingBox.from_str(item['bounds']))
            for item in page['data'][1]
        ]
        result.append(PageAnnotation(
            pagelinks,
            hyperlinks,
            page['page'],
        ))
    return result
