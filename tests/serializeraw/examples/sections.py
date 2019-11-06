# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

from functools import partial

from pytest import fixture

from iamraw import Sections
from iamraw.sections import PERCENT_100
from iamraw.sections import Appendix
from iamraw.sections import Chapter
from iamraw.sections import Index
from iamraw.sections import Introduction
from iamraw.sections import MainPart
from iamraw.sections import Percentage
from iamraw.sections import Position
from iamraw.sections import Table
from iamraw.sections import TableOfContent
from iamraw.sections import Text
from iamraw.sections import TitlePage
from iamraw.sections import WhitePage


@fixture
def restructured_sections_manual() -> Sections:
    result = Sections()

    def analyse(section, start, end):
        return section(result, start, end, PERCENT_100)
        # TODO: reactivate [start, START] later
        # return section(result, [start, START], [end, END], PERCENT_100)

    def add_children(parent, ctor, start, end):
        # new = ctor(parent, [start, START], [end, END], PERCENT_100)
        new = ctor(parent, start, end, PERCENT_100)
        return new

    # Page, Start
    # Intro
    intro = analyse(add_introduction, 0, 1)
    add_children(intro, add_title, 0, 0)
    add_children(intro, add_whitepage, 1, 1)

    # First pages with tables
    table_first = analyse(add_table, 2, 5)
    add_children(table_first, add_toc, 2, 2)
    add_children(table_first, add_whitepage, 3, 3)
    add_children(table_first, add_text, 4, 4)
    add_children(table_first, add_whitepage, 5, 5)

    # Content starts here
    content = analyse(add_content, 6, 25)
    add_chapter(content, 6, 7, number=1)
    add_chapter(content, 8, 9, number=2)
    add_chapter(content, 10, 11, number=3)
    add_chapter(content, 12, 17, number=4)
    add_chapter(content, 18, 19, number=5)
    add_chapter(content, 20, 21, number=6)
    add_chapter(content, 22, 23, number=7)
    add_chapter(content, 24, 25, number=8)

    # Second pages with table
    table_second = analyse(add_table, 26, 26)
    add_children(table_second, add_index, 26, 26)

    return result


def _add_x(
        root: Sections,  # or DocumentSection
        pstart: Position,
        pend: Position,
        trust: Percentage,
        constructor,
):
    insert = constructor(start=pstart, end=pend, trust=trust)
    root.content.append(insert)
    return insert


#pylint:disable=C0103
add_table = partial(_add_x, constructor=Table)
add_introduction = partial(_add_x, constructor=Introduction)
add_content = partial(_add_x, constructor=MainPart)
add_appendix = partial(_add_x, constructor=Appendix)

add_title = partial(_add_x, constructor=TitlePage)
add_whitepage = partial(_add_x, constructor=WhitePage)
add_toc = partial(_add_x, constructor=TableOfContent)
add_index = partial(_add_x, constructor=Index)
add_text = partial(_add_x, constructor=Text)


def add_chapter(
        root: MainPart,
        pstart: float,
        pend: float,
        trust: Percentage = PERCENT_100,
        number: int = 0,
):

    insert = Chapter(
        start=pstart,
        end=pend,
        # start=[pstart, START],
        # end=[pend, END],
        trust=trust,
        number=number,
    )
    root.content.append(insert)
    return insert
