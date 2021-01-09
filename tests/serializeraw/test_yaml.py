# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================
"""A simple test to getting started with yaml API and ensure a little bit of
upgrading external yaml package."""

from yaml import safe_dump
from yaml import safe_load


def test_dump_and_load():
    """Dump and load a simple example"""
    simple = {
        'name': 'Reis',
        'prename': 'Milch',
        'age': 42,
        'sex': 'm',
        'notes': [1, 2, 1, 3, 1, 1]
    }

    dumped = safe_dump(simple)
    loaded = safe_load(dumped)

    assert loaded == simple
