# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import collections.abc

import configos
import utilo

import iamraw


def dump_lines(lines: iamraw.PageContentLines) -> str:
    lines = sorted(lines, key=lambda x: x.page)
    collected = []
    for page in lines:
        if not page.content:
            # skip empty page
            continue
        content = ['%.2f %.2f %.2f %.2f' % item for item in page.content]
        pageitem = {
            'page':page.page,
            'content':content,
        }
        if page.rotated:
            pageitem['rotated'] = 1
        collected.append(pageitem)
    dumped = utilo.yaml_dump(collected)
    return dumped


def load_lines(
    source: str,
    pages: tuple = None,
    prefix: str = '',
) -> iamraw.PageContentLines:
    prefix = f'{prefix}_' if prefix else ''
    loaded = utilo.yaml_load(
        source,
        fname=f'rawmaker__{prefix}line_line',
        safe=False,
    )
    result = []
    for page in loaded:
        pagenumber = int(page['page'])
        if utilo.should_skip(pagenumber, pages):
            continue
        content = []
        for raw in page['content']:
            item = utilo.parse_tuple(raw)
            content.append(item)
        rotated = utilo.str2bool(page.get('rotated', False))
        pageitem = iamraw.PageContentLine(
            page=pagenumber,
            content=content,
            rotated=rotated,
        )
        result.append(pageitem)
    return result


def dump_horizontals(pages: iamraw.PagesWithHorizontalList) -> str:
    assert isinstance(pages, collections.abc.Iterable), type(pages)
    collected = []
    for page in pages:
        if not page.content:
            continue  # skip empty pages
        horizontals = [str(horizontal.box) for horizontal in page.content]
        pageitem = {
            'page':page.page,
            'horizontals':horizontals,
        }
        if page.rotated:
            pageitem['rotated'] = 1
        collected.append(pageitem)
    dumped = utilo.yaml_dump(collected)
    return dumped


@configos.cache_small
def load_horizontals(
    content: str,
    pages=None,
    prefix='',
    width_min: int = 120,
) -> iamraw.PagesWithHorizontalList:
    """Load horizontals or verticals.

    A vertical is a horizontal on a rotated page.
    """
    prefix = f'{prefix}_' if prefix else ''
    loaded = utilo.yaml_load(
        content,
        fname=f'rawmaker__{prefix}horizontals_horizontals',
    )
    result = []
    for page in loaded:
        pagenumber = int(page['page'])
        if utilo.should_skip(pagenumber, pages):
            continue
        horizontals = [
            iamraw.HorizontalLine(
                iamraw.BoundingBox.from_list(utilo.parse_tuple(item)))
            for item in page['horizontals']
        ]
        # skip short horizontals
        horizontals = [item for item in horizontals if item.width >= width_min]
        if not horizontals:
            continue
        rotated = utilo.str2bool(page.get('rotated', False))
        item = iamraw.PageContentHorizontals(
            content=horizontals,
            page=pagenumber,
            rotated=rotated,
        )
        result.append(item)
    return result
