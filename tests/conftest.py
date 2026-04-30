# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

# import genex.example
import hoverpower
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
# hoverpower.setup(iamraw.ROOT)

RESOURCES = [
    hoverpower.DOCU027_PDF,
    hoverpower.DOCU007_PDF,
    (hoverpower.MASTER072_PDF, '0:10'),
    (hoverpower.BACHELOR111_PDF, '0:5'),
    (hoverpower.BACHELOR037_PDF, '0:5'),
]

hoverpower.BACHELOR037_PDF = "abc/bachelor/bachelor037.pdf"
hoverpower.BACHELOR111_PDF = "abc/bachelor/bachelor111.pdf"
hoverpower.DOCU027_PDF = "abc/docu/docu027.pdf"

hoverpower.MASTER072_PDF = "abc/master/master072.pdf"


@pytest.mark.usefixtures('session')
def pytest_sessionstart():
    # hoverpower.run()
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
