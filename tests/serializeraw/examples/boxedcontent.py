# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

from iamraw import BoundingBox

# pylint:disable=C0301
EXAMPLE = [
    # page 9
    (9, [
        (0, 0, [
            [
                (BoundingBox(x0=68.61, y0=140.62, x1=543.39, y1=223.71),
                 (1, [(BoundingBox(x0=72.00, y0=143.40, x1=179.60,
                                   y1=152.80), 3, 'This is normal text.'),
                      (BoundingBox(x0=93.52, y0=165.32, x1=222.64,
                                   y1=174.72), 4, 'This is blockquoted text'),
                      (BoundingBox(x0=93.52, y0=187.24, x1=340.99, y1=196.64),
                       5, 'This is another paragraph of blockquoted text.'),
                      (BoundingBox(x0=115.04, y0=209.16, x1=281.81, y1=218.56),
                       6, 'This is a nested block of text.')])),
            ],
        ]),
        (0, 1, [
            [(BoundingBox(x0=68.61, y0=251.01, x1=543.39, y1=345.06), (0, [
                (BoundingBox(x0=72.00, y0=252.70, x1=367.89,
                             y1=339.90), 8, """<p>This is normal text.</p>/
<blockquote>/
<div><p>This is blockquoted text</p>/
<p>This is another paragraph of blockquoted text.</p>/
<blockquote>/
<div>This is a nested block of text.</div></blockquote>/
</div></blockquote>/
</div>""")
            ]))],
        ]),
    ]),
    # page 12
    (12, [
        (3, 0, [[(BoundingBox(x0=68.61, y0=463.35, x1=543.39,
                              y1=480.68), (0, [(BoundingBox(x0=72.00,
                                                            y0=466.13,
                                                            x1=190.36,
                                                            y1=475.53), 6,
                                                'reST -> Sphinx -> HTML')]))]]),
        (3, 1, [[(BoundingBox(x0=68.61, y0=600.08, x1=543.39, y1=617.41), (1, [
            (BoundingBox(x0=72.00, y0=602.86, x1=201.12,
                         y1=612.26), 10, 'sudo easy_install Sphinx')
        ]))]])
    ]),
    (13, [(0, 0, [
        [
            (BoundingBox(x0=68.61, y0=127.45, x1=543.39, y1=177.66), (4, [
                (BoundingBox(x0=72.00, y0=130.23, x1=141.94,
                             y1=172.50), 2, """mkdir crawler/
cd crawler/
mkdir docs/
cd docs"""),
            ])),
        ],
    ]),
          (0, 1, [[(BoundingBox(x0=68.61, y0=204.96, x1=543.39,
                                y1=222.29), (0, [(BoundingBox(x0=72.00,
                                                              y0=207.74,
                                                              x1=163.46,
                                                              y1=217.14), 4,
                                                  'sphinx-quickstart')]))]]),
          (0, 2, [
              [
                  (BoundingBox(x0=68.61, y0=261.55, x1=543.39,
                               y1=322.72), (1, [
                                   (BoundingBox(x0=72.00,
                                                y0=264.33,
                                                x1=115.04,
                                                y1=273.73), 6, 'crawler/'),
                                   (BoundingBox(x0=93.52,
                                                y0=275.29,
                                                x1=120.42,
                                                y1=284.69), 7, 'docs/'),
                                   (BoundingBox(x0=115.04,
                                                y0=286.24,
                                                x1=163.46,
                                                y1=317.55), 8, """conf.py/
index.rst/
Makefile"""),
                               ])),
              ],
          ]),
          (0, 3, [[(BoundingBox(x0=68.61, y0=537.76, x1=543.39,
                                y1=566.05), (2, [
                                    (BoundingBox(x0=72.00,
                                                 y0=540.54,
                                                 x1=260.29,
                                                 y1=560.90), 20,
                                     """# Inside top-level docs/ directory./
make html""")
                                ]))]]),
          (0, 4, [[(BoundingBox(x0=68.61, y0=605.30, x1=543.39,
                                y1=622.64), (3, [(BoundingBox(x0=72.00,
                                                              y0=608.08,
                                                              x1=217.26,
                                                              y1=617.48), 22,
                                                  'open _build/html/index.html')
                                                ]))]])]),
    # page 14
    (14, [
        (0, 1, [
            [
                (BoundingBox(x0=68.61, y0=357.03, x1=543.39, y1=505.88), (0, [
                    (BoundingBox(x0=72.00, y0=359.82, x1=109.66,
                                 y1=391.13), 13, """=======/
Support/
======="""),
                    (BoundingBox(x0=72.00, y0=403.65, x1=475.49, y1=434.96), 14,
                     """The easiest way to get help with the project is to join the ``#crawler``/
channel on Freenode_. We hang out there and you can get real-time help with/
your projects. The other good way is to open an issue on Github_."""),
                    (BoundingBox(x0=72.00, y0=447.49, x1=529.29, y1=456.89), 15,
                     'The mailing list at https://groups.google.com/forum/#!forum/crawler is also available'
                    ),
                    (BoundingBox(x0=74.92, y0=458.45, x1=147.32,
                                 y1=467.85), 16, '/u02d3/u2192for support.'),
                    (BoundingBox(x0=72.00, y0=480.36, x1=351.75, y1=500.72), 17,
                     """.. _Freenode: irc://freenode.net/
.. _Github: http://github.com/example/crawler/issues"""),
                ])),
            ],
        ]),
    ]),
]
