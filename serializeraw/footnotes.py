# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utila

import iamraw
import serializeraw


def load_footnotes(
        content: str,
        prefix: str = '',
        pages: tuple = None,
) -> iamraw.PageContentFootnotes:
    fname = 'groupme__footer_footerheader'
    if prefix:
        fname = fname.replace('groupme', f'groupme_{prefix}')
    content = utila.from_raw_or_path(content, fname=fname)
    loaded = serializeraw.load_headerfooter(content, pages=pages)
    result = []
    for item in loaded:
        try:
            selected = item.footer.notes
        except AttributeError:
            continue
        assert selected
        yrange = (item.footer.begin, item.footer.end)
        notes = iamraw.PageContentFootnote(
            content=selected,
            page=item.page,
            yrange=yrange,
        )
        result.append(notes)
    return result
