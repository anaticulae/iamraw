# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utila
import yaml

import iamraw


def dump_formulas(pages: iamraw.PageContentFormula) -> str:
    # remove empty pages
    result = [item for item in pages if item.content]
    # convert
    dumped = yaml.dump(result)
    return dumped


def load_formulas(
        content: str,
        pages: tuple = None,
) -> iamraw.PageContentFormula:
    content = utila.from_raw_or_path(
        content,
        ftype='yaml',
        fname='detector__formula_detected',
    )
    loaded = yaml.load(content, Loader=yaml.FullLoader)

    result = [
        item for item in loaded if not utila.should_skip(item.page, pages)
    ]
    return result
