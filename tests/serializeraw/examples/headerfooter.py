# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

from iamraw import BoundingBox
from iamraw import FixedFooterInfo
from iamraw import FixedHeaderInfo
from iamraw import FootNoteMerged
from iamraw import FootNoteRaw
from iamraw import HeaderTitle
from iamraw import MovingFooterInfo
from iamraw import PageContentFooterHeader
from iamraw import PageInformation
from iamraw import PagesFooterInfo
from iamraw import RawText

FOOTER_HEADER = [
    PageContentFooterHeader(header=None, footer=None, page=2),
    PageContentFooterHeader(header=None, footer=None, page=3),
    PageContentFooterHeader(header=None, footer=None, page=4),
    PageContentFooterHeader(header=None, footer=None, page=6),
    PageContentFooterHeader(header=None, footer=None, page=7),
    PageContentFooterHeader(
        header=None,
        footer=MovingFooterInfo(
            begin=0.81,
            end=1.0,
            page=None,
            notes=[
                FootNoteRaw(
                    number='1',
                    text='Personal Digital Assistant.',
                    raw='1Personal Digital Assistant.',
                ),
                FootNoteRaw(
                    number='2',
                    text='Operating System.',
                    raw='2Operating System.',
                )
            ],
        ),
        page=9,
    ),
    PageContentFooterHeader(
        header=None,
        footer=MovingFooterInfo(
            begin=0.76,
            end=1.0,
            page=None,
            notes=[
                FootNoteRaw(
                    number='3',
                    text='Eclipse ist eine Gemeinschaft die sich mit ',
                    raw='3Eclipse ist eine Gemeinschaft die sich mit ',
                ),
                FootNoteRaw(
                    number='4',
                    text='Java Standard Edition',
                    raw='4Java Standard Edition',
                ),
                FootNoteRaw(
                    number='5',
                    text='Software Development Kit',
                    raw='5Software Development Kit',
                )
            ],
        ),
        page=10,
    ),
    PageContentFooterHeader(
        header=None,
        footer=MovingFooterInfo(
            begin=0.81,
            end=1.0,
            page=None,
            notes=[
                FootNoteRaw(
                    number='6',
                    text='Virtual Machine',
                    raw='6Virtual Machine',
                ),
                FootNoteRaw(
                    number='7',
                    text='Application Programming Interface',
                    raw='7Application Programming Interface',
                )
            ],
        ),
        page=11,
    ),
    PageContentFooterHeader(
        header=None,
        footer=MovingFooterInfo(
            begin=0.82,
            end=1.0,
            page=None,
            notes=[
                FootNoteRaw(
                    number='8',
                    text='Graphical User Interface',
                    raw='8Graphical User Interface',
                )
            ],
        ),
        page=12,
    ),
    PageContentFooterHeader(
        header=None,
        footer=MovingFooterInfo(
            begin=0.79,
            end=1.0,
            page=None,
            notes=[
                FootNoteRaw(
                    number='21',
                    text='High Speed Packet Access',
                    raw='21High Speed Packet Access',
                ),
                FootNoteMerged(notes=[
                    FootNoteRaw(
                        number='22',
                        text='Orthogonal-Frequency-Division-Multiplexing',
                        raw='22Orthogonal-Frequency-Division-Multiplexing',
                    ),
                    FootNoteRaw(
                        number='23',
                        text='Multiple-Input-Multiple-Output',
                        raw='23Multiple-Input-Multiple-Output',
                    ),
                ]),
            ],
        ),
        page=18,
    ),
    PageContentFooterHeader(
        header=None,
        footer=MovingFooterInfo(
            begin=0.81,
            end=1.0,
            page=None,
            notes=[
                FootNoteRaw(
                    number='24',
                    text='Industrial, scientific, medical',
                    raw='24Industrial, scientific, medical',
                ),
            ],
        ),
        page=19,
    ),
]

SECOND = [
    PageContentFooterHeader(
        header=FixedHeaderInfo(
            begin=0.0,
            end=0.14,
            page=PageInformation(value='ii', raw='ii'),
            title=None,
            undefined=[RawText(text='INHALTSVERZEICHNIS')],
            images=[],
        ),
        footer=None,
        page=2,
    ),
    PageContentFooterHeader(
        header=FixedHeaderInfo(
            begin=0.0,
            end=0.14,
            page=PageInformation(value='iii', raw='iii'),
            title=None,
            undefined=[RawText(text='INHALTSVERZEICHNIS')],
            images=[],
        ),
        footer=None,
        page=3,
    ),
    PageContentFooterHeader(
        header=FixedHeaderInfo(
            begin=0.0,
            end=0.14,
            page=PageInformation(value='iv', raw='iv'),
            title=None,
            undefined=[RawText(text='INHALTSVERZEICHNIS')],
            images=[],
        ),
        footer=None,
        page=4,
    ),
    PageContentFooterHeader(
        header=FixedHeaderInfo(
            begin=0.0,
            end=0.14,
            page=PageInformation(value='2', raw='2'),
            title=HeaderTitle(title='MOTIVATION UND ZIELSETZUNG',
                              raw='1.1. MOTIVATION UND ZIELSETZUNG'),
            undefined=[],
            images=[],
        ),
        footer=None,
        page=6,
    ),
    PageContentFooterHeader(
        header=FixedHeaderInfo(
            begin=0.0,
            end=0.14,
            page=PageInformation(value='3', raw='3'),
            title=HeaderTitle(title='AUFBAU DER ARBEIT',
                              raw='1.2. AUFBAU DER ARBEIT'),
            undefined=[],
            images=[],
        ),
        footer=None,
        page=7,
    ),
    PageContentFooterHeader(
        header=FixedHeaderInfo(
            begin=0.0,
            end=0.14,
            page=PageInformation(value='5', raw='5'),
            title=HeaderTitle(title='SMARTPHONES', raw='2.1. SMARTPHONES'),
            undefined=[],
            images=[],
        ),
        footer=None,
        page=9,
    ),
    PageContentFooterHeader(
        header=FixedHeaderInfo(
            begin=0.0,
            end=0.14,
            page=PageInformation(value='9', raw='9'),
            title=HeaderTitle(title='SMARTPHONES', raw='2.1. SMARTPHONES'),
            undefined=[],
            images=[],
        ),
        footer=None,
        page=13,
    ),
    PageContentFooterHeader(
        header=FixedHeaderInfo(
            begin=0.0,
            end=0.14,
            page=PageInformation(value='10', raw='10'),
            title=HeaderTitle(title='SMARTPHONES', raw='2.1. SMARTPHONES'),
            undefined=[],
            images=[],
        ),
        footer=None,
        page=14,
    ),
    PageContentFooterHeader(
        header=FixedHeaderInfo(
            begin=0.0,
            end=0.14,
            page=PageInformation(value='11', raw='11'),
            title=HeaderTitle(title='DRAHTLOSE KOMMUNIKATIONSTECHNOLOGIEN',
                              raw='2.2. DRAHTLOSE KOMMUNIKATIONSTECHNOLOGIEN'),
            undefined=[],
            images=[],
        ),
        footer=None,
        page=15,
    ),
    PageContentFooterHeader(
        header=FixedHeaderInfo(
            begin=0.0,
            end=0.14,
            page=PageInformation(value='12', raw='12'),
            title=HeaderTitle(title='DRAHTLOSE KOMMUNIKATIONSTECHNOLOGIEN',
                              raw='2.2. DRAHTLOSE KOMMUNIKATIONSTECHNOLOGIEN'),
            undefined=[],
            images=[],
        ),
        footer=None,
        page=16,
    ),
]
THIRD = [
    PageContentFooterHeader(
        header=None,
        footer=PagesFooterInfo(
            begin=0.95,
            end=1.0,
            page=None,
            page_location=BoundingBox(x0=291.77,
                                      y0=797.35,
                                      x1=307.96,
                                      y1=806.35),
        ),
        page=1,
    ),
    PageContentFooterHeader(
        header=None,
        footer=PagesFooterInfo(
            begin=0.95,
            end=1.0,
            page=None,
            page_location=BoundingBox(x0=291.77,
                                      y0=797.35,
                                      x1=307.96,
                                      y1=806.35),
        ),
        page=2,
    ),
    PageContentFooterHeader(
        header=None,
        footer=PagesFooterInfo(
            begin=0.95,
            end=1.0,
            page=None,
            page_location=BoundingBox(x0=291.77,
                                      y0=797.35,
                                      x1=307.96,
                                      y1=806.35),
        ),
        page=6,
    ),
    PageContentFooterHeader(
        header=None,
        footer=PagesFooterInfo(
            begin=0.95,
            end=1.0,
            page=None,
            page_location=BoundingBox(x0=291.77,
                                      y0=797.35,
                                      x1=307.96,
                                      y1=806.35),
        ),
        page=7,
    ),
    PageContentFooterHeader(
        header=None,
        footer=PagesFooterInfo(
            begin=0.95,
            end=1.0,
            page=None,
            page_location=BoundingBox(x0=291.77,
                                      y0=797.35,
                                      x1=307.96,
                                      y1=806.35),
        ),
        page=8,
    ),
]

FOURTH = [
    PageContentFooterHeader(header=None, footer=None, page=0),
    PageContentFooterHeader(
        header=None,
        footer=FixedFooterInfo(begin=0.93, end=1.0, page=None),
        page=2,
    ),
    PageContentFooterHeader(
        header=None,
        footer=FixedFooterInfo(begin=0.93, end=1.0, page=None),
        page=3,
    ),
    PageContentFooterHeader(
        header=FixedHeaderInfo(
            begin=0.0,
            end=0.07,
            page=None,
            title=None,
            undefined=[
                RawText(
                    text='The RestructuredText Book Documentation, Release 0.1'
                ),
            ],
            images=[]),
        footer=FixedFooterInfo(begin=0.93, end=1.0, page=None),
        page=4,
    ),
    PageContentFooterHeader(
        header=FixedHeaderInfo(
            begin=0.0,
            end=0.07,
            page=None,
            title=None,
            undefined=[
                RawText(
                    text='The RestructuredText Book Documentation, Release 0.1')
            ],
            images=[]),
        footer=FixedFooterInfo(begin=0.93, end=1.0, page=None),
        page=5,
    ),
    PageContentFooterHeader(
        header=None,
        footer=FixedFooterInfo(begin=0.93, end=1.0, page=None),
        page=6,
    ),
    PageContentFooterHeader(
        header=FixedHeaderInfo(
            begin=0.0,
            end=0.07,
            page=None,
            title=None,
            undefined=[
                RawText(
                    text='The RestructuredText Book Documentation, Release 0.1'
                ),
            ],
            images=[]),
        footer=FixedFooterInfo(begin=0.93, end=1.0, page=None),
        page=7,
    ),
    PageContentFooterHeader(
        header=None,
        footer=FixedFooterInfo(begin=0.93, end=1.0, page=None),
        page=8,
    ),
    PageContentFooterHeader(
        header=FixedHeaderInfo(
            begin=0.0,
            end=0.07,
            page=None,
            title=None,
            undefined=[
                RawText(
                    text='The RestructuredText Book Documentation, Release 0.1'
                ),
            ],
            images=[]),
        footer=FixedFooterInfo(begin=0.93, end=1.0, page=None),
        page=9,
    ),
    PageContentFooterHeader(
        header=None,
        footer=FixedFooterInfo(begin=0.93, end=1.0, page=None),
        page=10,
    ),
    PageContentFooterHeader(
        header=FixedHeaderInfo(
            begin=0.0,
            end=0.07,
            page=None,
            title=None,
            undefined=[
                RawText(
                    text='The RestructuredText Book Documentation, Release 0.1'
                ),
            ],
            images=[]),
        footer=FixedFooterInfo(begin=0.93, end=1.0, page=None),
        page=11,
    ),
    PageContentFooterHeader(
        header=None,
        footer=FixedFooterInfo(begin=0.93, end=1.0, page=None),
        page=12,
    ),
    PageContentFooterHeader(
        header=FixedHeaderInfo(
            begin=0.0,
            end=0.07,
            page=None,
            title=None,
            undefined=[
                RawText(
                    text='The RestructuredText Book Documentation, Release 0.1'
                ),
            ],
            images=[]),
        footer=FixedFooterInfo(begin=0.93, end=1.0, page=None),
        page=13,
    ),
]
