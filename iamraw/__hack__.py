# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================
"""Hack to fix bug after upgrading yaml. YAML is not able anymore to
serialize dataclasses correctly."""

import yaml

import iamraw


def register_class(item):
    try:
        name = f'tag:yaml.org,2002:python/object:{item.__module__}.{item.__name__}'
    except AttributeError:
        return

    def dataclass_constructor(loader, node):
        loaded = loader.construct_mapping(node)
        return item(**loaded)

    def dataclass_constructor_sequence(loader, node):
        loaded = loader.construct_sequence(node)[0]
        return list(item)[loaded - 1]

    yaml.add_constructor(name, dataclass_constructor)
    name = f'tag:yaml.org,2002:python/object/apply:{item.__module__}.{item.__name__}'
    yaml.add_constructor(name, dataclass_constructor_sequence)


[register_class(getattr(iamraw, name)) for name in dir(iamraw)]  # pylint:disable=expression-not-assigned
