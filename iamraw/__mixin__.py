# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================
"""\
>>> @extracted
... class Helmut:
...     pass
>>> first = Helmut()
>>> first.__strategy__ = 'hello'
>>> first.__strategy__
'hello'
"""


def extracted(item):
    setattr(item, '__strategy__', None)
    setattr(item, '__strategy_location__', None)

    def raw(self) -> str:
        """Element in document which is converted to current result."""
        raise NotImplementedError

    setattr(item, '__strategy_raw__', raw)
    return item


def hasstrategy(item) -> bool:
    return hasattr(item, '__strategy__')
