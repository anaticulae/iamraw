# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2022-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import math

import utila

import texmex
import texmex.group.ml
import texmex.nav


@utila.rename(
    max_distance='distance_max',
    max_sizediff='sizediff_max',
)
def group_linedistances_complex(
    content: texmex.nav.PTN,
    sizediff_max: float = texmex.group.ml.SIZEDIFF_MAX,
    distance_max: callable = texmex.group.ml.maxdistance,
    xdist_max: float = None,
    returndata: bool = False,
) -> list[int]:
    """Group lines by sizes and distances of text chunks.

    Args:
        content: content to group
        sizediff_max: absolute difference of 2 font size in one group
        distance_max: function to determine limit maxmimal distance
                      between 2 lines in a group.
        xdist_max: max xdist change to be in the same group
        returndata: convert indexes to data
    Returns:
        List of grouped indexes
    """
    assert isinstance(content, texmex.NavigatorMixin), type(content)
    prepared = setup(content, returndata=returndata)
    if isinstance(prepared, list):
        return prepared
    result = []
    current_group = []
    cursize = None
    for index, (size, distance, xdist) in enumerate(prepared):
        if cursize is None:
            if distance > distance_max(size):
                result.append([index])
            else:
                current_group.append(index)
                cursize = size
            continue
        if xdist_max is not None and xdist > xdist_max:
            # xdist is to high
            result.append(current_group)
            current_group = [index]
            cursize = None
            continue
        sizediff = utila.roundme(math.fabs(cursize - size))
        if sizediff < sizediff_max:
            if distance < distance_max(size):
                current_group.append(index)
            else:
                current_group.append(index)
                result.append(current_group)
                current_group = []
                cursize = None
        else:
            result.append(current_group)
            current_group = [index]
            cursize = None
    if current_group:
        result.append(current_group)
    result = finish(result, content, returndata=returndata)
    return result


def setup(content, returndata: bool = False):
    if len(content) == 0:  # pylint:disable=compare-to-zero
        return []
    if len(content) == 1:
        return [content[0]] if returndata else [[0]]
    distances = texmex.group.ml.linedistances(content)
    sizes = [max((item.size for item in items.style)) for items in content]
    xdists = texmex.group.ml.xdistances(content)
    assert len(distances) == len(sizes) == len(xdists)
    if len(distances) < 2:
        return []
    distances = distances[:]
    # remove None at end of distances
    distances[-1] = distances[-2]
    return zip(sizes, distances, xdists)


def finish(result, ptxn, returndata: bool = False):
    if not returndata:
        return result
    # replace group index by navigator data
    result = [[ptxn[index] for index in group] for group in result]
    return result
