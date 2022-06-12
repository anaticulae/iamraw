# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import typing

import configo
import utila


def dump_chapter(chapters: typing.List[typing.Dict]) -> str:
    result = []
    for item in chapters:
        level, title, content = item['level'], item['title'], item['content']
        result.append({
            'level': level,
            'title': title,
            'content': content,
        })
    dumped = utila.yaml_dump(result)
    return dumped


@configo.cache_small
def load_chapter(content: str) -> typing.List[typing.Dict]:
    loaded = utila.yaml_load(content)
    return loaded
