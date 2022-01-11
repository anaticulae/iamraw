# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utila
import yaml

import iamraw
import serializeraw


def dump_wspaces(pages) -> str:

    def dumper(items: list) -> str:
        raw = [utila.from_tuple(item) for item in items]
        return raw

    dumped = serializeraw.dump_pagecontent(pages, pagedumper=dumper)
    return dumped


def load_wspaces(content: str, pages: tuple = None) -> iamraw.PageContents:

    def loader(items: list) -> iamraw.PageContents:
        loaded = [utila.parse_tuple(item) for item in items]
        return loaded

    loaded = serializeraw.load_pagecontent(
        content=content,
        pages=pages,
        pageloader=loader,
        fname='spacestation__wspace_wspace',
    )
    return loaded


def dump_wwords(pages) -> str:

    def dumper(words: list) -> str:
        result = []
        for word in words:
            word = [rawchar(char) for char in word]
            result.append(word)
        return result

    dumped = serializeraw.dump_pagecontent(pages, pagedumper=dumper)
    return dumped


def load_wwords(content: str, pages: tuple = None) -> iamraw.PageContents:

    def loader(pages: list) -> iamraw.PageContents:
        loaded = [[fromraw(char) for char in word] for word in pages]
        return loaded

    loaded = serializeraw.load_pagecontent(
        content=content,
        pages=pages,
        pageloader=loader,
        fname='spacestation__wspace_words',
    )
    return loaded


def rawchar(item) -> str:
    # ensure to have single char, treat ligature as single char
    text = item._text[0]  # pylint:disable=W0212
    char = ord(text)
    raw = f'{char}|{utila.from_tuple(item.bbox)}|{item.fontsize}|{item.fontname}'
    return raw


def fromraw(item: str) -> tuple:
    text, bounding, fontsize, fontname = item.split('|')
    text = chr(int(text))
    bounding = utila.parse_tuple(bounding)
    fontsize = float(fontsize)
    result = (text, bounding, fontsize, fontname)
    return result


def dump_document_chardist(item: iamraw.DocumentCharDist) -> str:
    raw = vars(item)
    dumped = yaml.dump(raw)
    return dumped


def load_document_chardist(path: str) -> iamraw.DocumentCharDist:
    loaded = utila.yaml_load(
        path,
        fname='spacestation__chardist_chardist',
        safe=True,
    )
    result = iamraw.DocumentCharDist(**loaded)
    return result


def dump_document_worddist(item: iamraw.DocumentWordDist) -> str:
    raw = vars(item)
    dumped = yaml.dump(raw)
    return dumped


def load_document_worddist(path: str) -> iamraw.DocumentWordDist:
    loaded = utila.yaml_load(
        path,
        fname='spacestation__worddist_worddist',
        safe=True,
    )
    result = iamraw.DocumentWordDist(**loaded)
    return result
