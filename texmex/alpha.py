# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================
"""Alpha
=====

This module provides methods to work with german languages constructs.
"""
import contextlib


def sort(*items):
    """Sort words included greek letter alphabetically.

    >>> sort('Alpha', 'α', 'Gamma', 'beta')
    ['α', 'Alpha', 'beta', 'Gamma']
    """
    return sorted(items, key=lambda x: replace(x).lower())


def replace(*items):
    """Convert to ascii.

    >>> replace('α', 'χ', '²', 'Abc')
    ['a', 'X', '2', 'Abc']
    >>> replace('Hαχ²')
    'HaX2'
    >>> replace('χ')
    'X'
    """
    # TODO: REPLACE WITH GOOD ONE
    table = {'α': 'a', 'χ': 'X', '²': '2'}
    result = []
    for item in items:
        replaced = []
        for char in item:
            with contextlib.suppress(KeyError):
                char = table[char]
            replaced.append(char)
        result.append(''.join(replaced))
    if len(result) == 1:
        return result[0]
    return result
