# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import collections
import functools
import os

import utila

import iamraw


def dump_image_info(info: iamraw.ImageInformation) -> str:
    assert isinstance(info, iamraw.ImageInformation), type(info)
    result = {}
    if info.height is not None:
        result['height'] = info.height
    if info.width is not None:
        result['width'] = info.width
    if info.page is not None:
        result['page'] = info.page
    if info.hidden:
        result['hidden'] = info.hidden
    if info.figure:
        result['figure'] = info.figure
    if info.bounding:
        result['bounding'] = utila.from_tuple(info.bounding)
    if info.dpi:
        result['dpi'] = utila.from_tuple(info.dpi)
    dumped = utila.yaml_dump(result)
    return dumped


def load_image_info(content: str) -> iamraw.ImageInformation:
    loaded = utila.yaml_load(content)
    parsed = iamraw.ImageInformation()
    loader = [
        ('page', int),
        ('width', float),
        ('height', float),
        ('hidden', utila.str2bool),
        ('figure', utila.str2bool),
        ('dpi', functools.partial(utila.parse_tuple, length=2)),
        ('bounding', functools.partial(utila.parse_tuple, length=4)),
    ]
    for key, typ in loader:
        try:
            value = typ(loaded[key])
        except KeyError:
            continue
        except TypeError:
            utila.error(f'invalid load_image_info: {loaded}')
            return None
        setattr(parsed, key, value)
    return parsed


def load_image_infos_frompath(
    path: str,
    pages: tuple = None,
    skip_hidden: bool = False,
    path_append: bool = False,
) -> iamraw.PageContentImageInfos:
    if not os.path.exists(path):
        return []
    files = [
        os.path.join(path, item)
        for item in utila.file_list(path, include='yaml')
    ]
    result = load_image_infos_fromfiles(
        files=files,
        pages=pages,
        skip_hidden=skip_hidden,
        path_append=path_append,
    )
    return result


load_image_informations_frompath = load_image_infos_frompath  # pylint:disable=C0103


def load_image_infos_fromfiles(
    files: str,
    pages: tuple = None,
    skip_hidden: bool = False,
    path_append: bool = False,
) -> iamraw.PageContentImageInfos:
    collected = collections.defaultdict(list)
    for source in files:
        loaded = load_image_info(source)
        if not loaded:
            continue
        if utila.should_skip(loaded.page, pages):
            continue
        if skip_hidden and loaded.hidden:
            continue
        # add image content hash
        hashedimage = utila.file_name(source)
        loaded.hashedimage = hashedimage
        if path_append:
            collected[loaded.page].append((loaded, source))
        else:
            collected[loaded.page].append(loaded)
    result = [
        iamraw.PageContentImageInfo(page=key, content=content)
        for key, content in collected.items()
    ]
    result.sort(key=lambda x: x.page)
    return result
