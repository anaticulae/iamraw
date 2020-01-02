# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

from functools import lru_cache
from typing import Dict
from typing import List

from configo import CACHE_SMALL
from utila import from_raw_or_path
from yaml import FullLoader
from yaml import dump
from yaml import load


def dump_chapter(chapters: List[Dict]) -> str:
    result = []
    for item in chapters:
        level, title, content = item['level'], item['title'], item['content']
        result.append({
            'level': level,
            'title': title,
            'content': content,
        })
    dumped = dump(result)
    return dumped


@lru_cache(CACHE_SMALL)
def load_chapter(content: str) -> List[Dict]:
    content = from_raw_or_path(content, ftype='yaml')
    loaded = load(content, Loader=FullLoader)
    return loaded
