# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2022-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================
"""Index
=====

Example
-------

    Symbols
        95 per cent syndrome, 76, 77
    A
        Abstract, 117, 130
        Academic career, 138
        Academic documents, 52

>>> INDEX = DocumentIndex()
>>> INDEX.add('A', 'Academic career', 138, raw='Academic career, 138')
>>> for key, value in INDEX:
...     print(key, value)
A [DocumentIndexElement(Academic career 138 raw="Academic career, 138")]
"""

import dataclasses

import utila


@dataclasses.dataclass
class DocumentIndexElement:
    title: str = None
    page: int = None
    raw: str = None
    pdfpage: int = None

    def __repr__(self) -> str:
        return f'DocumentIndexElement({self.title} {self.page} raw="{self.raw}")'


class DocumentIndex:

    def __init__(self):
        self.data = {}

    def add(
        self,
        cat: str,
        title: str,
        page=None,
        raw: str = None,
        pdfpage: int = None,
    ):
        item = DocumentIndexElement(
            title=title,
            page=page,
            raw=raw,
            pdfpage=pdfpage,
        )
        try:
            self.data[cat].append(item)
        except KeyError:
            self.data[cat] = [item]

    def __iter__(self):
        for key, value in self.data.items():
            yield key, value

    def __len__(self):
        return sum(len(item) for item in self.data.values())

    def __repr__(self) -> str:
        result = ['DocumentIndex:']
        for key, value in self:
            result.append(f'{key}:')
            for item in value:
                result.append(item.raw)
        raw = utila.NEWLINE.join(result)
        return raw

    def __eq__(self, value):
        return str(self) == str(value)

    def __hash__(self):
        return hash(str(self))
