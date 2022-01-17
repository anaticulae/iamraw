# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================
r"""\
YAML PAGES
==========

Aims to speed up partial loading of special pages instead of parsing the
whole yaml document.

Header:

```
# YAMLPAGES:HEADERSIZE:FIXEDCONTENT
# 0/0/100 1/101/200 3/201/400
```

Content:

Content is not changed.

Example:

>>> yamlpages = YAMLPages()
>>> for page in range(10):
...     yamlpages.addpage(page, page*100+(1 if page else 0), (page+1)*100)
>>> yamlpages.header(width=80)
'# 0/0/100 1/101/200 2/201/300 3/301/400 4/401/500 5/501/600 6/601/700 7/701/800\n# 8/801/900 9/901/1000'
"""

import dataclasses
import re
import textwrap

import utila

import serializeraw.__patch__

YAML_WIDTH = serializeraw.__patch__.YAML_WIDTH

HEADER = '# YAMLPAGES:'


@dataclasses.dataclass
class YAMLPages:
    content: dict = dataclasses.field(default_factory=dict)

    def addpage(self, page, start, end):
        self.content[page] = (start, end)

    @property
    def pages(self):
        return list(self.content.keys())

    def header(self, width: int = YAML_WIDTH) -> str:
        raw = [
            f'{page}/{item[0]}/{item[1]}'
            for page, item in self.content.items()
        ]
        joined = ' '.join(raw)
        wrapped = textwrap.wrap(joined, width=width)
        result = '# ' + '\n# '.join(wrapped)
        return result


def isyamlpage(path: str) -> bool:
    # TODO: USE ONLY LIMTED BITS AFTER UPGRADING UTILA
    header = utila.file_read(path)
    return header.startswith(HEADER)


def load_yamlpages(content: str, pages: tuple = None, fname=None) -> str:
    content = utila.from_raw_or_path(content, fname=fname)
    isyamlpages = content.startswith(HEADER)
    if not isyamlpages:
        return content
    fileinfo, content = content.split(utila.NEWLINE, maxsplit=1)
    fileinfo = fileinfo.replace(HEADER, '')
    headerlength, fixed = utila.parse_numbers(fileinfo.replace(':', ' '))
    if pages is None:
        content = content[headerlength:]
        return content
    header = parse_header(content[0:headerlength], pages=pages)
    content = content[headerlength:].strip()
    raw = []
    if fixed:
        raw.append(content[0:fixed])
    content = content[fixed:].strip()
    for _, (start, end) in header.content.items():
        raw.append(content[start:end])
    result = utila.NEWLINE.join(raw)
    return result


def write_yamlpages(path: str):
    utila.exists_assert(path)
    content = utila.file_read(path)
    result = dump_yamlpages(content)
    utila.file_replace(path, result)


def dump_yamlpages(content: str) -> str:
    isyamlpages = content.startswith(HEADER)
    assert not isyamlpages
    header, static, dynamic = split_content(content)
    header: str = header.header()
    bottom = f'{static}\n{dynamic}'
    top = f'{HEADER}{len(header)}:{len(static)}\n{header}\n'
    result = f'{top}{bottom}'
    return result


def split_content(content: str) -> tuple:
    loaded = utila.yaml_load(content)
    static = {}
    dynamic = {}
    islist = isinstance(loaded, list)
    if islist:
        dynamic = loaded
    else:
        for key, value in loaded.items():
            if isinstance(value, list):
                dynamic[key] = value
            else:
                static[key] = value
        static: str = utila.yaml_dump(static) if static else ''
        assert len(dynamic) <= 1, 'could not write more than one dynamic'
    dynamic: str = utila.yaml_dump(dynamic) if dynamic else ''
    if islist:
        head, tail = '', dynamic
    else:
        head, tail = dynamic.split('\n', maxsplit=1)
    header = create_header(tail)
    if static:
        static = f'{static.strip()}\n{head}'.strip()
    else:
        static = f'{head}'
    dynamic = [tail[start:end] for page, (start, end) in header.content.items()]
    dynamic: str = utila.NEWLINE.join(dynamic)
    return header, static, dynamic


SEPARATOR = r'^-[ ]\w+\:'


def create_header(tail: str) -> YAMLPages:
    collected = []
    current = 0
    for matched in list(re.finditer(SEPARATOR, tail, re.MULTILINE))[1:]:
        start, _ = matched.span()
        collected.append((current, start - 1))
        current = start
    collected.append((current, len(tail)))
    header = YAMLPages()
    for start, end in collected:
        # TODO: STRIP CONTENT HERE AFTER CLARIFING TODO BELOW
        content = tail[start:end]
        if not content.strip():
            # TODO: WHY CAN THIS HAPPEN? NO DYNAMIC CONTENT?
            continue
        page = getpage(content)
        header.addpage(page, start, end)
    return header


def parse_header(content: str, pages: tuple = None) -> YAMLPages:
    content = content.replace('# ', '')
    result = YAMLPages()
    for item in content.split():
        page, start, end = utila.parse_tuple(
            item,
            length=3,
            typ=int,
            separator='/',
        )
        if utila.should_skip(page, pages):
            continue
        result.addpage(page, start, end)
    return result


def getpage(content: str) -> int:
    loaded = utila.yaml_load(content)
    if isinstance(loaded, list):
        loaded = loaded[0]
    return loaded['page']
