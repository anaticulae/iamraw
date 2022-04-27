# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utila

import iamraw


def dump_tables(pages: iamraw.PageContentTableBoundings) -> str:
    pages = sorted(pages, key=lambda x: x.page)
    result = []
    for page in pages:
        content = [{
            'lines': [tupleraw(line) for line in item.lines],
            'bounding': tupleraw(item.bounding),
        } for item in page.content]
        raw = {'page': page.page, 'content': content}
        result.append(raw)
    dumped = utila.yaml_dump(result)
    return dumped


def load_tables(
    content: str,
    pages: tuple = None,
) -> iamraw.PageContentTableBoundings:
    loaded = utila.yaml_load(
        content,
        fname='tablero__decide_decide',
        safe=False,
    )
    result = []
    for page in loaded:
        pagenumber = int(page['page'])
        if utila.should_skip(page=pagenumber, pages=pages):
            continue
        item = iamraw.PageContentTableBounding(page=pagenumber)
        for raw in page['content']:
            lines = [utila.parse_tuple(item) for item in raw['lines']]
            bounding = utila.parse_tuple(raw['bounding'])
            parsed = iamraw.TableBounding(
                bounding=bounding,
                lines=lines,
                page=pagenumber,
            )
            item.append(parsed)
        result.append(item)
    return result


def tupleraw(item) -> str:
    """\
    >>> tupleraw(iamraw.BoundingBox.from_str('10.22 50.33 20 60'))
    '10.22 50.33 20.0 60.0'
    >>> tupleraw((10.22, 50.33, 20.0, 60.0))
    '10.22 50.33 20.0 60.0'
    """
    item = utila.roundme(*item, digits=2, convert=False)
    return utila.from_tuple(item)
