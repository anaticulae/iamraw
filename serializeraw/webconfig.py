# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import dataclasses
import os

import utila

import iamraw


def load_webconfig(path: str) -> iamraw.WebConfig:
    assert os.path.exists(path), str(path)
    config = utila.yaml_load(path)
    assert utila.iterable(config['decider']), type(config['decider'])
    activex = config.get('active', set())
    # support for tuple with msgid and comment
    config['active'] = set(int(str(item).split()[0]) for item in activex)
    result = iamraw.WebConfig(**config)
    return result


def dump_webconfig(path: str, config: iamraw.WebConfig):
    raw = dataclasses.asdict(config)
    raw['active'] = list(raw['active'])
    raw['decider'] = list(raw['decider'])
    dumped = utila.yaml_dump(raw)
    utila.file_replace(path, dumped)
