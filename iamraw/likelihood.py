# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import collections
import dataclasses
import typing

PageContentLikelihood = collections.namedtuple('PageLikelihood', 'page content')
PageContentLikelihoods = typing.List[PageContentLikelihood]


@dataclasses.dataclass
class Likelihood:
    value: str = None
    name: str = ''
