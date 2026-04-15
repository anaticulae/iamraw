# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

# import genex.example
import power
import pytest
import resinf

import iamraw
from tests.fixtures.textnavigator import navigator  # pylint:disable=W0611
from tests.serializeraw.examples.sections import restructured_sections_manual  # pylint:disable=W0611
from tests.serializeraw.fixtures import boxdata_from_pdf  # pylint:disable=W0611
from tests.serializeraw.fixtures import docu027_fontstore  # pylint:disable=W0611

pytest_plugins = ['pytester', 'xdist']  # pylint: disable=invalid-name

PACKAGE = 'iamraw'
resinf.setup(iamraw.ROOT)  # TODO: REMOVE LATER?
# power.setup(iamraw.ROOT)

RESOURCES = [
    # power.DOCU027_PDF,
    # power.DOCU007_PDF,
    # (power.MASTER072_PDF, '0:10'),
    # (power.BACHELOR111_PDF, '0:5'),
    # (power.BACHELOR037_PDF, '0:5'),
]

power.BACHELOR037_PDF = "abc/bachelor/bachelor037.pdf"
power.BACHELOR111_PDF = "abc/bachelor/bachelor111.pdf"
power.DOCU027_PDF = "abc/docu/docu027.pdf"

power.MASTER072_PDF = "abc/master/master072.pdf"


@pytest.mark.usefixtures('session')
def pytest_sessionstart():
    # power.run()
    pass


def extract(resources):
    # genex.example.extract(
    #     files=resources,
    #     footnote=True,
    #     groupme='--border --hefopa',
    #     headnote=True,
    #     pagenumber=True,
    #     reftable='--toc',
    #     worker=len(RESOURCES),
    # )
    pass
