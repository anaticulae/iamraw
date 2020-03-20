# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import functools

import configo
import utila
import yaml

from iamraw.sections import Appendix
from iamraw.sections import Chapter
from iamraw.sections import DocumentSection
from iamraw.sections import Index
from iamraw.sections import Introduction
from iamraw.sections import MainPart
from iamraw.sections import MultipleSection
from iamraw.sections import NotImplementedItem
from iamraw.sections import Sections
from iamraw.sections import Table
from iamraw.sections import TableOfContent
from iamraw.sections import Text
from iamraw.sections import TitlePage
from iamraw.sections import Unknown
from iamraw.sections import WhitePage

CLASSNAME = '__class__'
SEPCIALFIELD = '__'


def dump_sections(sections: Sections) -> str:
    """Convert `Sections` to raw data."""
    result = []
    for page in sections:
        content = dump_item(page)
        content['content'] = [dump_item(item) for item in page.content]
        result.append(content)
    dumped = yaml.dump(result)
    return dumped


@functools.lru_cache(configo.CACHE_SMALL)
def load_sections(
        content: str,
        onerror: callable = None,
        pages: tuple = None,
) -> Sections:
    """Load sections from path or str.

    Args:
        content(str): path or yaml representation of `Sections`
        pages(tuple): tuple of page numbers to load - if none, load all
        onerror(callable): if `CTOR` is not found, onerror is called for
                           a second try.
    Return:
        loaded Sections
    """
    content = utila.from_raw_or_path(content, ftype='yaml')
    loaded = yaml.load(content, Loader=yaml.FullLoader)

    result = Sections()
    for section in loaded:
        start, end = section['start'], section['end']
        section_pages = range(start, end + 1)
        inside = [
            page for page in section_pages
            if not utila.should_skip(page, pages)
        ]
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
            return [load_item(single) for single in item]
        return item

    result = {
        key: determine_type(item[key])
        for key in item.keys()
        if not key.startswith(SEPCIALFIELD)
    }
    try:
        ctor = CTOR[item[CLASSNAME]]
    except KeyError:
        ctor = None
    if ctor is None and onerror:
        # error handling
        ctor = onerror(CLASSNAME)
    if ctor is None:
        result = NotImplementedItem(name=CLASSNAME)
        utila.error(f'section `{CLASSNAME}` not supported - use default')
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


def generate_ctor():
    """Create table with name[constructor]."""
    items = [
        Appendix,
        Chapter,
        DocumentSection,
        Index,
        Introduction,
        MainPart,
        MultipleSection,
        Sections,
        Table,
        TableOfContent,
        Text,
        TitlePage,
        Unknown,
        WhitePage,
    ]
    return {str(item.__name__): item for item in items}


# lookuptable with constructor to create objects out of raw information
CTOR = generate_ctor()
