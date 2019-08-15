# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

from collections import defaultdict
from functools import lru_cache

from configo import CACHE_SMALL
from utila import from_raw_or_path
from utila import should_skip
from yaml import FullLoader
from yaml import dump
from yaml import load

from iamraw import BoundingBox

# TODO: not very nice, yet.


def dump_boxedcontent(boxed) -> str:

    # headlinenumber,
    # headlineblocknumber,
    # collected,

    # BoundingBox
    # boxid, content
    raw = []
    for (page, pagecontent) in boxed:
        pageresult = []
        for (headlinenumber, headlineblocknumber, collected) in pagecontent:
            # for (bounding, blockcontent) in collected:
            # more than one box in a box-container:
            # content, box, box, content, box, content
            single_collector = []  # crazy naming!
            for multiboxed in collected:
                items = []
                for index, item in enumerate(multiboxed):
                    bounding, (boxid, _content) = item
                    items.append({
                        'boxed_id':
                        '%d %d' % (boxid, index),
                        'bounding':
                        str(bounding),
                        'content': [
                            '%s %d %s' % (str(bounding), uindex, contentitem)
                            for (bounding, uindex, contentitem) in _content
                        ]
                    })
                single_collector.append(items)
            pageresult.append({
                'headlinenumber': headlinenumber,
                'headlineblocknumber': headlineblocknumber,
                'content': single_collector,
            })

        raw.append({
            'page': page,
            'content': pageresult,
        })

    dumped = dump(raw)
    return dumped


@lru_cache(CACHE_SMALL)
def load_boxedcontent(content: str, pages=None):

    def _parse_box_content(line: str):
        """Returns:
            bounding(BoundingBox):
            undefined_index(int):
            content(str):
        """
        splitted = line.split(maxsplit=5)
        bounding = BoundingBox.from_str(' '.join(splitted[0:4]))
        return (bounding, int(splitted[4]), splitted[5])

    content = from_raw_or_path(content, ftype='yaml')
    loaded = load(content, Loader=FullLoader)
    pagedict = defaultdict(list)
    for line in loaded:
        pagenumber = int(line['page'])
        if should_skip(pagenumber, pages):
            continue
        for item in line['content']:
            multiboxed = []
            headlinenumber = item['headlinenumber']
            headlineblocknumber = item['headlineblocknumber']
            for single_collector in item['content']:
                boxed = []
                for multibox in single_collector:
                    m_bounding = BoundingBox.from_str(multibox['bounding'])
                    m_content = multibox['content']
                    boxid, _ = [  # boxid, index
                        int(item) for item in multibox['boxed_id'].split()
                    ]
                    m_content = [_parse_box_content(item) for item in m_content]
                    boxed.append((m_bounding, (boxid, m_content)))
                multiboxed.append(boxed)
            pagedict[pagenumber].append((
                headlinenumber,
                headlineblocknumber,
                multiboxed,
            ))
    result = []
    for page, value in pagedict.items():
        result.append((page, value))
    return result
