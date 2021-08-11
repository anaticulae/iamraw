# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os

import power
import utila
import utilatest

import serializeraw


def test_yamlpages_write(testdir):
    source = power.link(power.DOCU27_PDF)
    filename = 'rawmaker__text_text.yaml'
    utila.copy_content(
        source,
        dest=testdir.tmpdir,
        pattern=filename,
    )
    dumped = serializeraw.dump_document(
        serializeraw.load_document(filename),
        fast=False,
    )
    utila.file_replace(filename, dumped)
    serializeraw.write_yamlpages(filename)
    loaded = serializeraw.load_yamlpages(filename, pages=10)
    yaml = utila.yaml_from_raw_or_path(loaded)
    assert yaml['dimension']
    assert yaml['pages'][0]['page'] == 10
    # double page test
    loaded = serializeraw.load_yamlpages(filename, pages=(0, 11))
    yaml = utila.yaml_from_raw_or_path(loaded)
    assert yaml['pages'][0]['page'] == 0
    assert yaml['pages'][1]['page'] == 11


def test_yamlpages_compare_speed(testdir, capsys):
    source = power.link(power.DOCU27_PDF)
    filename = 'rawmaker__text_text.yaml'
    utila.copy_content(
        source,
        dest=testdir.tmpdir,
        pattern=filename,
    )
    dumped = serializeraw.dump_document(
        serializeraw.load_document(filename),
        fast=False,
    )
    utila.file_replace(filename, dumped)
    with utila.level_temp(utila.Level.DEBUG):
        with utila.profile('slow'):
            slow = serializeraw.load_document(filename, pages=10, fast=False)
        fast = os.path.join(source, filename)
        with utila.profile('fast'):
            fast = serializeraw.load_document(fast, pages=10, fast=True)
    assert fast == slow
    # compare speed
    log = utilatest.stdout(capsys)
    times = utila.parse_floats(log)
    assert times[1] < times[0], str(times)


def test_yamlpages_load(testdir):
    """Do not fail on raw yaml sources."""
    source = power.link(power.DOCU27_PDF)
    filename = 'rawmaker__text_text.yaml'
    utila.copy_content(source, dest=testdir.tmpdir, pattern=filename)
    loaded = serializeraw.load_yamlpages(filename, pages=10)
    assert loaded
