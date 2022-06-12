# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import contextlib

import configo
import utila

import iamraw


def dump_likelihood(likelihoods: iamraw.PageContentLikelihoods) -> str:
    """Dump list of page likehoods"""
    result = []
    for page in likelihoods:
        assert isinstance(page, iamraw.PageContentLikelihood), type(page)
        content = page.content
        if not isinstance(content, list):
            content = [content]

        pageresult = []
        for single in content:
            item = {'value': single.value}
            if single.name:
                item['name'] = single.name
            pageresult.append(item)

        if not pageresult:
            continue

        result.append({
            'page': page.page,
            'content': pageresult,
        })
    dumped = utila.yaml_dump(result)
    return dumped


@configo.cache_small
def load_likelihood(
    content: str,
    singlevalue: bool = True,
    pages: tuple = None,
) -> iamraw.PageContentLikelihoods:
    """Load list of likelihoods from single `content`

    Args:
        content(str): dumped str data
        singlevalue(bool): if true, the PageContentLikelihood is converted to
                           single item instead of a list with one item
        pages(tuple): select pages to load; if None load all items
    Returns:
        List of loaded likelihood.
    """
    loaded = utila.yaml_load(
        content,
        safe=False,
    )
    result = []
    for page in loaded:
        pagenumber = page['page']
        if utila.should_skip(pagenumber, pages):
            continue
        content = page['content']
        pagecontent = []
        for item in content:
            value = item['value']
            hood = iamraw.Likelihood(value=value)
            with contextlib.suppress(KeyError):
                hood.name = item['name']
            pagecontent.append(hood)
        if len(pagecontent) == 1 and singlevalue:
            pagecontent = pagecontent[0]
        result.append(iamraw.PageContentLikelihood(pagenumber, pagecontent))
    return result
