# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import dataclasses

import utila
import yaml

import iamraw


def dump_bibliography_reference(references: iamraw.BibliographyReferences) -> str: # yapf:disable
    result = []
    for page in references:
        result.append([dataclasses.asdict(item) for item in page])
    dumped = yaml.safe_dump(result)
    return dumped


def load_bibliography_reference(content: str) -> iamraw.BibliographyReferences:
    loaded = utila.yaml_from_raw_or_path(content, safe=True)
    result = []
    for page in loaded:
        result.append([iamraw.BibliographyReference(**item) for item in page])
    for page in result:
        for item in page:
            # TODO: IS TUPLE SO IMPORTANT HERE?
            item.authors = [tuple(item) for item in item.authors]
    return result
