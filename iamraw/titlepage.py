# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2020 by Helmut Konrad Fahrendholz. All rights reserved.
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

import collections
import dataclasses
import enum
import typing


class DocumentType(enum.Enum):
    NONE = enum.auto()
    STUDY = enum.auto()
    BACHELOR = enum.auto()
    MASTER = enum.auto()
    DOCTOR = enum.auto()
    BOOK = enum.auto()


THESIS = {
    DocumentType.STUDY: {
        'Komplexe Transferaufgabe',
        'Projektarbeit',
        'Projektpraktikum',
        'Studienarbeit',
    },
    DocumentType.BACHELOR: {
        'Bachelor',
        'Bachelorarbeit',
        'Bachelorthesis',
    },
    DocumentType.MASTER: {
        'Diplomarbeit',
        'Master',
        'Masterarbeit',
        'Masterthesis',
    },
    DocumentType.DOCTOR: {
        'Dissertation',
        'Doktor',
        'Doktorarbeit',
        'Promotion',
    },
}

TitleDate = collections.namedtuple(
    'TitleDate',
    'year month day location valid raw',
)

Person = collections.namedtuple('Person', 'title name firstname raw')
Persons = typing.List[Person]

Matrikel = collections.namedtuple('Matrikel', 'number intro raw')


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
    thesis: DocumentType = None
    date: TitleDate = None
    author: Person = None
    matrikel: Matrikel = None
    examiner: typing.List[Person] = dataclasses.field(default_factory=list)
    institution: Institution = None
    # page in pdf location to signal if first page was skipped
    pageraw: int = None


TitlePages = typing.List[TitlePage]

TitleThesisType = collections.namedtuple('TitleThesisType', 'typ title raw')
