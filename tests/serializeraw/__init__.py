# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================
from os.path import exists
from os.path import join

from iamraw import ROOT

TEST = join(ROOT, 'tests/serializeraw')
assert exists(TEST), TEST

DATA = join(TEST, 'data')

TEXT_YAML = join(DATA, 'text.yaml')
assert exists(TEXT_YAML), TEXT_YAML

TOC_YAML = join(DATA, 'toc.yaml')
assert exists(TOC_YAML), TOC_YAML

HITS_YAML = join(DATA, 'decider_border_hitthebox__hits.yaml')
assert exists(HITS_YAML), HITS_YAML
