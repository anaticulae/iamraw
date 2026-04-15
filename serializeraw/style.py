# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import dataclasses

import utilo

import iamraw


def load_doctextstyle(content: str) -> iamraw.DocTextStyle:
    loaded = utilo.yaml_load(
        content,
        fname='doctextstyle__textstyle',
    )
    result = iamraw.DocTextStyle(**loaded)
    return result


def dump_doctextstyle(style: iamraw.DocTextStyle) -> str:
    assert isinstance(style, iamraw.DocTextStyle)
    raw = dataclasses.asdict(style)
    dumped = utilo.yaml_dump(raw)
    return dumped
