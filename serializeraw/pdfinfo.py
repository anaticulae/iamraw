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
import re

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
    if loaded == {}:
        return iamraw.InvalidPDF
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


def date_str(date: iamraw.PDFDate) -> str:
    sign = '+' if date.utc_hour >= 0 else '-'
    result = (f'D:{date.year:04d}{date.month:02d}{date.day:02d}'
              f'{date.hour:02d}{date.minute:02d}{date.second:02d}'
              f'{sign}{date.utc_hour:02d}\'{date.utc_minute:02d}')
    return result


PATTERN = (r'D:(?P<year>\d{4})(?P<month>\d{2})(?P<day>\d{2})'
           r'(?P<hour>\d{2})(?P<minute>\d{2})(?P<second>\d{2})(?P<sign>[+-])'
           r'(?P<utc_hour>\d{2})\'(?P<utc_minute>\d{2})')


def date_fromstr(item: str) -> iamraw.PDFDate:
    """Parse ASN.1 date pattern.

    >>> date_fromstr("D:20160419072554+02'00")
    PDFDate(year=2016, month=4, day=19, hour=7, minute=25, second=54, utc_hour=2, utc_minute=0)
    """
    matched = re.match(PATTERN, item)
    if not matched:
        return None
    values = [
        'day', 'hour', 'minute', 'month', 'second', 'year', 'utc_hour',
        'utc_minute'
    ]
    data = {key: int(matched[key]) for key in values}
    result = iamraw.PDFDate(**data)
    if matched['sign'] == '-':
        result.hour = result * -1
    return result
