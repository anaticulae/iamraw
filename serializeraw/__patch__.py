# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================
"""Hack to fix bug after upgrading yaml. YAML is not able anymore to
serialize dataclasses correctly."""

import functools

import yaml
import yaml.constructor

yaml.constructor.FullConstructor.add_multi_constructor(
    'tag:yaml.org,2002:python/object:',
    yaml.constructor.FullConstructor.construct_python_object,
)
yaml.constructor.FullConstructor.add_multi_constructor(
    'tag:yaml.org,2002:python/object/apply:',
    yaml.constructor.FullConstructor.construct_python_object_apply,
)
yaml.constructor.FullConstructor.add_multi_constructor(
    'tag:yaml.org,2002:python/object/new:',
    yaml.constructor.FullConstructor.construct_python_object_new,
)

YAML_WIDTH = 256

# pylint:disable=C0103
dump = functools.partial(yaml.dump, width=YAML_WIDTH)
safe_dump = functools.partial(yaml.safe_dump, width=YAML_WIDTH)

yaml.dump = dump
yaml.safe_dump = safe_dump
