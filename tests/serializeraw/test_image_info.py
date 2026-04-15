# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import power
import pytest
import utilo
import utilotest

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


@utilotest.requires(power.BACHELOR037_PDF)
def test_images_load():
    source = power.link(power.BACHELOR037_PDF)
    imagepath = iamraw.path.images(source)
    loaded = serializeraw.load_image_infos_frompath(imagepath)
    loaded = utilo.flatten_content(loaded)
    assert len(loaded) == 2
