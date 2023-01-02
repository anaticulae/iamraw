# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

# TODO: REPLACE THIS DRAFT LATER

import utila

import iamraw


def dump_titlepage(titlepage: iamraw.TitlePage) -> str:
    # TODO: Improve with human readable format
    dumped = utila.yaml_dump(titlepage, safe=False)
    return dumped


def load_titlepage(content: str) -> iamraw.TitlePage:
    loaded = utila.yaml_load(
        content,
        safe=False,
        fname='detector__titlepage_detected',
    )
    return loaded
