# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import functools

import configo
import utila
import yaml

from iamraw.sections import AbbreviationTable
from iamraw.sections import Abstract
from iamraw.sections import Appendix
from iamraw.sections import Bibliography
from iamraw.sections import Chapter
from iamraw.sections import DocumentSection
from iamraw.sections import FigureTable
from iamraw.sections import Glossary
from iamraw.sections import Index
from iamraw.sections import Introduction
from iamraw.sections import LegalInformation
from iamraw.sections import MainPart
from iamraw.sections import MultipleSection
from iamraw.sections import NotImplementedItem
from iamraw.sections import Sections
from iamraw.sections import SymbolTable
from iamraw.sections import Table
from iamraw.sections import TableOfContent
from iamraw.sections import TableTable
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
    # selective page inside
    >>> inside_section({'start' : 0, 'end': 4}, pages=(3, 4, 5))
    ([3], (0, 1, 2, 3))

    # single page selected
    >>> inside_section({'start' : 2, 'end': 2}, pages=(1, 2, 3, 4))
    ([2], (2,))

    # no page inside
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
        result = NotImplementedItem(classname=classname, **result)
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


def generate_ctor():
    """Create table with name[constructor]."""
    # TODO: automate this
    items = [
        AbbreviationTable,
        Abstract,
        Appendix,
        Bibliography,
        Chapter,
        DocumentSection,
        FigureTable,
        Glossary,
        Index,
        Introduction,
        LegalInformation,
        MainPart,
        MultipleSection,
        Sections,
        SymbolTable,
        Table,
        TableOfContent,
        TableTable,
        Text,
        TitlePage,
        Unknown,
        WhitePage,
    ]
    return {str(item.__name__): item for item in items}


# lookuptable with constructor to create objects out of raw information
CTOR = generate_ctor()
