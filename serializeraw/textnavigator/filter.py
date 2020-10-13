# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utila


def remove_magic(ptcns, magics, validtypes: set):
    for ptcn in ptcns:
        magic = utila.select_page(magics, ptcn.page)
        invalid = {
            number for number, typ in magic.content if typ not in validtypes
        }
        data = [item for index, item in enumerate(ptcn) if index not in invalid]
        ptcn.data = data
    return ptcns
