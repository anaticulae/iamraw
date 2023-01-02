# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

# import rawmaker.features.fonts

import utila

import iamraw
import serializeraw
import serializeraw.fonts
import texmex


def dump_ptn(
    ptns: texmex.PTNs,
    fontstore: iamraw.FontStore,
) -> tuple:
    document = iamraw.Document(dimension=ptns[0].pagesize)
    textpositions = []
    for page in ptns:
        children, posis = create_page(page, fontstore)
        content = iamraw.Page(
            children=children,
            page=page.page,
            dimension=page.pagesize,
        )
        positions = iamraw.PageContentTextPosition(
            page=page.page,
            content=posis,
        )
        document.append(content)
        textpositions.append(positions)
    # write document
    dumped_document = serializeraw.dump_document(document)
    dumped_textpositions = serializeraw.dump_textpositions(textpositions)
    # fontstore, fontcontent = rawmaker.features.fonts.parse_fonts(document)
    # dumped_header = serializeraw.dump_font_header(fontstore)
    # dumped_content = serializeraw.dump_font_content(fontcontent)
    # return dumped_document, dumped_textpositions, dumped_header, dumped_content
    return dumped_document, dumped_textpositions


def create_page(page, fontstore: iamraw.FontStore) -> iamraw.Page:
    if not page:
        return [], {}
    lines, positions = [], []
    for item in page:
        line = create_line(item, fontstore)
        lines.append((item.line, line))
        position = iamraw.TextPosition(
            bounding=item.bounding,
            mean=item.bounding_mean,
        )
        positions.append(position)
    container, positions = merge_neighbors(lines, positions)
    positions = dict(enumerate(positions))
    return container, positions


def merge_neighbors(lines, positions):
    container, current = [lines[0][1]], lines[0][0]
    textpositions = [positions[0]]
    for ((number, line), texpos) in zip(lines[1:], positions[1:]):
        if (number - current) == 1:
            # merge
            before = container[-1]
            # add content
            before.lines.extend(line.lines)
            # update rectangle
            before.box = utila.rect_max((before.box, line.box))
            # merge textpositions
            textpositions[-1] = iamraw.TextPosition(
                bounding=tuple(before.box),
                mean=textpositions[-1].mean,
            )
            # update last line id to merge further items
            current = number
        else:
            # add new one
            container.append(line)
            textpositions.append(texpos)
            # reset merger
            current = 0
    return container, textpositions


def create_line(item, fontstore: iamraw.FontStore) -> iamraw.Line:
    rotation = item.style.rotation
    if rotation:
        line = iamraw.VerticalTextContainer(box=item.bounding)
    else:
        line = iamraw.TextContainer(box=item.bounding)
    style = item.style.content
    sizes = utila.flat([item.width * [item.size] for item in style])
    rises = utila.flat([item.width * [item.rise] for item in style])
    underlines = utila.flat([(item.width) * [item.underline] for item in style])
    fonts = utila.flat([
        (item.width) * [fontstore[item.font].pdfref] for item in style
    ])
    flags = utila.flat([
        item.width * [serializeraw.fonts.toflag(fontstore[item.font].flags)]
        for item in style
    ])
    chars = [
        iamraw.Char(
            value=value,
            size=size,
            rise=rise,
            font=font,
            flags=flag,
            underline=underline,
        ) for value, size, rise, font, flag, underline in zip(
            item.text,
            sizes,
            rises,
            fonts,
            flags,
            underlines,
        )
    ]
    line.append(iamraw.Line(chars=chars, box=item.bounding))
    return line
