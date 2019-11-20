# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================
from functools import lru_cache

from configo import CACHE_SMALL
from utila import from_raw_or_path
from utila import should_skip
from yaml import FullLoader
from yaml import dump
from yaml import load

from iamraw import Headline
from iamraw import PagesHeadlineList


def dump_headlines(headlines: PagesHeadlineList) -> str:
    raw = []
    for index, page in enumerate(headlines):
        content = []
        for item in page:
            container = item.container
            if isinstance(container, tuple):
                container = ' '.join([str(item) for item in container])
            content.append({
                'container': container,
                'level': item.level,
                'page': item.page,
                'rawlevel': item.rawlevel,
                'text': item.text,
            })
        if not content:
            # do not write empty pages
            continue
        raw.append({
            'chapter?': index,  # TODO: How to deal with empty chapter?
            'headlines': content,
        })
    dumped = dump(raw)
    return dumped


@lru_cache(CACHE_SMALL)
def load_headlines(content: str, pages=None) -> PagesHeadlineList:
    content = from_raw_or_path(content, ftype='yaml')
    loaded = load(content, Loader=FullLoader)
    result = []
    for step in loaded:
        loadedstep = []
        for headline in step['headlines']:
            pagenumber = int(headline['page'])
            if should_skip(pagenumber, pages):
                continue
            try:
                container = int(headline['container'])
            except ValueError:
                # support ranged container id
                container = [
                    int(index) for index in headline['container'].split()
                ]
                container = tuple(container)  # pylint:disable=R0204
            item = Headline(
                container=container,
                level=int(headline['level']),
                page=pagenumber,
                rawlevel=headline['rawlevel'],
                text=headline['text'],
            )
            loadedstep.append(item)
        if loadedstep:
            result.append(loadedstep)
    return result
