# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import collections

import configos
import utilo

import iamraw

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
                for index, (bounding, (*boxid, _content)) in enumerate(multiboxed): # yapf: disable
                    # TODO: REMOVE LATER
                    if len(boxid) > 1:
                        utilo.error(f'invalid boxid: {boxid} page:{page} index: {index}') # yapf:disable
                    boxid = boxid[0]
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
    return utilo.yaml_dump(raw)


@configos.cache_small
def load_boxedcontent(content: str, pages=None):
    loaded = utilo.yaml_load(content)
    pagedict = collections.defaultdict(list)
    for page in loaded:
        pagenumber = int(page['page'])
        if utilo.should_skip(pagenumber, pages):
            continue
        content = page['content']
        parsed = parse_boxed_page(content)
        pagedict[pagenumber].extend(parsed)
    result = []
    for page, value in pagedict.items():
        result.append((page, value))
    return result


def parse_boxed_page(content):
    result = []
    for item in content:
        multiboxed = []
        headlinenumber = item['headlinenumber']
        headlineblocknumber = item['headlineblocknumber']
        for single_collector in item['content']:
            boxed = []
            for multibox in single_collector:
                m_bounding = iamraw.BoundingBox.from_str(multibox['bounding'])
                m_content = multibox['content']
                boxid, _ = [  # boxid, index
                    int(item) for item in multibox['boxed_id'].split()
                ]
                m_content = [parse_box_content(item) for item in m_content]
                boxed.append((m_bounding, (boxid, m_content)))
            multiboxed.append(boxed)
        result.append((headlinenumber, headlineblocknumber, multiboxed))
    return result


def parse_box_content(line: str) -> tuple:
    """Returns:
        tuple of BoundingBox, undefined_index(int) and content(str)
    """
    splitted = line.split(maxsplit=5)
    bounding = iamraw.BoundingBox.from_str(' '.join(splitted[0:4]))
    return (bounding, int(splitted[4]), splitted[5])
