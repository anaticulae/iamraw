# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os

import utila

import iamraw
import serializeraw
import texmex


def ptn_frompath(
    path: str,
    prefix='',
    pages: tuple = None,
    mode=texmex.PTNMode.BOTH,
    *,
    backup: bool = False,
    fill_empty: bool = True,
    logging: bool = True,
    sort: bool = True,
) -> texmex.PTNs:
    """Load all resources from one `path` to create PTN
    for the selected list of `pages` with an optional `prefix` in loaded
    items.

    Args:
        path(str): Path to folder which contains all data to construct.
        prefix(str): Optional prefix to differentiate items in folder.
        pages(tuple): Tuple of pages to load.
        mode(PTNMode): select text container to skip
        backup(bool): If True use baml instead of yaml as ftype
        fill_empty(bool): insert empty pages for pages without any saved
                          data. Use `fill_empty=False` to avoid filling
                          navigators between pages=(0, 1, 4, 5).
        logging(bool): log errors while creating fontstore
        sort(bool): if False, do not check insert bounding position
    Returns:
        A list of selected PTNs.

    Example:
        rawmaker__oneline_text_text.yaml with `oneline` as prefix to
        separate instances.
    """
    # convert page to tuple, if required
    pages = utila.ensure_tuple(pages)
    # prepare path
    text, textpositions, fontheader, fontcontent = ptn_path(
        path,
        prefix,
        logging=logging,
        backup=backup,
    )
    # load data
    navigators = ptn_fromfile(
        text=text,
        textpositions=textpositions,
        fontheader=fontheader,
        fontcontent=fontcontent,
        fill_empty=fill_empty,
        mode=mode,
        sort=sort,
        pages=pages,
    )
    return navigators


def ptn_fromfile(
    text: str,
    textpositions: str,
    fontheader: str = None,
    fontcontent: str = None,
    pages: tuple = None,
    mode=texmex.PTNMode.BOTH,
    *,
    fill_empty: bool = True,
    sort: bool = True,
) -> texmex.PTNs:
    # convert page to tuple, if required
    pages = utila.ensure_tuple(pages)
    text = serializeraw.load_document(text, pages=pages)
    textpositions = serializeraw.load_textpositions(textpositions, pages=pages)
    fontstore = None
    if fontheader and fontcontent:
        fontstore = serializeraw.create_fontstore(
            fontheader,
            fontcontent,
        )
    navigators = texmex.create_pagetextnavigators(
        text,
        textpositions,
        fontstore,
        fill_empty=fill_empty,
        mode=mode,
        sort=sort,
    )
    return navigators


def ptn_path(
    path: str,
    prefix: str = '',
    *,
    logging: bool = False,
    backup: bool = False,
):
    ftype = 'baml' if backup else 'yaml'
    text = iamraw.path.text(path, prefix=prefix, ftype=ftype)
    textpositions = iamraw.path.textposition(path, prefix=prefix, ftype=ftype)
    fontheader = iamraw.path.fontheader(path, prefix=prefix, ftype=ftype)
    fontcontent = iamraw.path.fontcontent(path, prefix=prefix, ftype=ftype)
    if not utila.exists(fontheader):
        if logging:
            utila.debug(f'fontstore: {fontheader} does not exists')
        fontheader = None
    if not utila.exists(fontcontent):
        if logging:
            utila.debug(f'fontstore: {fontcontent} does not exists')
        fontcontent = None
    return text, textpositions, fontheader, fontcontent


def ptcn_frompath(
    path: str,
    prefix: str = '',
    pages: tuple = None,
    mode=texmex.PTNMode.BOTH,
    *,
    backup: bool = False,
    validate_leftright: bool = True,
    footer_sized_prefixed: bool = False,
    horizontals: bool = False,
) -> texmex.PTCNs:
    """Load `PTCNs` from `path`.

    Args:
        path(str): `path` where loaded data is located in
        prefix(str): prefix loaded resources
        pages(tuple): selected pages
        mode(PTNMode): select text container to skip
        backup(bool): If True use baml instead of yaml as ftype
        validate_leftright(bool): do not check writing over ``content border``.
        footer_sized_prefixed(bool): if True use prefixed data
                                     if False use default data
        horizontals(bool): insert horizontals if given
    Returns:
        List of loaded PTCNs depending on `pages`.
    """
    # convert page to tuple, if required
    pages = utila.ensure_tuple(pages)
    # prepare path
    text, textpositions, fontheader, fontcontent = ptn_path(
        path,
        prefix,
        backup=backup,
    )
    # do not generate general data twice
    prefix = prefix if footer_sized_prefixed else ''
    # determine paths
    headerfooterpath = iamraw.path.headerfooters(path, prefix=prefix)
    sizeandborderpath = iamraw.path.sizeandborder(path, prefix=prefix)
    if horizontals:
        horizontals = iamraw.path.horizontals(path, prefix=prefix)
        if not os.path.exists(horizontals):
            horizontals = None
    else:
        horizontals = None
    # create
    result = ptcn_fromfile(
        text=text,
        textpositions=textpositions,
        sizeandborderpath=sizeandborderpath,
        headerfooterpath=headerfooterpath,
        fontheader=fontheader,
        fontcontent=fontcontent,
        horizontals=horizontals,
        pages=pages,
        mode=mode,
        validate_leftright=validate_leftright,
    )
    return result


def ptcn_fromfile(
    text: str,
    textpositions: str,
    sizeandborderpath: str,
    headerfooterpath: str,
    fontheader: str = None,
    fontcontent: str = None,
    horizontals: str = None,
    pages: tuple = None,
    mode=texmex.PTNMode.BOTH,
    *,
    fill_empty: bool = True,
    validate_leftright: bool = True,
):
    # convert page to tuple, if required
    pages = utila.ensure_tuple(pages)
    navigators = ptn_fromfile(
        text,
        textpositions,
        fontheader,
        fontcontent,
        pages=pages,
        mode=mode,
        fill_empty=fill_empty,
    )
    # load header, footer, pageborder
    headerfooter = serializeraw.load_headerfooter(
        headerfooterpath,
        pages=pages,
    )
    sizeandborder = serializeraw.load_pageborders(
        sizeandborderpath,
        pages=pages,
    )
    if horizontals:
        horizontals = serializeraw.load_horizontals(
            horizontals,
            pages=pages,
        )
    # prepare result
    result = texmex.create_pagetextcontentnavigators(
        headerfooter=headerfooter,
        navigators=navigators,
        pages=pages,
        sizeandborder=sizeandborder,
        validate_leftright=validate_leftright,
        horizontals=horizontals,
    )
    return result
