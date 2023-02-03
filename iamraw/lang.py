# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import enum


class Language(enum.Enum):
    GERMAN = enum.auto()
    ENGLISH = enum.auto()
    FRENCH = enum.auto()
    UNKNOWN = enum.auto()

    @staticmethod
    def from_str(item: str) -> 'Language':
        """\
        >>> Language.from_str('GER')
        <Language.GERMAN:...>
        >>> Language.from_str('INVALID_LANG')
        Traceback (most recent call last):
        ...
        ValueError: not a lang: invalid_lang
        >>> Language.from_str('en')
        <Language.ENGLISH:...>
        """
        item = item.lower().strip()
        for value, key in LANGUAGE.items():
            if item in key:
                return value
        raise ValueError(f'not a lang: {item}')


LANGUAGE = {
    Language.GERMAN: 'ger german de'.split(),
    Language.ENGLISH: 'eng english en'.split(),
    Language.FRENCH: 'fre french'.split(),
    Language.UNKNOWN: 'none unknown'.split(),
}


def simplelang(lang: Language) -> str:
    """\
    >>> simplelang(Language.GERMAN)
    'ger'
    >>> simplelang('german')
    'ger'
    >>> simplelang('port')
    Traceback (most recent call last):
    ...
    ValueError: invalid language: port
    """
    if isinstance(lang, str):
        lang = lang.lower()
        for value in LANGUAGE.values():
            if lang in value:
                return value[0]
        raise ValueError(f'invalid language: {lang}')
    return LANGUAGE[lang][0]
