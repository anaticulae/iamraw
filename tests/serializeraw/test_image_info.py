# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import pytest

import iamraw
import serializeraw


def test_dump_and_load_image_info():
    info = iamraw.ImageInformation()
    dumped = serializeraw.dump_image_info(info)
    loaded = serializeraw.load_image_info(dumped)
    assert loaded == info


@pytest.mark.parametrize('hidden', (True, False))
def test_dump_and_load_image_hidden(hidden):
    info = iamraw.ImageInformation(hidden=hidden)
    dumped = serializeraw.dump_image_info(info)
    loaded = serializeraw.load_image_info(dumped)
    assert loaded == info
