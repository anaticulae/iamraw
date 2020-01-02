# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

from iamraw import PageList

EXAMPLE = [
    (8, [(2, 0,
          PageList(
              data=[
                  (0, 'Code: Block'),
                  (1, 'Code: Inline'),
                  (2, 'Emphasis: Italics'),
                  (3, 'Emphasis: Strong'),
                  (4, 'Headers'),
                  (5, 'Horizontal rules'),
                  (6, 'Images: Inline'),
                  (7, 'Line Return'),
                  (8, 'Links: Inline'),
                  (9, 'Links: Inline with title'),
                  (10, 'Links: Reference'),
                  (11, 'Lists: Simple'),
                  (12, 'Lists: Nested'),
                  (13, 'Paragraphs'),
                  (14, 'Images: Reference'),
              ],
              area=[4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]))]),
    (14, [(0, 0,
           PageList(
               data=[
                   (0, 'Index Page'),
                   (1, 'Support'),
                   (2, 'Installation'),
                   (3, 'Cookbook/Examples'),
                   (4, 'Command Line Options'),
                   (5, 'Changelog'),
               ],
               area=[3, 4, 5, 6, 7, 8]))]),
    (24, [(1, 0,
           PageList(
               data=[
                   (0, 'genindex'),
                   (1, 'modindex'),
                   (2, 'search'),
               ],
               area=[2, 3, 4]))]),
]
