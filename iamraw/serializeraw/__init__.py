#==============================================================================
# C O P Y R I G H T
#------------------------------------------------------------------------------
# Copyright (c) 2019 by Helmut Konrad Fahrendholz. All rights reserved.
# Tis file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
#==============================================================================
"""
Package to load and store raw objects as yaml files.
"""

import os

# document
from iamraw.serializeraw.text import dump_yaml as dump_document
from iamraw.serializeraw.text import load_yaml as load_document
# toc
from iamraw.serializeraw.toc import dump_yaml as dump_toc
from iamraw.serializeraw.toc import load_yaml as load_toc
