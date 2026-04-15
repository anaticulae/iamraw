# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import contextlib

import configo
import utilo

import iamraw


def dump_headlines(headlines: iamraw.PagesHeadlineList) -> str:
    collected = []
    for group in headlines:
        if not group:
            continue
        content = [headline_raw(headline) for headline in group]
        collected.append({
            'headlines': content,
        })
    strategy = None
    with contextlib.suppress(AttributeError):
        strategy = headlines.__strategy__
    confidence = None
    with contextlib.suppress(AttributeError):
        confidence = headlines.confidence
    result = dict(
        __strategy__=strategy,
        confidence=confidence,
        headlines=collected,
    )
    dumped = utilo.yaml_dump(result)
    return dumped


@configo.cache_small
def load_headlines(
    content: str,
    pages=None,
    *,
    oneline: bool = False,
) -> iamraw.PagesHeadlineList:
    fname = 'words__headlines_headlines'
    if oneline:
        fname = 'words__headlines_oneline'
    loaded = utilo.yaml_load(
        content,
        fname=fname,
    )
    if isinstance(loaded, list):
        # TODO: REMOVE LATER
        content = loaded
        strategy = None
        confidence = 1.0
    else:
        strategy = loaded.get('__strategy__', None)
        confidence = loaded.get('confidence', None)
        content = loaded.get('headlines')
    collected = []
    for step in content:
        loadedstep = []
        for rawheadline in step['headlines']:
            pagenumber = int(rawheadline['page'])
            if utilo.should_skip(pagenumber, pages):
                continue
            headline = headline_fromraw(rawheadline)
            loadedstep.append(headline)
        if not loadedstep:
            continue
        collected.append(iamraw.HeadlineGroup(headlines=loadedstep))
    result = iamraw.HeadlineResult(
        groups=collected,
        confidence=confidence,
    )
    result.__strategy__ = strategy
    return result


def headline_fromraw(headline: dict) -> iamraw.Headline:
    try:
        container = int(headline['container'])
    except ValueError:
        # support ranged container id
        container = utilo.parse_tuple(  # pylint:disable=R0204
            headline['container'],
            length=2,
            typ=int,
        )
    level = headline['level']
    if level is not None:
        level = int(level)
    else:
        utilo.error(f'headline level is None: {headline["title"]}')
    pagenumber = int(headline['page'])
    item = iamraw.Headline(
        container=container,
        level=level,
        page=pagenumber,
        raw=headline['raw'],
        raw_level=headline['raw_level'],
        title=headline['title'],
        decoration=headline.get('decoration', None),
    )
    return item


def headline_raw(item) -> dict:
    container = item.container
    if isinstance(container, tuple):
        container = utilo.from_tuple(container)
    result = {
        'container': container,
        'level': item.level,
        'page': item.page,
        'raw': item.raw,
        'raw_level': item.raw_level,
        'title': item.title,
        'decoration': item.decoration,
    }
    return result
