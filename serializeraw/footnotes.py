# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utilo

import iamraw
import serializeraw


def load_footnotes(
    content: str,
    prefix: str = '',
    pages: tuple = None,
) -> iamraw.PageContentFootnotes:
    fname = 'groupme__footer_footerheader'  # TODO: REMOVE LATER
    if prefix:
        fname = fname.replace('groupme', f'groupme_{prefix}')
    fname = (  # pylint:disable=R0204
        'footnote__result_result',
        fname,
    )
    content = utilo.from_raw_or_path(content, fname=fname)
    # list is not hashable, therefore we convert to tuple for #
    # headerfooter loading.
    pages = utilo.ensure_tuple(pages)
    loaded = serializeraw.load_headerfooter(content, pages=pages)
    result = []
    for page in loaded:
        try:
            selected = page.footer.notes
        except AttributeError:
            continue
        assert selected
        yrange = utilo.roundme((page.footer.begin, page.footer.end))
        notes = iamraw.PageContentFootnote(
            content=selected,
            page=page.page,
            yrange=yrange,
        )
        result.append(notes)
    return result
