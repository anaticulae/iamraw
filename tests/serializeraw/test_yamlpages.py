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
        destination=testdir.tmpdir,
        pattern=filename,
    )
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
        destination=testdir.tmpdir,
        pattern=filename,
    )
    serializeraw.write_yamlpages(filename)
    no_optimization = os.path.join(source, filename)

    with utila.profile('fast'):
        loaded = serializeraw.load_yamlpages(filename, pages=10)
        fast = loaded = serializeraw.load_document(loaded)
    assert fast
    assert len(fast) == 1

    with utila.profile('no_optimization'):
        slow = serializeraw.load_document(no_optimization, pages=10)
    assert fast == slow

    log = utilatest.stdout(capsys)
    times = utila.parse_floats(log)
    assert times[0] < times[1], str(times)


def test_yamlpages_load(testdir):
    """Do not fail on raw yaml sources."""
    source = power.link(power.DOCU27_PDF)
    filename = 'rawmaker__text_text.yaml'
    utila.copy_content(source, destination=testdir.tmpdir, pattern=filename)
    loaded = serializeraw.load_yamlpages(filename, pages=10)
    assert loaded
