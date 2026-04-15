# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2022-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================
"""\
>>> CONTENT = '''
... Starter
... 1. Bestimme fur eine feste Anzahl von Beispielen (von jedem zu klassifizierenden Objekt) die
... Some Lines
... More Lines
... x-Vektoren.
... More'''.splitlines()
>>> DETECTED = '''
... Bestimme fur eine feste Anzahl von Beispielen (von jedem zu klassifizierenden Objekt) die
... x-Vektoren.'''.strip()
>>> search_area(CONTENT, DETECTED)
[2, 3, 4, 5]
"""

import utilo


def search_area(items: list, detected: str, startindex: int = 0) -> list:
    if not items:
        return []
    if not isinstance(items[0], str):
        items = [line.text for line in items]
    splitted = detected.splitlines()
    if len(splitted) == 1:
        start, end = splitted[0], splitted[0]
    else:
        start, end = splitted[0], splitted[-1]
    start = find_withbackup(items, start)
    end = find_withbackup(items, end)
    if not isinstance(start, int):
        utilo.error(f'could not find {start} in: {items}')
        return []
    if not isinstance(end, int):
        utilo.error(f'could not find {end} in: {items}')
        return []
    end = end + 1  # ranged list
    result = utilo.rlist(start + startindex, end + startindex)
    return result


def find_withbackup(items, find) -> int:
    for similar in (utilo.verysimilar, utilo.similar):
        for index, item in enumerate(items):
            if similar(item, find):
                return index
    return None
