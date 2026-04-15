# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================
"""A simple test to getting started with yaml API and ensure a little bit of
upgrading external yaml package."""

import utilo


def test_dump_and_load():
    """Dump and load a simple example"""
    simple = {
        'name': 'Reis',
        'prename': 'Milch',
        'age': 42,
        'sex': 'm',
        'notes': [1, 2, 1, 3, 1, 1]
    }
    dumped = utilo.yaml_dump(simple)
    loaded = utilo.yaml_load(dumped)
    assert loaded == simple
