# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import collections
import dataclasses
import enum

import iamraw.bounding


class Link(enum.Enum):
    UNDEFINED = -1
    INTERNAL = 0
    HYPERLINK = 1


@dataclasses.dataclass
class Annotation:
    goal: str
    bounds: iamraw.bounding.BoundingBox
    typ: Link = Link.UNDEFINED


@dataclasses.dataclass
class HyperLink(Annotation):
    typ: Link = Link.HYPERLINK


@dataclasses.dataclass
class PageLink(Annotation):
    typ: Link = Link.INTERNAL


PageAnnotation = collections.namedtuple(
    'PageAnnotation',
    'pagelinks hyperlinks page',
)
PageAnnotations = list[PageAnnotation]


def pagelink_annotations(annos: PageAnnotations) -> list[PageLink]:
    return [item.pagelinks for item in annos]


def hyperlink_annotations(annos: PageAnnotations) -> list[HyperLink]:
    return [item.hyperlinks for item in annos]
