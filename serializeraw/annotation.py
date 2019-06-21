# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

from utila import from_raw_or_path
from yaml import FullLoader
from yaml import dump
from yaml import load

from iamraw import BoundingBox
from iamraw import HyperLink
from iamraw import PageAnnotations
from iamraw import PageLink


def dump_annotations(annotations: PageAnnotations) -> str:
    raw = []
    for page in annotations:
        pagelink, hyperlink = page

        rawpage = [{
            'goto': link.goal,
            'bounds': link.bounds.raw(),
        } for link in pagelink]

        rawhyper = [{
            'href': link.goal,
            'bounds': link.bounds.raw(),
        } for link in hyperlink]

        raw.append([
            rawpage,
            rawhyper,
        ])
    dumped = dump(raw)
    return dumped


def load_annotations(content: str) -> PageAnnotations:
    content = from_raw_or_path(content, ftype='yaml')
    loaded = load(content, Loader=FullLoader)
    result = []
    for page in loaded:
        pagelinks = [
            PageLink(
                goal=item['goto'], bounds=BoundingBox.from_str(item['bounds']))
            for item in page[0]
        ]
        hyperlinks = [
            HyperLink(
                goal=item['href'], bounds=BoundingBox.from_str(item['bounds']))
            for item in page[1]
        ]
        result.append([
            pagelinks,
            hyperlinks,
        ])
    return result
