# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import dataclasses

import utila

import iamraw


def load_doctextstyle(content: str) -> iamraw.DocTextStyle:
    loaded = utila.yaml_load(content)
    result = iamraw.DocTextStyle(**loaded)
    return result


def dump_doctextstyle(style: iamraw.DocTextStyle) -> str:
    assert isinstance(style, iamraw.DocTextStyle)
    raw = dataclasses.asdict(style)
    dumped = utila.yaml_dump(raw)
    return dumped
