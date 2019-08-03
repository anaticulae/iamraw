# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

from functools import lru_cache

from configo import CACHE_SMALL
from utila import from_raw_or_path
from yaml import FullLoader
from yaml import dump
from yaml import load

from iamraw.sections import Appendix
from iamraw.sections import Chapter
from iamraw.sections import Content
from iamraw.sections import DocumentSection
from iamraw.sections import Index
from iamraw.sections import Introduction
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
    """Convert `Sections` to raw data"""

    def dump_item(item):
        keys = [key for key in dir(item) if not key.startswith(SEPCIALFIELD)]
        result = {key: item.__getattribute__(key) for key in keys}
        result[CLASSNAME] = item.__class__.__name__
        return result

    result = []
    for page in sections:
        content = dump_item(page)
        content['content'] = [dump_item(item) for item in page.content]
        result.append(content)
    dumped = dump(result)
    return dumped


@lru_cache(CACHE_SMALL)
def load_sections(content: str) -> Sections:
    """Load sections from path or str

    Args:
        content(str):
    Return:
        loaded Sections
    """
    content = from_raw_or_path(content, ftype='yaml')
    loaded = load(content, Loader=FullLoader)

    def generate_ctor():
        """Create table with name[constructor]"""
        items = [
            Appendix,
            Chapter,
            Content,
            DocumentSection,
            Index,
            Introduction,
            Sections,
            Table,
            TableOfContent,
            Text,
            TitlePage,
            Unknown,
            WhitePage,
        ]
        return {str(item.__name__): item for item in items}

    _ctor = generate_ctor()

    def load_item(item):

        def determine_type(item):
            """Load items, in special a list entry"""
            if isinstance(item, list):
                # recursive call
                return [load_item(single) for single in item]
            return item

        result = {
            key: determine_type(item[key])
            for key in item.keys()
            if not key.startswith(SEPCIALFIELD)
        }

        ctor = _ctor[item[CLASSNAME]]
        result = ctor(**result)
        return result

    result = Sections()
    for section in loaded:
        result.append(load_item(section))
    return result
