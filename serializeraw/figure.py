# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import itertools
import os
import re

import utila

import iamraw
import serializeraw.images

EXT = 'png'


def dump_figures(figures: iamraw.Figures, path: str):
    """Group list of figures by page number and write `raw figure` and
    `figure information` to `path`."""
    assert os.path.exists(path), str(path)

    for page, values in itertools.groupby(
            figures,
            key=lambda item: serializeraw.images.load_image_info(item[0]).page,
    ):
        for index, (info, raw) in enumerate(values):
            write_image_info(info, path, page, index)
            write_image_raw(raw, path, page, index)


def load_figures(path: str, skip_raw: bool = True, pages: tuple = None):
    assert os.path.exists(path)
    files = utila.file_list(
        path,
        include='yaml',
        absolute=True,
    )
    files = utila.files_sort(files)  # pylint:disable=R0204
    result = []
    for item in files:
        figure = _load_figure(item)
        if utila.should_skip(figure.page, pages=pages):
            continue
        name = filename(figure.page, figure.index, EXT)
        if not skip_raw:
            raw_path = os.path.join(path, name)
            raw = _load_image_raw(raw_path)
            figure.data = raw
        result.append(figure)
    return result


def write_image_raw(data: bytes, path: str, page: int, index: int):
    name = filename(page, index, ext=EXT)
    outpath = os.path.join(path, name)
    with open(outpath, mode='wb') as output:
        output.write(data)


def write_image_info(dumped: str, path: str, page: int, index: int):
    assert isinstance(dumped, str), type(dumped)
    name = filename(page, index, ext='yaml')
    outpath = os.path.join(path, name)
    utila.file_create(outpath, dumped)


def _load_figure(path: str) -> iamraw.Figure:
    info = serializeraw.load_image_info(path)
    index = parse_index(path)
    result = iamraw.Figure(
        page=info.page,
        index=index,
        bounding=info.bounding,
    )
    return result


def _load_image_raw(path: str) -> 'PIL.Image.Image':
    import PIL.Image  # pylint:disable=import-outside-toplevel
    try:
        image = PIL.Image.open(path)
        image.load()
        return image
    except OSError as err:
        utila.error(err)
        return None


def filename(page, index, ext):
    page = f'{page}'.zfill(3)
    index = f'{index}'.zfill(2)
    return f'{page}_{index}.{ext}'


def parse_index(item: str) -> int:
    """\
    >>> parse_index('005_43.yaml')
    43
    """
    pattern = r'\d{3}\_(?P<index>\d{2})\.yaml'
    matched = re.search(pattern, item)
    if not matched:
        return None
    matched = int(matched['index'])
    return matched
