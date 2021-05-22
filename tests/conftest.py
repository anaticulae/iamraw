# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import power
import pytest
import utila

import iamraw
from tests.fixtures.textnavigator import navigator  # pylint:disable=W0611
from tests.serializeraw.fixtures import boxdata_from_pdf  # pylint:disable=W0611

pytest_plugins = ['pytester', 'xdist']  # pylint: disable=invalid-name

PACKAGE = 'iamraw'
power.setup(iamraw.ROOT)

WORKER = 2
RESOURCES = [
    (power.DOCU27_PDF, None),
    (power.DOCU07_PDF, None),
]


@pytest.mark.usefixtures('session')
def pytest_sessionstart():
    power.run()


def extract(resources):
    todo = "--border --text --fonts --horizontals --toc --line -j4"
    layout = "--char_margin 5.0 --boxes_flow 1.0 --line_margin 0.3"
    todo = [(f'rawmaker -i {source} -o {power.link(source)} '
             f'--pages={utila.simplify_pages(pages)} {todo} {layout} && '
             f'groupme -i {power.link(source)} -o {power.link(source)} '
             '--footer --pagenumbers') for source, pages in resources]
    completed = utila.run_parallel(todo, worker=WORKER)
    assert completed == utila.SUCCESS
