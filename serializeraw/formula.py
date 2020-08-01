# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================
"""Extracted Raw Formulas
======================

>>> EXTRACTED = [iamraw.PageContentFormula(page=5, content=[iamraw.FormulaRaw(
...     page=5,
...     content=[
...         iamraw.MathChar(bounding=(491.2, 109.97, 495.18, 124.63), size=14.66, value='x'),
...         iamraw.MathChar(bounding=(495.18, 109.97, 501.15, 124.63), size=14.66, value='='),
...         iamraw.MathChar(bounding=(501.15, 109.97, 504.14, 124.63), size=14.66, value='y'),
...         iamraw.MathChar(bounding=(504.14, 109.97, 510.12, 124.63), size=14.66, value='+'),
...         iamraw.MathChar(bounding=(510.12, 109.97, 514.1, 124.63), size=14.66, value='3')
...     ]
... )])]

>>> dumped = dump_rawformulas(EXTRACTED)
>>> loaded = load_rawformulas(dumped)
>>> assert loaded == EXTRACTED

"""

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
    content = utila.from_raw_or_path(content, ftype='yaml')
    loaded = yaml.load(content, Loader=yaml.FullLoader)

    result = [
        item for item in loaded if not utila.should_skip(item.page, pages)
    ]
    return result


def dump_rawformulas(pages: iamraw.PageContentRawFormulas) -> str:
    # remove empty pages
    result = [item for item in pages if item.content]
    # convert
    dumped = yaml.dump(result)
    return dumped


def load_rawformulas(
        content: str,
        pages: tuple = None,
) -> iamraw.PageContentRawFormulas:
    content = utila.from_raw_or_path(content, ftype='yaml')
    loaded = yaml.load(content, Loader=yaml.FullLoader)

    result = [
        item for item in loaded if not utila.should_skip(item.page, pages)
    ]
    return result
