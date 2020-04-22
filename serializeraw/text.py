# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utila
import yaml

import iamraw


def dump_text(text: iamraw.ChapterTextList) -> str:
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
    dumped = yaml.dump(raw)
    return dumped


def load_text(
        content: str,
        headlines: iamraw.PagesHeadlineList = None,
        pages=None,
) -> iamraw.ChapterTextList:
    """Load text and replace headline reference with current headline

    Args:
        content(str): path to dumped text
        headlines(PagesHeadlineList): list of page with list of headlines
        pages(tuple): load all if None or load selected one.
    Returns:
        loaded text with replaced headlines
    """
    content = utila.from_raw_or_path(content, ftype='yaml')
    loaded = yaml.load(content, Loader=yaml.FullLoader)

    # convert page index to global index
    headlines = utila.flatten(headlines)

    result = []
    for line in loaded:
        page, content = int(line['page']), line['content']
        if utila.should_skip(page, pages):
            continue
        pagecontent = []
        for section in content:
            section_content, headline = section['content'], section['headline']
            headline = headlines[headline] if headlines is not None else None
            if headline is None:
                headline = iamraw.Headline(
                    text=None,
                    level=None,
                    rawlevel=None,
                    page=page,
                    container=section['fc'],
                )
            pagecontent.append((headline, section_content))

        result.append((page, pagecontent))
    return result
