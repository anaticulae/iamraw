# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import re

import utila
import yaml

import iamraw


def dump_docref(references: iamraw.DocRefs) -> str:
    result = []
    for reference in references:
        marked = utila.from_tuple(utila.flatten(reference.marked))
        raw = f'{reference.page} {reference.sentence} {marked}'
        result.append(raw)
    dumped = yaml.safe_dump(result)
    return dumped


PATTERN = re.compile(r'\d+[ ]\d+')


def load_docref(content: str, pages: tuple = None) -> iamraw.DocRefs:
    loaded = utila.yaml_load(content)
    result = []
    for raw in loaded:
        page, sentence, marked = raw.split(maxsplit=2)
        page, sentence = int(page), int(sentence)
        marked = [
            utila.parse_tuple(item, length=2, typ=int)
            for item in PATTERN.findall(marked)
        ]
        result.append(
            iamraw.DocRef(
                page=page,
                sentence=sentence,
                marked=marked,
            ))
    # remove non selected pages
    result = [
        item for item in result if not utila.should_skip(item.page, pages)
    ]
    return result
