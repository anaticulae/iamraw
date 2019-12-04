# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

from typing import List

from utila import flatten
from utila import from_raw_or_path
from utila import should_skip
from yaml import FullLoader
from yaml import dump
from yaml import load

from iamraw import ChapterText
from iamraw import Headline
from iamraw import PagesHeadlineList


def dump_text(text: List[ChapterText]) -> str:
    raw = []
    index = 0
    for (page, content) in text:
        collector = []
        for headline, headline_content in content:
            current = {
                # placeholder headline
                'headline': None,
                'fc': headline.container,
                'content': [],
            }
            if headline.text is not None:
                current['headline'] = index
                index += 1
            for oneline in headline_content:
                current['content'].append(oneline)
            collector.append(current)
        raw.append({
            'page': page,
            'content': collector,
        })
    dumped = dump(raw)
    return dumped


def load_text(
        content: str,
        headlines: PagesHeadlineList,
        pages=None,
) -> List[ChapterText]:
    """Load text and replace headline reference with current headline

    Args:
        content(str): path to dumped text
        headlines(PagesHeadlineList): list of page with list of headlines
        pages(tuple): load all if None or load selected one.
    Returns:
        loaded text with replaced headlines
    """
    content = from_raw_or_path(content, ftype='yaml')
    loaded = load(content, Loader=FullLoader)

    # convert page index to global index
    headlines = flatten(headlines)

    result = []
    for line in loaded:
        page, content = int(line['page']), line['content']
        if should_skip(page, pages):
            continue
        pagecontent = []
        for section in content:
            section_content, headline = section['content'], section['headline']
            headline = headlines[headline] if headline is not None else None
            if headline is None:
                headline = Headline(
                    text=None,
                    level=None,
                    rawlevel=None,
                    page=page,
                    container=section['fc'])
            pagecontent.append((headline, section_content))

        result.append((page, pagecontent))
    return result
