# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import iamraw
import iamraw.caption


def test_pagecaptions_toraw():
    pagecaptions = [
        iamraw.PageContentCaption(
            page=5,
            content=[
                iamraw.Caption(
                    line=3,
                    lineend=5,
                    raw='This is my first caption',
                ),
                iamraw.Caption(
                    line=10,
                    raw='This is my second caption',
                ),
            ],
        ),
        iamraw.PageContentCaption(
            page=8,
            content=[
                iamraw.Caption(
                    line=6,
                    raw='This is my third caption',
                ),
            ],
        )
    ]
    raw = iamraw.caption.pagecaptions_toraw(pagecaptions)
    expected = [
        {
            'page':
                5,
            'captions': [
                {
                    'line': 3,
                    'raw': 'This is my first caption',
                    'lineend': 5
                },
                {
                    'line': 10,
                    'raw': 'This is my second caption'
                },
            ]
        },
        {
            'page': 8,
            'captions': [{
                'line': 6,
                'raw': 'This is my third caption'
            },]
        },
    ]
    assert raw == expected
