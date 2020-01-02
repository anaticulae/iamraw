# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================
from collections import namedtuple
from dataclasses import dataclass
from enum import Enum
from typing import List

from iamraw.document import BoundingBox


class Link(Enum):
    UNDEFINED = -1
    INTERNAL = 0
    HYPERLINK = 1


@dataclass
class Annotation:
    goal: str
    bounds: BoundingBox
    typ: Link = Link.UNDEFINED


@dataclass
class HyperLink(Annotation):
    typ: Link = Link.HYPERLINK


@dataclass
class PageLink(Annotation):
    typ: Link = Link.INTERNAL


PageAnnotation = namedtuple('PageAnnotation', 'pagelinks,hyperlinks,page')
PageAnnotations = List[PageAnnotation]


def pagelink_annotations(annotations: PageAnnotations) -> List[PageLink]:
    return [item.pagelinks for item in annotations]


def hyperlink_annotations(annotations: PageAnnotations) -> List[HyperLink]:
    return [item.hyperlinks for item in annotations]
