# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

# TODO: REPLACE THIS DRAFT LATER

import utila
import yaml

import iamraw


def dump_titlepage(titlepage: iamraw.TitlePage) -> str:
    # TODO: Improve with human readable format
    dumped = yaml.dump(titlepage)
    return dumped


def load_titlepage(content: str) -> iamraw.TitlePage:
    loaded = utila.yaml_from_raw_or_path(
        content,
        safe=False,
    )
    return loaded
