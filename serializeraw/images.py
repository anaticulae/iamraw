# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import collections
import functools
import os

import utila
import yaml

import iamraw


def dump_image_info(info: iamraw.ImageInformation) -> str:
    assert isinstance(info, iamraw.ImageInformation)
    result = {}
    if info.height is not None:
        result['height'] = info.height
    if info.width is not None:
        result['width'] = info.width
    if info.page is not None:
        result['page'] = info.page
    if info.bounding:
        result['bounding'] = utila.from_tuple(info.bounding)
    if info.dpi:
        result['dpi'] = utila.from_tuple(info.dpi)
    dumped = yaml.safe_dump(result)
    return dumped


def load_image_info(content: str) -> iamraw.ImageInformation:
    source = utila.from_raw_or_path(content, ftype='yaml')
    loaded = yaml.safe_load(source)
    parsed = iamraw.ImageInformation()
    loader = [
        ('page', int),
        ('width', float),
        ('height', float),
        ('dpi', functools.partial(utila.parse_tuple, length=2)),
        ('bounding', functools.partial(utila.parse_tuple, length=4)),
    ]
    for key, typ in loader:
        try:
            value = typ(loaded[key])
        except KeyError:
            continue
        setattr(parsed, key, value)
    return parsed


def load_image_informations_frompath(
        path: str,
        pages: tuple = None,
) -> iamraw.PageContentImageInfos:
    if not os.path.exists(path):
        return []

    files = utila.file_list(path, include='yaml')

    collected = collections.defaultdict(list)
    for item in files:
        source = os.path.join(path, item)
        loaded = load_image_info(source)
        if utila.should_skip(loaded.page, pages):
            continue
        collected[loaded.page].append(loaded)
    result = [
        iamraw.PageContentImageInfo(page=key, content=value)
        for key, value in collected.items()
    ]
    result.sort(key=lambda x: x.page)
    return result
