# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import contextlib
import functools

import configo
import utila
import yaml

import iamraw
import serializeraw


def dump_headerfooter(pages: iamraw.PageContentFooterHeaders) -> str:
    serializeraw.validate(pages)
    result = []
    for page in pages:
        raw_header = _dump_header(page.header)
        raw_footer = _dump_footer(page.footer)

        result.append({
            'page': page.page,
            'header': raw_header,
            'footer': raw_footer,
        })
    return yaml.dump(result)


@functools.lru_cache(maxsize=configo.CACHE_SMALL)
def load_headerfooter(
    content: str,
    pages=None,
) -> iamraw.PageContentFooterHeaders:
    loaded = utila.yaml_from_raw_or_path(
        content,
        fname='groupme__footer_footerheader',
        safe=False,
    )
    result = []
    for item in loaded:
        pagenumber = item['page']
        assert isinstance(pagenumber, int)

        if utila.should_skip(pagenumber, pages):
            continue

        header = _load_header(item['header'])
        footer = _load_footer(item['footer'])

        footerheader = iamraw.PageContentFooterHeader(
            header=header,
            footer=footer,
            page=pagenumber,
        )
        result.append(footerheader)
    serializeraw.validate(result)
    return result


def dump_footnote(note: iamraw.FootNote):
    assert note.number is not None, note
    with contextlib.suppress(AttributeError):
        assert note.text, note
    raw = {key: value for key, value in vars(note).items() if value is not None}
    return raw


def load_footnote(raw: dict) -> iamraw.FootNote:
    with contextlib.suppress(TypeError):
        return iamraw.FootRawNote(**raw)
    with contextlib.suppress(TypeError):
        return iamraw.FootJudgedNote(**raw)
    raise ValueError(f'not supported: {raw}')


def _dump_footer(footer):
    if not footer:
        return None
    raw = {
        'begin': footer.begin,
        'end': footer.end,
    }
    if footer.page is not None:
        raw['page_value'] = footer.page.value
        raw['page_raw'] = footer.page.raw

    if isinstance(footer, iamraw.MovingFooterInformation):
        # dump footnotes
        notes = [dump_footnote(item) for item in footer.notes]
        raw['notes'] = notes

    if isinstance(footer, iamraw.PagesFooterInformation):
        if footer.page_location is not None:
            raw['page_location'] = str(footer.page_location)
        else:
            raw['page_location'] = None

    return raw


def _load_footer(raw) -> iamraw.FooterInformation:
    if not raw:
        return None
    begin = raw['begin']
    end = raw['end']

    page = None
    with contextlib.suppress(KeyError):
        page = iamraw.PageInformation(
            value=raw['page_value'],
            raw=raw['page_raw'],
        )

    # try to export MovingFooterInformation
    with contextlib.suppress(KeyError):
        notes = raw['notes']
        notes = [load_footnote(item) for item in notes]
        result = iamraw.MovingFooterInformation(
            begin=begin,
            end=end,
            notes=notes,
        )
        return result

    # try to export PagesFooterInformation
    with contextlib.suppress(KeyError):
        page_location = raw['page_location']
        if page_location is not None:
            page_location = iamraw.BoundingBox.from_str(page_location)
        result = iamraw.PagesFooterInformation(  # pylint:disable=R0204
            begin=begin,
            end=end,
            page_location=page_location,
        )
        if page is not None:
            result.page = page
        return result

    # try to export FixedFooterInformation
    result = iamraw.FixedFooterInformation(
        begin=begin,
        end=end,
    )

    return result


def _dump_header(header):
    if not header:
        return None
    raw = {
        'begin': header.begin,
        'end': header.end,
        'page': _dump_pageinformation(header.page)
    }

    with contextlib.suppress(KeyError):
        raw['undefined'] = [
            _dump_headerinfo_undefined(item) for item in header.undefined
        ]
    with contextlib.suppress(KeyError):
        raw['title'] = _dump_headerinfo_headertitle(header.title)

    return raw


def _load_header(raw):
    if not raw:
        return None
    begin = raw['begin']
    end = raw['end']
    page = _load_pageinformation(raw['page'])

    undefined = None
    with contextlib.suppress(KeyError):
        undefined = [
            _load_headerinfo_undefined(item) for item in raw['undefined']
        ]

    title = None
    with contextlib.suppress(KeyError):
        title = _load_headerinfo_headertitle(raw['title'])

    result = iamraw.FixedHeaderInformation(
        begin=begin,
        end=end,
        page=page,
    )
    if undefined:
        result.undefined = undefined
    if title:
        result.title = title
    return result


def _dump_pageinformation(pageinfo):
    if not pageinfo:
        return None
    raw = {
        'value': pageinfo.value,
        'raw': pageinfo.raw,
    }
    return raw


def _load_pageinformation(raw):
    if not raw:
        return None
    result = iamraw.PageInformation(
        value=raw['value'],
        raw=raw['raw'],
    )
    return result


def _dump_headerinfo_undefined(item):
    if item is None:
        return None
    raw = {
        'text': item.text,
    }
    return raw


def _load_headerinfo_undefined(item):
    if item is None:
        return None
    return iamraw.RawText(text=item['text'])


def _dump_headerinfo_headertitle(item):
    if item is None:
        return None
    raw = {
        'title': item.title,
        'raw': item.raw,
    }
    return raw


def _load_headerinfo_headertitle(item):
    if item is None:
        return None
    result = iamraw.HeaderTitle(
        title=item['title'],
        raw=item['raw'],
    )
    return result
