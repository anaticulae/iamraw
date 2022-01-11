# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import enum


class Language(enum.Enum):
    GERMAN = enum.auto()
    ENGLISH = enum.auto()
    FRENCH = enum.auto()
    UNKNOWN = enum.auto()


LANGUAGE = {
    Language.GERMAN: 'ger german'.split(),
    Language.ENGLISH: 'eng english'.split(),
    Language.FRENCH: 'fre french'.split(),
    Language.UNKNOWN: 'none unknown'.split(),
}


def simplelang(lang: Language) -> str:
    if isinstance(lang, str):
        return lang
    return LANGUAGE[lang][0]
