# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================
"""\
>>> import iamraw, serializeraw
>>> info = iamraw.PDFInfo(pages=10,
...                       generator=iamraw.PDFGenerator.MSWORD,
...                       version=iamraw.PDFVersion(1,7))
>>> dumped = serializeraw.dump_pdfinfo(info, ext='yaml')
>>> loaded = serializeraw.load_pdfinfo(dumped)
>>> assert loaded == info
"""

import json

import utila
import yaml

import iamraw


def dump_pdfinfo(info: iamraw.PDFInfo, ext: str = 'json') -> str:
    assert ext in ('yaml', 'json'), ext
    simple = raw(info)
    if ext == 'yaml':
        return yaml.dump(simple)
    if ext == 'json':
        return json.dumps(simple)
    return None


def load_pdfinfo(path: str) -> iamraw.PDFInfo:
    loaded = utila.yaml_from_raw_or_path(
        path,
        fname='pdfinfo',
    )
    loaded['version'] = iamraw.PDFVersion(
        loaded['version']['major'],
        loaded['version']['minor'],
    )
    loaded['generator'] = iamraw.PDFGenerator[loaded['generator'].upper()]
    result = iamraw.PDFInfo(**loaded)
    return result


def raw(info: iamraw.PDFInfo) -> dict:
    result = {
        'pages': info.pages,
        'generator': str(info.generator),
        'version': {
            'major': info.version.major,
            'minor': info.version.minor,
        }
    }
    if info.meta:
        result['meta'] = info.meta
    return result
