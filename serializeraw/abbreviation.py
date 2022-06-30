# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import contextlib

import utila

import iamraw


def dump_abbreviation(item) -> dict:
    """\
    >>> dump_abbreviation(iamraw.Abbreviation(position=iamraw.AbbreviationPosition(page=20)))
    {'short': None, 'position': '20 None None'}
    """
    assert isinstance(item, iamraw.Abbreviation), type(item)
    position = item.position
    raw = {
        'short': item.short,
    }
    if item.description:
        raw['description'] = item.description
    if position:
        raw['position'] = f'{position.page} {position.sentence} {position.word}'
    return raw


def load_abbreviation(raw: dict) -> iamraw.Abbreviation:
    """\
    >>> load_abbreviation({'short' : 'ABC', 'position' : '10 5 0',\
    'description' : 'alpha beta gum'}) # doctest: +NORMALIZE_WHITESPACE
    Abbreviation(short='ABC', description='alpha beta gum',
    position=AbbreviationPosition(page=10, sentence=5, word=0))

    >>> load_abbreviation({'short': None, 'position': '20 None None'})
    Abbreviation(short=None, description=None, position=AbbreviationPosition(page=20, sentence=None, word=None))
    """
    assert isinstance(raw, dict), type(raw)
    result = iamraw.Abbreviation(short=raw['short'])
    with contextlib.suppress(KeyError):
        result.description = raw['description']
    with contextlib.suppress(KeyError):
        page, sentence, word = utila.parse_tuple(
            raw['position'],
            length=3,
            typ=int,
            none=True,
        )
        result.position = iamraw.AbbreviationPosition(
            page=page,
            sentence=sentence,
            word=word,
        )
    return result


def dump_abbreviation_table(result: iamraw.abbreviation.AbbreviationResult) -> str: # yapf:disable
    assert isinstance(result, iamraw.AbbreviationResult), type(result)
    raw = [dump_abbreviation(item) for item in result]
    dumped = utila.yaml_dump(raw)
    return dumped


def load_abbreviation_table(content: str) -> iamraw.AbbreviationResult:
    loaded = utila.yaml_load(
        content,
        fname=(
            'reftable__abbrev_abbrev',
            'groupme__abbreviation_abbreviation',
        ),
        safe=False,
    )
    result = iamraw.AbbreviationResult()
    for item in loaded:
        loaded = load_abbreviation(item)
        result.append(loaded)
    return result


def dump_text_abbreviations(items) -> str:
    result = []
    for page in items:
        content = []
        for item in page.content:
            raw = dump_abbreviation(item)
            content.append(raw)
        if not content:
            continue
        result.append({'page': page.page, 'content': content})
    dumped = utila.yaml_dump(result)
    return dumped


def load_text_abbreviations(
    content: str,
    pages: tuple = None,
) -> iamraw.ExtractedTextAbbreviations:
    loaded = utila.yaml_load(
        content,
        safe=False,
    )
    result = []
    for page in loaded:
        pagenumber = int(page['page'])
        if utila.should_skip(pagenumber, pages):
            continue
        current = [load_abbreviation(item) for item in page['content']]
        result.append(
            iamraw.ExtractedTextAbbreviation(
                page=pagenumber,
                content=current,
            ))
    return result
