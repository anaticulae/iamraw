# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================
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
    r'Dipl.-\w+': AcademicTitle.MASTER,
    'Dipl. Ing.': AcademicTitle.MASTER,
    'M.A.': AcademicTitle.MASTER,
    'M.Sc.': AcademicTitle.MASTER,
    'Dr.-Ing.': AcademicTitle.DR,
    'Dr.': AcademicTitle.DR,
    'Prof.': AcademicTitle.PROF,
    r'\w+. ': AcademicTitle.DR,
    # see general pattern above
    # 'Dr. rer. biol. hum.': Title.DR,
    # 'Dr. med.': Title.DR,
}
