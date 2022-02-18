# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import enum
import re

import utila


class SentenceType(enum.Enum):
    """\
    >>> SentenceType.QUOT.name
    'QUOT'
    """
    # no special sentence
    NORMAL = enum.auto()
    # lists
    LIST_SEPA = enum.auto()
    LIST_ITEM = enum.auto()
    # formulas
    FORMULA = enum.auto()
    # TODO: ADD DIFFERENT FORMULAS
    # quotation
    QUOT = enum.auto()
    QUOT_START = enum.auto()
    QUOT_END = enum.auto()
    QUOT_QUOT = enum.auto()  # quotation inside quotation
    QUOT_QUOT_START = enum.auto()
    QUOT_QUOT_END = enum.auto()


DETECTOR = utila.compiles(r"""
    ^
    \#\$\@
    (
        %s
    )
    \@\$\#\:
    (
    .+
    )
    $
""" % '|'.join(re.escape(item.name) for item in SentenceType))


def sentence_type(sentence: str, verbose: bool = False) -> SentenceType:
    """\
    >>> sentence_type('#$@LIST_ITEM@$#:Content')
    <SentenceType.LIST_ITEM:...>
    >>> sentence_type('Just a simple sentence.')
    <SentenceType.NORMAL:...>
    >>> sentence_type('Just a simple sentence.', verbose=True)
    (<SentenceType.NORMAL:...>, 'Just a simple sentence.')
    """
    sentence = sentence.strip()
    matched = DETECTOR.match(sentence)
    if not matched:
        if verbose:
            return SentenceType.NORMAL, sentence
        return SentenceType.NORMAL
    typ = matched[1]
    if verbose:
        return SentenceType[typ], matched[2]
    return SentenceType[typ]


def special(item: str) -> str:
    return f'#$@{item}@$#:'


def is_listsepa(item: str) -> bool:
    """\
    >>> is_listsepa('#$@LIST_SEPA@$#:Hände waschen')
    True
    """
    return sentence_type(item) == SentenceType.LIST_SEPA


def is_listitem(item: str) -> bool:
    """\
    >>> is_listitem('#$@LIST_ITEM@$#:Content')
    True
    """
    return sentence_type(item) == SentenceType.LIST_ITEM


def is_formula(item: str) -> bool:
    """\
    >>> is_formula('#$@FORMULA@$#:5')
    True
    """
    return sentence_type(item) == SentenceType.FORMULA


def nosentence(text: str) -> bool:
    """\
    >>> nosentence('#$@FORMULA@$#:5')
    True
    """
    return sentence_type(text) != SentenceType.NORMAL


QUOT = special(SentenceType.QUOT.name)
LIST_SEPA = special(SentenceType.LIST_SEPA.name)
LIST_ITEM = special(SentenceType.LIST_ITEM.name)


def list_split(item: str):
    """\
    >>> list_split('#$@LIST_ITEM@$#:Content')
    ('Content', '#$@LIST_ITEM@$#:')
    """
    matched = sentence_type(item, verbose=True)
    if matched[0] == SentenceType.NORMAL:
        return matched[1]
    if matched[0] == SentenceType.LIST_SEPA:
        return matched[1], LIST_SEPA
    if matched[0] == SentenceType.LIST_ITEM:
        return matched[1], LIST_ITEM
    assert 0, f'should not match: {matched}'  # pragma: no cover
