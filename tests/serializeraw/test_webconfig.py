# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2022-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import iamraw
import serializeraw


def test_webconfig_dump_load(testdir):
    config = iamraw.WebConfig()
    config.decider.append('first')
    config.decider.append('third')
    config.decider.append('second')
    config.decider.sort()
    path = testdir.tmpdir.join('abc.config')
    serializeraw.dump_webconfig(path, config)
    loaded = serializeraw.load_webconfig(path)
    assert loaded == config
