# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import configo
import utila

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
        assert isinstance(page, PageAnnotation), type(page)
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
    dumped = utila.yaml_dump(raw)
    return dumped


@configo.cache_medium
def load_annotations(content: str, pages=None) -> PageAnnotations:
    """Load annotations from dumped raw data.

    Args:
        content(str): dumped raw data
        pages(list): pages to load
    Returns:
        loaded PageAnnotations
    """
    loaded = utila.yaml_load(
        content,
        fname='annotation_annotation',
    )
    result = []
    for page in loaded:
        pagenumber = int(page['page'])
        if utila.should_skip(pagenumber, pages):
            continue
        pagelinks = [
            PageLink(
                goal=item['goto'],
                bounds=BoundingBox.from_str(item['bounds']),
            ) for item in page['data'][0]
        ]
        hyperlinks = [
            HyperLink(
                goal=item['href'],
                bounds=BoundingBox.from_str(item['bounds']),
            ) for item in page['data'][1]
        ]
        result.append(PageAnnotation(
            pagelinks,
            hyperlinks,
            pagenumber,
        ))
    return result
