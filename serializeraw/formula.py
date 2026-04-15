# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utilo

import iamraw


def dump_formulas(pages: iamraw.PageContentFormula) -> str:
    # remove empty pages
    result = [item for item in pages if item.content]
    # convert
    dumped = utilo.yaml_dump(result, safe=False)
    return dumped


def load_formulas(
    content: str,
    pages: tuple = None,
) -> iamraw.PageContentFormula:
    loaded = utilo.yaml_load(
        content,
        fname='detector__formula_detected',
        safe=False,
    )

    result = [
        item for item in loaded if not utilo.should_skip(item.page, pages)
    ]
    return result
