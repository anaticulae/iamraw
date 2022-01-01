# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import dataclasses
import functools
import typing

import utila

import iamraw

NO_FONT = -1


@dataclasses.dataclass
class FontChunk:
    content: str
    font: iamraw.Font = None


FontChunks = typing.List[FontChunk]


@dataclasses.dataclass
class FontStore:

    header: dict = dataclasses.field(default_factory=dict)
    pages: dict = dataclasses.field(default_factory=dict)

    def __init__(self, header, pages):
        if not header:
            utila.error('empty font header')
        if not pages:
            utila.error('empty font footer/pages')
        self.header = {hash(item): item for item in header}
        self.pages = {page.page: page.content for page in pages}

    def font(
        self,
        number: int,
        container: int,
        line: int,
        char: int,
    ) -> int:
        fontid = self.fontid(number, container, line, char)
        return self[fontid]

    def fontid(
        self,
        number: int,
        container: int,
        line: int,
        char: int,
    ) -> int:
        # TODO: linear complexity!
        page = self.pages[number]
        for item in page:
            cur_container, cur_line, cur_char, cur_font = item
            if cur_container > container:
                return cur_font
            if cur_container == container:
                if cur_line > line:
                    return cur_font
                if cur_line == line:
                    if char >= cur_char:
                        continue
                    return cur_font
                continue
            continue
        return NO_FONT

    @functools.lru_cache()
    def font_to_fontid(self, font: iamraw.Font) -> int:
        hashed = hash(font)
        try:
            _ = self[hashed]
            return hashed
        except KeyError:
            return NO_FONT

    def fromstr(
        self,
        page: int,
        container: int,
        line: int,
        text: str,
    ) -> FontChunks:
        assert isinstance(text, str), type(text)
        result = []
        current = self.font(page, container, line, 0)
        collector = ''
        lines = text.splitlines()
        for linenumber, textline in enumerate(lines, start=line):
            for index, item in enumerate(textline, start=0):
                font = self.font(page, container, linenumber, index)
                if font != current:
                    result.append(FontChunk(content=collector, font=current))
                    collector = item
                    current = font
                else:
                    collector += item
            if linenumber + 1 < len(lines):
                # last item needs no newline
                collector += utila.NEWLINE
        # Final font
        if collector:
            result.append(FontChunk(content=collector, font=current))
        return result

    def page_iter(self, number):
        return iter(self.pages[number])

    def __len__(self) -> int:
        return len(self.pages)

    def __getitem__(self, index: int) -> iamraw.Font:
        try:
            return self.header[index]
        except KeyError:
            utila.error(f'could not find font: {index}')
            return None

    def __hash__(self):
        return hash(str(self))


class FontContentStore:

    def __init__(
        self,
        store: FontStore,
        navigator: 'PageTextContentNavigator',
        page: int,
    ):
        assert store, navigator
        # assert isinstance(navigator, PageTextContentNavigator)
        assert page == navigator.page, f'{page} {navigator.page}'
        self.store = store
        self.off_start = navigator.offset[0]
        self.off_end = navigator.offset[1]
        self.page = page

    def fontid(
        self,
        container: int,
        line: int,
        char: int,
    ) -> int:
        """Determine fontid based on location. The container index
        starts with zero. The containerid is relative to the start of
        content.

        Args:
            container(int): containerid relative to start of content.
                            The internal containerid is determined as
                            `content-start` + `container`.
            line(int): line in selected container
            char(int): char in goal line
        Returns:
            fontid - font number defined in font_header
        Raises:
            IndexError: if `container` is out of bounds
        """
        current_container = self.off_start + container
        if container >= len(self):
            # TODO: check the index
            raise IndexError(f'index {container} out of bounds')
        fontid = self.store.fontid(self.page, current_container, line, char)
        return fontid

    def fromstr(
        self,
        container: int,
        line: int,
        text: str,
    ) -> FontChunks:
        current_container = self.off_start + container
        result = self.store.fromstr(
            self.page,
            current_container,
            line,
            text,
        )
        return result

    def __len__(self):
        return self.off_end - 1

    def __getitem__(self, index: int) -> iamraw.Font:
        try:
            return self.store[index]
        except (KeyError, TypeError) as error:
            raise IndexError('Invalid font index: %r' % index) from error
