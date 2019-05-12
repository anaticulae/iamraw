# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

from dataclasses import dataclass
from dataclasses import field
from typing import List

from iamraw.document.page import Page
from iamraw.document.utils import BoundingBox


@dataclass
class Document:
    dimension: BoundingBox = None
    pages: List[Page] = field(default_factory=list)

    @property
    def page_count(self):
        """Return pagecount of this document"""
        return len(self.pages)

    @property
    def text(self):
        texts = []
        for page in self.pages:
            texts.append(page.text)
        return ''.join(texts)

    def __repr__(self):
        result = 'Document: pages[%d]\n' % len(self.pages)
        for page in self.pages:
            result += str(page) + '\n'
        return result
