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


def dump_headlines(headlines: iamraw.PagesHeadlineList) -> str:
    raw = []
    for index, page in enumerate(headlines):
        content = []
        for item in page:
            container = item.container
            if isinstance(container, tuple):
                container = utila.from_tuple(container)
            content.append({
                'container': container,
                'level': item.level,
                'page': item.page,
                'raw': item.raw,
                'raw_level': item.raw_level,
                'title': item.title,
                'decoration': item.decoration,
            })
        if not content:
            # do not write empty pages
            continue
        raw.append({
            'chapter?': index,  # TODO: How to deal with empty chapter?
            'headlines': content,
        })
    dumped = yaml.safe_dump(raw)
    return dumped


@functools.lru_cache(configo.CACHE_SMALL)
def load_headlines(content: str, pages=None) -> iamraw.PagesHeadlineList:
    content = utila.from_raw_or_path(
        content,
        fname='words__headlines_headlines',
        ftype='yaml',
    )
    loaded = yaml.safe_load(content)
    result = []
    for step in loaded:
        loadedstep = []
        for headline in step['headlines']:
            pagenumber = int(headline['page'])
            if utila.should_skip(pagenumber, pages):
                continue
            try:
                container = int(headline['container'])
            except ValueError:
                # support ranged container id
                container = utila.parse_tuple(  # pylint:disable=R0204
                    headline['container'],
                    length=2,
                    typ=int,
                )
            level = headline['level']
            if level is not None:
                level = int(level)
            else:
                utila.error(f'headline level is None: {headline["title"]}')
            item = iamraw.Headline(
                container=container,
                level=level,
                page=pagenumber,
                raw=headline['raw'],
                raw_level=headline['raw_level'],
                title=headline['title'],
                decoration=headline.get('decoration', None),
            )
            loadedstep.append(item)
        if loadedstep:
            result.append(loadedstep)
    return result
