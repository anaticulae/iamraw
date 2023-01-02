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


def example() -> iamraw.DocumentIndex:
    result = iamraw.DocumentIndex()
    result.add(
        cat='Symbols',
        title='per cent syndrome',
        page=[76, 77],
        raw='95 per cent syndrome, 76, 77',
    )
    return result


def test_index_dump_load():
    current = example()
    dumped = serializeraw.dump_index(current)
    loaded = serializeraw.load_index(dumped)
    assert loaded == current
