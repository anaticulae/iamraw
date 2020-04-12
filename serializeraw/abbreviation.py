# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import contextlib

import utila
import yaml

import iamraw


def dump_abbreviation(item) -> dict:
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
    assert isinstance(raw, dict), type(raw)
    result = iamraw.Abbreviation(short=raw['short'])
    with contextlib.suppress(KeyError):
        result.description = raw['description']
    with contextlib.suppress(KeyError):
        page, sentence, word = utila.parse_tuple(raw['position'], typ=int)
        result.position = iamraw.AbbreviationPosition(
            page=page,
            sentence=sentence,
            word=word,
        )
    return result


def dump_abbreviation_table(result: iamraw.abbreviation.AbbreviationResult,
                           ) -> str:
    assert isinstance(result, iamraw.AbbreviationResult), type(result) # yapf:disable
    raw = [dump_abbreviation(item) for item in result]
    dumped = yaml.dump(raw)
    return dumped


def load_abbreviation_table(content: str,) -> iamraw.AbbreviationResult:
    content = utila.from_raw_or_path(content, ftype='yaml')
    loaded = yaml.load(content, Loader=yaml.FullLoader)

    result = iamraw.AbbreviationResult()
    for item in loaded:
        loaded = load_abbreviation(item)
        result.append(loaded)
    return result
