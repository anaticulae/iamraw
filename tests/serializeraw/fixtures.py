# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================
from pytest import fixture

from iamraw import Border
from iamraw import PageBoundings
from iamraw import PageSize
from iamraw import PageSizeBorder


@fixture
def boxdata_from_pdf():
    size = [
        PageSize(width=595.28, height=841.89),
        PageSize(width=None, height=None),
        PageSize(width=595.28, height=841.89),
        PageSize(width=595.28, height=841.89),
        PageSize(width=595.28, height=841.89),
        PageSize(width=595.28, height=841.89),
        PageSize(width=595.28, height=841.89),
        PageSize(width=595.28, height=841.89),
        PageSize(width=595.28, height=841.89),
        PageSize(width=595.28, height=841.89),
        PageSize(width=595.28, height=841.89),
        PageSize(width=595.28, height=841.89),
        PageSize(width=595.28, height=841.89)
    ]
    border = [
        Border(left=194.37, right=400.9, top=648.34, bottom=72.0),
        Border(left=None, right=None, top=None, bottom=None),
        Border(left=50.4, right=544.88, top=700.78, bottom=40.18),
        Border(left=50.4, right=544.88, top=807.93, bottom=41.15),
        Border(left=50.4, right=544.88, top=807.93, bottom=41.15),
        Border(left=47.01, right=548.26, top=807.93, bottom=41.15),
        Border(left=50.4, right=544.88, top=807.93, bottom=41.15),
        Border(left=50.4, right=544.89, top=807.93, bottom=41.15),
        Border(left=50.4, right=544.88, top=807.93, bottom=41.15),
        Border(left=50.4, right=544.88, top=807.93, bottom=41.15),
        Border(left=50.4, right=544.89, top=807.93, bottom=41.15),
        Border(left=50.4, right=544.89, top=807.93, bottom=41.15),
        Border(left=50.4, right=544.88, top=807.93, bottom=41.15)
    ]

    sizesandborders = [
        PageSizeBorder(size=size, border=border, page=index)
        for index, (size, border) in enumerate(zip(size, border))
    ]

    boxes = [
        PageBoundings(
            boundings=[
                # First page
                [0, [232.4, 617.65, 362.87, 648.34]],
                [1, [224.79, 370.83, 370.49, 388.49]],
                [2, [240.4, 354.94, 354.88, 366.23]],
                [3, [237.65, 338.0, 357.62, 349.29]],
                [4, [194.37, 72.0, 400.9, 83.29]],
                [5, [207.64, 403.5, 387.64, 610.5]],
            ],
            page=0,
        ),
        PageBoundings(
            boundings=[
                # Second page
                [6, [50.4, 669.44, 244.84, 700.13]],
                [7, [50.4, 570.7, 136.23, 583.2]],
                [8, [50.4, 548.78, 146.45, 561.29]],
                [9, [88.25, 514.85, 113.51, 527.38]],
                [10, [65.34, 72.51, 520.54, 551.29]],
                [11, [541.69, 570.7, 544.88, 583.2]],
                [12, [534.91, 72.51, 544.88, 561.29]],
                [13, [541.69, 40.18, 544.88, 52.68]],
                [14, [50.4, 54.27, 544.88, 54.27]],
            ],
            page=1,
        ),
        PageBoundings(
            boundings=[
                # Third page
                [15, [50.4, 675.22, 154.43, 700.78]],
                [16, [50.4, 618.63, 234.5, 649.32]],
                [17, [65.34, 553.7, 544.87, 578.19]],
                [18, [75.31, 541.75, 129.59, 554.28]],
                [19, [97.22, 521.72, 464.3, 532.51]],
                [20, [97.22, 476.92, 501.96, 510.59]],
                [21, [65.34, 447.3, 544.87, 471.79]],
                [22, [75.31, 435.34, 526.64, 447.88]],
                [23, [65.34, 423.39, 544.87, 435.92]],
                [24, [75.31, 411.43, 474.35, 423.97]],
                [25, [65.34, 399.48, 544.87, 412.01]],
                [26, [75.31, 387.52, 109.11, 400.06]],
                [27, [65.34, 375.57, 312.67, 388.1]],
                [28, [50.4, 333.87, 169.51, 351.53]],
                [29, [121.75, 78.12, 203.92, 310.73]],
                [30, [216.67, 78.12, 473.53, 310.73]],
                [31, [539.15, 40.18, 544.88, 52.68]],
                [32, [94.23, 471.61, 525.95, 532.38]],
            ],
            page=2,
        ),
    ]
    return sizesandborders, boxes
