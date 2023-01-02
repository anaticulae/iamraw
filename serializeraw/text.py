# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utila

import iamraw


def dump_text(text: iamraw.PageContentTexts) -> str:
    raw = []
    for item in text:
        collected = []
        for headline, headline_content in item.content:
            current = {
                # placeholder headline
                'headline': None,
                'fc': headline.container if headline else None,
                'content': [],
            }
            if headline and headline.title is not None:
                current['headline'] = headline.identifier
            for oneline in headline_content:
                current['content'].append(oneline)
            collected.append(current)
        raw.append({
            'page': item.page,
            'content': collected,
        })
    dumped = utila.yaml_dump(raw)
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
    loaded = utila.yaml_load(
        content,
        fname='words__text_text',
        safe=False,
    )
    if headlines is None:
        utila.debug('load_text without any given headlines')
    else:
        headlines = {
            headline.identifier: headline for headline in utila.flat(headlines)
        }
    result = []
    for line in loaded:
        page, content = int(line['page']), line['content']
        if utila.should_skip(page, pages):
            continue
        pagecontent = []
        for section in content:
            section_content = section['content']
            headline = None
            if headlines:
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
    selected = section['headline']
    try:
        selected = headlines[selected]
    except KeyError:
        if selected is not None:
            # None-Headline is expected on page start?
            msg = f'could not load headline: {selected} on page:{page}'
            utila.error(msg)
        selected = None
    if selected:
        return selected
    result = iamraw.Headline(
        title=None,
        level=None,
        raw_level=None,
        page=page,
        container=section.get('fc', None),
    )
    return result
