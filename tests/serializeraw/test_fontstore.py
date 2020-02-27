# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import iamraw
import serializeraw
import tests.serializeraw


def test_fontstore_font_to_fontid():
    # prepare sample font store
    # pylint:disable=C0103
    f0 = iamraw.Font(name='SuperFont', scale=12.5)
    f1 = iamraw.Font(name='Arial', scale=12.5)
    f2 = iamraw.Font(name='Verdana', scale=17.5)
    f3 = iamraw.Font(name='Times', scale=5)
    f4 = iamraw.Font(name='Arial', scale=20)
    f5 = iamraw.Font(name='Arial', scale=5)
    header = [f0, f1, f2, f3, f4, f5]
    content = [iamraw.PageFontContent(content=[], page=0)]

    store = iamraw.FontStore(header, content)
    assert store.font_to_fontid(f4) == hash(f4)
    assert store.font_to_fontid(f3) == hash(f3)
    assert store.font_to_fontid(f3) == hash(f3)
    assert store.font_to_fontid(f0) == hash(f0)
    assert store.font_to_fontid(f5) == hash(f5)


def test_fontstore_from_path():
    source = tests.serializeraw.RESTRUCTURED
    loaded = serializeraw.create_fontstore_frompath(source)
    assert loaded, loaded

    shrunken = serializeraw.create_fontstore_frompath(source, pages=(0, 1, 2))
    assert shrunken

    assert loaded != shrunken


def test_fontstore_font_access():
    source = tests.serializeraw.RESTRUCTURED
    loaded = serializeraw.create_fontstore_frompath(source)
    fontid = loaded.fontid(0, 0, 0, 0)
    font = loaded.font(0, 0, 0, 0)

    assert loaded[fontid] == font
