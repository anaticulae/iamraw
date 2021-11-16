# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import dataclasses
import typing


@dataclasses.dataclass
class DocRef:
    page: int
    sentence: int
    marked: list = dataclasses.field(default=list)

    def __getitem__(self, index):
        return (self.page, self.sentence, self.marked)[index]


DocRefs = typing.List[DocRef]


@dataclasses.dataclass
class TextAdvice:
    raw: str = None
    typ: str = None
    docref: DocRef = None

    @property
    def page(self) -> int:
        return self.docref.page if self.docref else -1


TextAdvices = typing.List[TextAdvice]


@dataclasses.dataclass
class TextAdviceReplacement(TextAdvice):
    replacement: str = None
    hint: str = None


@dataclasses.dataclass
class TextAdviceDelete(TextAdvice):
    pass
