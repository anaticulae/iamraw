# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

# TODO: REPLACE THIS DRAFT LATER

import utila

import iamraw


def dump_index(titlepage: iamraw.DocumentIndex) -> str:
    dumped = utila.yaml_dump(titlepage, safe=False)
    return dumped


def load_index(content: str) -> iamraw.DocumentIndex:
    loaded = utila.yaml_load(
        content,
        fname='detector__index_detected',
        safe=False,
    )
    return loaded
