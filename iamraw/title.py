# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
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
    def merges(items) -> 'iamraw.AcademicTitle':
        """\
        >>> AcademicTitle.merges((AcademicTitle.PROF, AcademicTitle.DR))
        <AcademicTitle.DR|PROF: 96>
        """
        if not items:
            return None
        result = items[0]
        for item in items:
            if not item:
                continue
            result |= item
        return result


PROF_DR = AcademicTitle.PROF | AcademicTitle.DR
