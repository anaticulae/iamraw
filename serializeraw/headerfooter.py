# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import contextlib

import configo
import utilo

import iamraw
import serializeraw
import texmex


def dump_headerfooter(pages: iamraw.PageContentFooterHeaders) -> str:
    serializeraw.validate(pages)
    content = []
    for page in pages:
        raw_header = _dump_header(page.header)
        raw_footer = _dump_footer(page.footer)
        content.append({
            'page': page.page,
            'header': raw_header,
            'footer': raw_footer,
        })
    result = dict(
        content=content,
        __strategy__=None,
    )
    with contextlib.suppress(AttributeError):
        result['__strategy__'] = pages.__strategy__
    return utilo.yaml_dump(result)


@configo.cache_small
def load_headerfooter(
    content: str,
    pages=None,
) -> iamraw.PageContentFooterHeaders:
    loaded = utilo.yaml_load(
        content,
        fname=(
            'groupme__hefopa_result',
            'footnote__result_result',
            'headnote__result_result',
            'groupme__footer_footerheader',
        ),
        safe=False,
    )
    content = []
    legacy = isinstance(loaded, list)
    data = loaded if legacy else loaded['content']
    for item in data:
        pagenumber = item['page']
        assert isinstance(pagenumber, int)
        if utilo.should_skip(pagenumber, pages):
            continue
        header = _load_header(item['header'])
        footer = _load_footer(item['footer'])
        footerheader = iamraw.PageContentFooterHeader(
            header=header,
            footer=footer,
            page=pagenumber,
        )
        content.append(footerheader)
    serializeraw.validate(content)
    result = iamraw.PageContentFooterHeaders(content=content)
    if not legacy:
        result.__strategy__ = loaded.get('__strategy__', None)
    return result


def dump_footnote(note: iamraw.FootNote):
    assert hasattr(note, 'number'), str(note)
    with contextlib.suppress(AttributeError):
        assert note.text, note
    raw = utilo.simplify(note)
    return raw


def load_footnote(raw: dict) -> iamraw.FootNote:
    with contextlib.suppress(TypeError):
        rawnote = iamraw.FootNoteRaw(**raw)
        # TODO: REMOVE WITH NEXT MAJOR
        if rawnote.style and len(rawnote.style) == 2:
            # style=(number.style, note.style),
            number = None
            if rawnote.style[0]:
                number = texmex.CharStyle(**rawnote.style[0])
            rawnote.style[1]['content'] = [
                texmex.CharStyle(**item) for item in rawnote.style[1]['content']
            ]
            note = texmex.TextStyle(**(rawnote.style[1]))
            rawnote.style = (number, note)
        # new approach
        if rawnote.style_number:
            rawnote.style_number = texmex.CharStyle(**rawnote.style_number)
        if rawnote.style_text:
            rawnote.style_text['content'] = [
                texmex.CharStyle(**item)
                for item in rawnote.style_text['content']
            ]
            rawnote.style_text = texmex.TextStyle(**rawnote.style_text)
        return rawnote
    with contextlib.suppress(TypeError):
        return iamraw.FootJudgedNote(**raw)
    with contextlib.suppress(TypeError):
        merged = iamraw.FootNoteMerged(**raw)
        merged.notes = [load_footnote(item) for item in merged.notes]
        return merged
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
    if isinstance(footer, iamraw.MovingFooterInfo):
        # dump footnotes
        notes = [dump_footnote(item) for item in footer.notes]
        raw['notes'] = notes
    if isinstance(footer, iamraw.PagesFooterInfo):
        if footer.page_location is not None:
            raw['page_location'] = str(footer.page_location)
        else:
            raw['page_location'] = None
    if isinstance(footer, iamraw.FixedFooterInfo):
        if dumped := _dump_header(footer):
            return dumped
    return raw


def _load_footer(raw) -> iamraw.FooterInfo:
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
    # try to export MovingFooterInfo
    with contextlib.suppress(KeyError):
        notes = raw['notes']
        notes = [load_footnote(item) for item in notes]
        result = iamraw.MovingFooterInfo(
            begin=begin,
            end=end,
            notes=notes,
        )
        return result
    # try to export PagesFooterInfo
    with contextlib.suppress(KeyError):
        page_location = raw['page_location']
        if page_location is not None:
            page_location = iamraw.BoundingBox.from_str(page_location)
        result = iamraw.PagesFooterInfo(  # pylint:disable=R0204
            begin=begin,
            end=end,
            page_location=page_location,
        )
        if page is not None:
            result.page = page
        return result
    if loaded := _load_footer_fixed(raw):
        return loaded
    # try to export FixedFooterInfo
    result = iamraw.FixedFooterInfo(
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
    with contextlib.suppress(KeyError):
        refs = _dump_refs(header.refs)
        if refs:
            raw['refs'] = refs
    return raw


def _load_header(raw):
    if not raw:
        return None
    begin = raw['begin']
    end = raw['end']
    page = _load_pageinformation(raw['page'])
    # undefined
    undef = None
    with contextlib.suppress(KeyError):
        undef = [_load_headerinfo_undefined(item) for item in raw['undefined']]
    # title
    title = None
    with contextlib.suppress(KeyError):
        title = _load_headerinfo_headertitle(raw['title'])
    refs = None
    with contextlib.suppress(KeyError):
        refs = _load_refs(raw['refs'])
    result = iamraw.FixedHeaderInfo(
        begin=begin,
        end=end,
        page=page,
    )
    if undef:
        result.undefined = undef
    if title:
        result.title = title
    if refs:
        result.refs = refs
    return result


def _load_footer_fixed(raw):
    if not raw:
        return None
    begin = raw['begin']
    end = raw['end']
    page = _load_pageinformation(raw.get('page'))
    undefined = None
    with contextlib.suppress(KeyError):
        undefined = [
            _load_headerinfo_undefined(item) for item in raw['undefined']
        ]
    title = None
    with contextlib.suppress(KeyError):
        title = _load_headerinfo_headertitle(raw['title'])
    refs = None
    with contextlib.suppress(KeyError):
        refs = _load_refs(raw['refs'])
    result = iamraw.FixedFooterInfo(
        begin=begin,
        end=end,
        page=page,
    )
    if undefined:
        result.undefined = undefined
    if title:
        result.title = title
    if refs:
        result.refs = refs
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


def _dump_refs(items):
    if not items:
        return []
    return [utilo.from_tuple(item) for item in items]


def _load_refs(items):
    if not items:
        return []
    return [utilo.parse_tuple(item) for item in items]
