# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================
"""Titlepage
==========

Definition
----------

* Institution - Institut
* Department - Fakultaet
* Institute - Institut
* Field - Fachgebiet
* Course of studies - Studiengang
* Academic year - Studienjahr/Semester
"""

import dataclasses
import typing

import iamraw

THESIS = {
    iamraw.DocumentType.HOMEWORK: {
        'Komplexe Transferaufgabe',
        'Projektarbeit',
        'Projektpraktikum',
        'Studienarbeit',
        'Wissenschaftliche Hausarbeit',
    },
    iamraw.DocumentType.BACHELOR: {
        'Bachelor',
        'Bachelorarbeit',
        'Bachelorthesis',
    },
    iamraw.DocumentType.MASTER: {
        'Diplomarbeit',
        'Master',
        'Master Thesis',
        'Masterarbeit',
        'Masterthesis',
    },
    iamraw.DocumentType.DISS: {
        'Dissertation',
        'Doktor',
        'Doktorarbeit',
        'Promotion',
    },
    iamraw.DocumentType.HABIL: {
        'Habilitation',
        'Habilitationsschrift',
    },
}


@dataclasses.dataclass
class TitleDate:
    year: int = None
    month: int = None
    day: int = None
    location: str = None
    valid: bool = False
    raw: str = None


@dataclasses.dataclass
class Matrikel:
    number: int = None
    intro: str = None
    raw: str = None


@dataclasses.dataclass
class Institution:
    courseofstudies: str = None
    department: str = None
    field: str = None
    institute: str = None
    university: str = None


@dataclasses.dataclass
class TitlePage:
    title: str = ''
    thesis: iamraw.DocumentType = None
    date: TitleDate = None
    author: iamraw.Person = None
    matrikel: Matrikel = None
    examiner: iamraw.Persons = dataclasses.field(default_factory=list)
    institution: Institution = None
    # Some user put the page number on the title page which is not correct
    pagenumber: str = None
    # page in pdf location to signal if first page was skipped
    pageraw: int = None


TitlePages = typing.List[TitlePage]


@dataclasses.dataclass
class TitleThesisType:
    typ: str = None
    title: str = None
    raw: str = None
