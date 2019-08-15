# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

from collections import namedtuple
from functools import lru_cache
from typing import List

from configo import CACHE_SMALL
from utila import from_raw_or_path
from yaml import FullLoader
from yaml import dump
from yaml import load


def dump_likelihood(likelihoods: List[float]) -> str:
    """Write list of likelihoods into a single str"""
    result = ['%.2f' % item for item in likelihoods]
    dumped = dump(result)
    return dumped


@lru_cache(CACHE_SMALL)
def load_likelihood(content: str) -> List[float]:
    """Load list of likelihoods from single `content`"""
    content = from_raw_or_path(content, ftype='yaml')
    loaded = load(content, Loader=FullLoader)
    result = [float(item) for item in loaded]
    return result
