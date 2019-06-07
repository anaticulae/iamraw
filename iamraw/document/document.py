# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import warnings
from dataclasses import dataclass
from dataclasses import field
from typing import List

from iamraw.document.page import Page
from iamraw.document.utils import BoundingBox


@dataclass
class Document:
    """A document describe a parsed PDF file. It is possbile to iterate over
    the different pages to inspect the parsed children.
    """
    dimension: BoundingBox = None
    pages: List[Page] = field(default_factory=list)

    @property
    def page_count(self):
        """Return pagecount of this document"""
        warnings.warn("use __len__", DeprecationWarning)
        return len(self.pages)

    @property
    def text(self):
        """Return the raw text of the document separated by pages"""
        texts = []
        for page in self.pages:  # pylint: disable=not-an-iterable
            texts.append(page.text)
        return ''.join(texts)

    def __len__(self):
        """Return pagecount of document"""
        return len(self.pages)

    def __repr__(self):
        result = 'Document: pages[%d]\n' % len(self.pages)
        for page in self.pages:  # pylint: disable=not-an-iterable
            result += str(page) + '\n'
        return result

    def __getitem__(self, key):
        """Iterate over pages"""
        return self.pages[key]  # pylint: disable=unsubscriptable-object
