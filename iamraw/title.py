# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================
"""Person
======

>>> assert AcademicTitle.STUDENT < AcademicTitle.PROF
>>> assert AcademicTitle.DR < AcademicTitle.PROF
>>> assert AcademicTitle.DR < PROF_DR
"""

import enum


class AcademicTitle(enum.Flag):
    NO_TITLE = enum.auto()
    STUDENT = enum.auto()  # author without academic title
    BSC = enum.auto()
    MASTER = enum.auto()
    EXAMINIER = enum.auto()  # examiner without academic title
    DR = enum.auto()
    PROF = enum.auto()

    def __lt__(self, item):
        # make `Title` orderable
        try:
            return self.value < item.value  # pylint:disable=comparison-with-callable
        except ValueError:
            return False
        except AttributeError:
            return False

    @staticmethod
    def fromstring(value):
        """\
        >>> AcademicTitle.fromstring('M.Sc.')
        <AcademicTitle.MASTER: ...>
        """
        # TODO: DECOUPLE FROM AcademicTitle and use regex matches also
        try:
            return MATCHES[value]
        except KeyError:
            return None

    @staticmethod
    def keys():
        return [item for item in MATCHES]


PROF_DR = AcademicTitle.PROF | AcademicTitle.DR

MATCHES = {
    'B.Sc.': AcademicTitle.BSC,
    'Dipl.(-| )Ing.': AcademicTitle.MASTER,
    r'Dipl.-\w+': AcademicTitle.MASTER,
    'M.A.': AcademicTitle.MASTER,
    'M.Sc.': AcademicTitle.MASTER,
    'Dr.-Ing.': AcademicTitle.DR,
    'Dr.': AcademicTitle.DR,
    # TODO: ADD GENERAL -/RULE?
    'Prof.[-]{0,1}': AcademicTitle.PROF,
    # minimum two chapters to distinguish from first names
    r'[a-zA-Z\-]{2,}. ': AcademicTitle.DR,
    # see general pattern above
    # 'Dr. rer. biol. hum.': AcademicTitle.DR,
    # 'Dr. med.': AcademicTitle.DR,
}
