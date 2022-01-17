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

import iamraw.sections

CLASSNAME = '__class__'
SEPCIALFIELD = '__'


def dump_sections(sections: iamraw.sections.Sections) -> str:
    """Convert `Sections` to raw data."""
    result = []
    for page in sections:
        content = dump_item(page)
        content['content'] = [dump_item(item) for item in page.content]
        result.append(content)
    dumped = utila.yaml_dump(result)
    return dumped


@functools.lru_cache(configo.CACHE_SMALL)
def load_sections(
    content: str,
    onerror: callable = None,
    pages: tuple = None,
) -> iamraw.sections.Sections:
    """Load sections from path or str.

    Args:
        content(str): path or yaml representation of `Sections`
        pages(tuple): tuple of page numbers to load - if none, load all
        onerror(callable): if `CTOR` is not found, onerror is called for
                           a second try.
    Return:
        loaded Sections
    """
    loaded = utila.yaml_load(
        content,
        fname='sections__section_result',
        safe=False,
    )
    result = iamraw.sections.Sections()
    for section in loaded:
        inside, section_pages = inside_section(section, pages)
        if not inside:
            # no part of current section is inside
            continue
        if len(section_pages) == len(inside):
            # every page of section is inside, add all
            result.append(load_item(section, onerror=onerror))
            continue
        # some parts are inside, shrink section with reduced content
        complete = load_item(section, onerror=onerror)
        shrinked = shrink_section(complete, pages)
        result.append(shrinked)
    return result


def inside_section(section: dict, pages: tuple) -> list:
    """\
    selective page inside
    >>> inside_section({'start' : 0, 'end': 4}, pages=(3, 4, 5))
    ([3], (0, 1, 2, 3))

    single page selected
    >>> inside_section({'start' : 2, 'end': 2}, pages=(1, 2, 3, 4))
    ([2], (2,))

    no page inside
    >>> inside_section({'start' : 2, 'end': 10}, pages=(12, 13, 14))
    ([], (2, 3, 4, 5, 6, 7, 8, 9))
    """
    start, end = section['start'], section['end']
    if start == end:
        end = end + 1
    section_pages = tuple(range(start, end))
    inside = [
        page for page in section_pages if not utila.should_skip(page, pages)
    ]
    return inside, section_pages


def dump_item(item):
    keys = [key for key in dir(item) if not key.startswith(SEPCIALFIELD)]
    result = {
        key: (item.__getattribute__(key)
              if key != 'content' else [dump_item(it) for it in item.content])
        for key in keys
        if not callable(item.__getattribute__(key))
    }
    result[CLASSNAME] = item.__class__.__name__
    return result


def load_item(item, onerror: callable = None):

    def determine_type(item):
        """Load items, in special a list entry."""
        if isinstance(item, list):
            # recursive call
            return [load_item(single, onerror=onerror) for single in item]
        return item

    result = {
        key: determine_type(item[key])
        for key in item.keys()
        if not key.startswith(SEPCIALFIELD)
    }
    classname = item[CLASSNAME]
    try:
        ctor = CTOR[classname]
    except KeyError:
        ctor = None
    if ctor is None and onerror:
        # error handling
        ctor = onerror(classname)
    if ctor is None:
        result = iamraw.sections.NotImplementedItem(
            classname=classname,
            **result,
        )
        utila.error(f'section `{classname}` not supported - use default')
    else:
        result = ctor(**result)  # pylint:disable=not-a-mapping
    return result


def shrink_section(section, pages: tuple):
    """Shrink content `section` to selected `pages`."""
    section_pages = range(section.start, section.end + 1)
    inside = [
        page for page in section_pages if not utila.should_skip(page, pages)
    ]
    # adjust border to new border
    section.start, section.end = min(inside), max(inside)
    # shrink to new border
    section.content = [
        item for item in section.content
        if item.start >= section.start and item.end <= section.end
    ]
    return section


# Create table with name[constructor].
# lookuptable with constructor to create objects out of raw information
CTOR = utila.name_classes(utila.collect_classes(iamraw.sections))
