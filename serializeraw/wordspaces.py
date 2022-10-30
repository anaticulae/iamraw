# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utila

import iamraw
import serializeraw


def dump_wordspaces(items) -> str:

    def dumper(lines) -> list:
        result = []
        for number, content in lines:
            content = utila.from_tuple(utila.flat(content))
            line = f'{number} {content}'
            result.append(line)
        return result

    dumped = serializeraw.dump_pagecontent(items, pagedumper=dumper)
    return dumped


def load_wordspaces(content: str, pages: tuple = None) -> iamraw.PageContents:

    def loader(page) -> iamraw.PageContent:
        result = []
        for line in page:
            number, content = line.split(maxsplit=1)
            # TODO: IMPROVE THIS METHOD
            content = content.split()
            content = [
                utila.parse_tuple(' '.join(chunk))
                for chunk in utila.chunks(content, size=4)
            ]
            result.append((int(number), content))
        return result

    loaded = serializeraw.load_pagecontent(
        content,
        pages=pages,
        pageloader=loader,
        fname='textflow__wordspace_wordspace',
    )
    return loaded
