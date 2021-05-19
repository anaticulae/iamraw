# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import typing

import utila

import iamraw

Strs = typing.List[str]


class TextContainerIterator:

    def __init__(self, page):
        # TODO: We do not want to copy!
        self.page = [
            item for item in page if isinstance(item, iamraw.TextContainer)
        ]

    def __getitem__(self, index):
        return self.page[index]

    def __len__(self):
        return len(self.page)


class PageIter:

    def __init__(self, page):
        self.page = TextContainerIterator(page)
        self.container = 0
        self.line = 0
        self.char = 0

    def __str__(self):
        result = "Position[container=%d, line=%d, char=%d]"
        result = result % (self.container, self.line, self.char)
        return result

    def next_item(self, container, line, char) -> str:
        """Extract data between `current` iterator position
        `(self.container, self.line, self.char)` and the passed `new`
        iterator position `(container, line, char)`.

        Raises:
            ValueError: next step is on current iterator
            ValueError: content can be provided cause iter stands on end
        Returns:
            content between current text iterator and passed new iterator
            if the new iterator is out of bounds a ValueError is raised.
        """
        utila.debug(f'input {container} {line} {char}')
        utila.debug(f'current: {self.container} {self.line} {self.char}')
        empty = True
        result = ''
        if all([
                container == self.container,
                line == self.line,
                char == self.char,
        ]):
            raise ValueError('iter stands on goal %d %d' % (container, line))

        if self.char > 0 and char == 0:
            # text iterator is not on the line start
            if self.container < container or self.line < line:
                # fill the rest of the current line and goto next lien
                result += self.page[self.container][self.line].text[self.char:]
                self.char = 0
                self.line += 1
                empty = False
        if self.line > 0 and self.container < container:
            # Fill up the container before continuing with the next
            for item in self.page[self.container][self.line:]:
                result += item.text
                empty = False
            self.line = 0
            self.container += 1
        while self.container < container:
            result += self.page[self.container].text
            self.container += 1
            empty = False
        while self.line < line:
            result += self.page[self.container][self.line].text
            self.line += 1
            empty = False
        if char:
            result += self.page[self.container][self.line].text[self.char:char-1] # yapf:disable
            # Example: iterator stands on 10, next `char` is 15, we have to add
            # chardistance (15-10) to add. After this the current iterator
            # stands on 15.
            charsdistance = (char - self.char) - 1
            self.char += charsdistance
            empty = False
        if empty:
            msg = 'no content selected %d %d %d' % (container, line, char)
            raise ValueError(msg)
        return result

    def finish(self):
        # TODO Dirty hack!
        try:
            return self.next_item(len(self.page), 0, 0)
        except ValueError:
            return ''


def split_page(
    page: iamraw.Page,
    positions: typing.List,
    *,
    append_unvisited: bool = True,
) -> Strs:
    """Split page into chunks given by `positions`. The source of these
    positions can be rawmaker with font-extractor.

    Hint:
        Append unvisited is a little bit crazy - may remove later?

    Args:
        page(Page): page with text content(TextContainer)
        positions(List[(container, line, char)]): List with separation order

        append_unvisited(bool): if True, the content from current iter
                                to the rest of the page will be added.
    Returns:
        List of selected text chunks.
    """
    pageiter = PageIter(page=page)
    result = [pageiter.next_item(*item) for item in positions]
    if not append_unvisited:
        return result
    finish = pageiter.finish().strip()
    if finish:
        result.append(finish)
    return result
