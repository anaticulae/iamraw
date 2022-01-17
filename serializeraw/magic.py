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


def load_magic_types(
    content: str,
    pages: tuple = None,
) -> iamraw.PageContentContentTypes:
    content = utila.from_raw_or_path(
        content,
        fname='magic__content_content',
        ftype='yaml',
    )
    loaded = utila.yaml_load(content)

    result = []
    for page, pagecontent in loaded:
        if utila.should_skip(page, pages):
            continue
        parsed = types_fromstr(pagecontent)
        result.append(iamraw.PageContentContentType(page=page, content=parsed))
    return result


load_types = load_magic_types  # pylint:disable=C0103


def dump_magic_types(items: iamraw.PageContentContentTypes) -> str:
    result = [(page, types_tostr(content)) for page, content in items]
    # remove empty pages:
    result = [item for item in result if item[1]]
    dumped = utila.yaml_dump(result)
    return dumped


dump_types = dump_magic_types  # pylint:disable=C0103


def types_fromstr(content: list) -> list:
    """\
    >>> types_fromstr(['5 TEXT', '10 UNDEFINED'])
    [(5, <PageContentType.TEXT: ...>), (10, <PageContentType.UNDEFINED: ...>)]
    """
    result = []
    for item in content:
        number, value = item.split()
        number, value = int(number), iamraw.PageContentType[value]
        result.append((number, value))
    return result


def types_tostr(items) -> str:
    """\
    >>> types_tostr([(3, iamraw.PageContentType.TEXT),
    ...             (2, iamraw.PageContentType.UNDEFINED)])
    ['3 TEXT', '2 UNDEFINED']
    """
    result = [f'{index} {item.name}' for index, item in items]
    return result
