# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utila
import yaml

import iamraw


def dump_text(text: iamraw.PageContentTexts) -> str:
    raw = []
    index = 0
    for item in text:
        collected = []
        for headline, headline_content in item.content:
            current = {
                # placeholder headline
                'headline': None,
                'fc': headline.container,
                'content': [],
            }
            if headline.title is not None:
                current['headline'] = index
                index += 1
            for oneline in headline_content:
                current['content'].append(oneline)
            collected.append(current)
        raw.append({
            'page': item.page,
            'content': collected,
        })
    dumped = yaml.dump(raw)
    return dumped


def load_text(
    content: str,
    headlines: iamraw.PagesHeadlineList = None,
    pages=None,
) -> iamraw.PageContentTexts:
    """Load text and replace headline reference with current headline

    Args:
        content(str): path to dumped text
        headlines(PagesHeadlineList): list of page with list of headlines
        pages(tuple): load all if None or load selected one.
    Returns:
        loaded text with replaced headlines
    """
    loaded = utila.yaml_from_raw_or_path(
        content,
        fname='words__text_text',
        safe=False,
    )
    # convert page index to global index
    headlines = utila.flatten(headlines) if headlines is not None else None
    result = []
    for line in loaded:
        page, content = int(line['page']), line['content']
        if utila.should_skip(page, pages):
            continue
        pagecontent = []
        for section in content:
            section_content = section['content']
            headline = select_headline(headlines, section, page)
            pagecontent.append(
                iamraw.TextSection(
                    headline=headline,
                    content=section_content,
                    pages=[page] * len(section_content),
                ))
        result.append(iamraw.PageContentText(
            page=page,
            content=pagecontent,
        ))
    return result


def select_headline(
    headlines,
    section,
    page,
) -> iamraw.Headline:
    headline_selected = section['headline']
    try:
        headline_selected = headlines[headline_selected]
    except (IndexError, TypeError):
        if headline_selected is not None:
            # None-Headline is expected on page start?
            msg = f'could not load headline: {headline_selected} on page:{page}'
            utila.error(msg)
        headline_selected = None
    if headline_selected is None:
        headline_selected = iamraw.Headline(
            title=None,
            level=None,
            raw_level=None,
            page=page,
            container=section['fc'],
        )
    return headline_selected
