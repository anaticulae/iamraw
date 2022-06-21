# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================
r"""\
>>> import iamraw
>>> advices = [iamraw.TextAdvice(), iamraw.TextAdviceDelete(), iamraw.TextAdviceReplacement()]
>>> assert load_textadvices(dump_textadvices(advices)) == advices

>>> REFERENCES = [iamraw.DocRef(page=5, sentence=1, marked=((5, 23),), raw=('siehe Abbildung 13',))]
>>> dump_docref(REFERENCES)
"- '5 1 5 23 raw: siehe Abbildung 13'\n"
>>> assert load_docref(dump_docref(REFERENCES)) == REFERENCES, 'verify dumper/loader'
"""

import re

import utila

import iamraw


def dump_docref(references: iamraw.DocRefs) -> str:
    result = []
    for reference in references:
        marked = utila.from_tuple(utila.flatten(reference.marked))
        line = f'{reference.page} {reference.sentence} {marked}'
        if reference.raw:
            reference_raw = utila.from_tuple(reference.raw, separator='@@@@')
            line += SEPARATOR_RAW + reference_raw
        result.append(line)
    dumped = utila.yaml_dump(result)
    return dumped


PATTERN = re.compile(r'\d+[ ]\d+')

SEPARATOR_RAW = ' raw: '


def load_docref(content: str, pages: tuple = None) -> iamraw.DocRefs:
    loaded = utila.yaml_load(content)
    result = []
    for raw in loaded:
        page, sentence, marked = raw.split(maxsplit=2)
        page, sentence = int(page), int(sentence)
        if utila.should_skip(page, pages):
            # remove non selected pages
            continue
        try:
            marked, raw, = marked.split(SEPARATOR_RAW, maxsplit=1)
            raw = utila.parse_tuple(
                raw,
                length=None,
                typ=str,
                separator='@@@@',
            )
        except ValueError:
            raw = None
        marked = tuple((utila.parse_tuple(item, length=2, typ=int)
                        for item in PATTERN.findall(marked)))
        docref = iamraw.DocRef(
            page=page,
            sentence=sentence,
            marked=marked,
            raw=raw,
        )
        result.append(docref)
    return result


def dump_textadvices(advices: iamraw.TextAdvices) -> str:
    dumped = utila.yaml_dump(advices, safe=False)
    return dumped


def load_textadvices(raw: str, pages: tuple = None) -> str:
    loaded = utila.yaml_load(raw, safe=False)
    result = [
        item for item in loaded if not utila.should_skip(item.page, pages=pages)
    ]
    return result
