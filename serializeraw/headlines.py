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
from yaml import FullLoader
from yaml import dump
from yaml import load

from iamraw import Headline
from iamraw import PagesHeadlineList


def dump_headlines(headlines: PagesHeadlineList) -> str:
    raw = []
    for index, page in enumerate(headlines):
        content = [{
            'container': item.container,
            'level': item.level,
            'page': item.page,
            'rawlevel': item.rawlevel,
            'text': item.text,
        } for item in page]
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
def load_headlines(content: str) -> PagesHeadlineList:
    content = from_raw_or_path(content, ftype='yaml')
    loaded = load(content, Loader=FullLoader)
    result = []
    for page in loaded:
        step = []
        for headline in page['headlines']:
            step.append(
                Headline(
                    container=int(headline['container']),
                    level=int(headline['level']),
                    page=headline['page'],
                    rawlevel=headline['rawlevel'],
                    text=headline['text'],
                ))
        result.append(step)
    return result
