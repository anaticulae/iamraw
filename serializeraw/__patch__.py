# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import functools

import yaml

YAML_WIDTH = 256

# pylint:disable=C0103
dump = functools.partial(yaml.dump, width=YAML_WIDTH)
safe_dump = functools.partial(yaml.safe_dump, width=YAML_WIDTH)

yaml.dump = dump
yaml.safe_dump = safe_dump
