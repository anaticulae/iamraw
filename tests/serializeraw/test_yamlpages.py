# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os

import hoverpower
import utilo
import utilotest

import serializeraw


@utilotest.requires(hoverpower.DOCU027_PDF)
def test_yamlpages_write(testdir):
    source = hoverpower.link(hoverpower.DOCU027_PDF)
    filename = 'rawmaker__text_text.yaml'
    utilo.copy_content(
        source,
        dst=testdir.tmpdir,
        pattern=filename,
        unlock=True,
    )
    dumped = serializeraw.dump_document(
        serializeraw.load_document(filename),
        fast=False,
    )
    utilo.file_replace(filename, dumped)
    serializeraw.write_yamlpages(filename)
    loaded = serializeraw.load_yamlpages(filename, pages=10)
    yaml = utilo.yaml_load(loaded)
    assert yaml['dimension']
    assert yaml['pages'][0]['page'] == 10
    # double page test
    loaded = serializeraw.load_yamlpages(filename, pages=(0, 11))
    yaml = utilo.yaml_load(loaded)
    assert yaml['pages'][0]['page'] == 0  # pylint:disable=C2001
    assert yaml['pages'][1]['page'] == 11


@utilotest.requires(hoverpower.DOCU027_PDF)
def test_yamlpages_compare_speed(testdir, capsys):
    source = hoverpower.link(hoverpower.DOCU027_PDF)
    filename = 'rawmaker__text_text.yaml'
    utilo.copy_content(
        source,
        dst=testdir.tmpdir,
        pattern=filename,
        unlock=True,
    )
    dumped = serializeraw.dump_document(
        serializeraw.load_document(filename),
        fast=False,
    )
    utilo.file_replace(filename, dumped)
    with utilo.level_tmp(utilo.Level.DEBUG):
        with utilo.profile('slow'):
            slow = serializeraw.load_document(filename, pages=10, fast=False)
        fast = os.path.join(source, filename)
        with utilo.profile('fast'):
            fast = serializeraw.load_document(fast, pages=10, fast=True)
    assert fast == slow
    # compare speed
    log = utilotest.stdout(capsys)
    times = utilo.parse_floats(log)
    assert times[1] < times[0], str(times)


@utilotest.requires(hoverpower.DOCU027_PDF)
def test_yamlpages_load(testdir):
    """Do not fail on raw yaml sources."""
    source = hoverpower.link(hoverpower.DOCU027_PDF)
    filename = 'rawmaker__text_text.yaml'
    utilo.copy_content(source, dst=testdir.tmpdir, pattern=filename)
    loaded = serializeraw.load_yamlpages(filename, pages=10)
    assert loaded
