# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import genex.example
import power
import pytest

import iamraw
from tests.fixtures.textnavigator import navigator  # pylint:disable=W0611
from tests.serializeraw.examples.sections import restructured_sections_manual  # pylint:disable=W0611
from tests.serializeraw.fixtures import boxdata_from_pdf  # pylint:disable=W0611

pytest_plugins = ['pytester', 'xdist']  # pylint: disable=invalid-name

PACKAGE = 'iamraw'
power.setup(iamraw.ROOT)

RESOURCES = [
    power.DOCU027_PDF,
    power.DOCU007_PDF,
]


@pytest.mark.usefixtures('session')
def pytest_sessionstart():
    power.run()


def extract(resources):
    genex.example.extract(
        files=resources,
        destination=power.generated(),
        groupme=True,
        formulero=False,
        tablero=False,
        rawmaker_cleanup=False,
        pages=':',
    )
