# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================
import iamraw
import serializeraw.border
import serializeraw.document
import serializeraw.fontstore
import serializeraw.headerfooter
import serializeraw.textposition
import texmex


def create_pagetextnavigators_frompath(
        path: str,
        prefix='',
        pages=None,
        mode=texmex.PageTextNavigatorMode.BOTH,
        *,
        fill_empty: bool = True,
        logging: bool = True,
) -> texmex.PageTextNavigators:
    """Load all resources from one `path` to create PageTextNavigator
    for the selected list of `pages` with an optional `prefix` in loaded
    items.

    Args:
        path(str): Path to folder which contains all data to construct.
        prefix(str): Optional prefix to difference items in folder.
        pages(tuple): Tuple of pages to load.
        mode(PageTextNavigatorMode): select text container to skip
        fill_empty(bool): insert empty pages for pages without any saved
                          data. Use `fill_empty=False` to avoid filling
                          navgiators between pages=(0, 1, 4, 5).
        logging(bool): log errors while creating fontstore
    Returns:
        A list of selected PageTextNavigators.

    Example:
        rawmaker__oneline_text_text.yaml with `oneline` as prefix to
        separate instances.
    """
    text = iamraw.path.text(path, prefix=prefix)
    text = serializeraw.document.load_document(text, pages=pages)

    textposition = iamraw.path.textposition(path, prefix=prefix)
    textposition = serializeraw.textposition.load_textpositions(
        textposition,
        pages=pages,
    )
    fontstore = serializeraw.fontstore.create_fontstore_frompath(
        path,
        prefix=prefix,
        pages=pages,
        logging=logging,
    )
    navigators = texmex.create_pagetextnavigators(
        text,
        textposition,
        fontstore,
        fill_empty=fill_empty,
        mode=mode,
    )
    return navigators


def create_pagetextcontentnavigators_frompath(
        path: str,
        prefix: str = '',
        pages: tuple = None,
        mode=texmex.PageTextNavigatorMode.BOTH,
        *,
        validate_leftright: bool = True,
) -> texmex.PageTextContentNavigators:
    """Load `PageTextContentNavigators` from `path`.

    Args:
        path(str): `path` where loaded data is located in
        prefix(str): prefix loaded resources
        pages(tuple): selected pages
        mode(PageTextNavigatorMode): select text container to skip
        validate_leftright(bool): do not check writing over ``content border``.
    Returns:
        List of loaded PageTextContentNavigators depending on `pages`.
    """
    navigators = create_pagetextnavigators_frompath(
        path=path,
        prefix=prefix,
        pages=pages,
        mode=mode,
    )

    # TODO: ENABLE LATER
    # headerfooterpath = hey.path.headerfooters(path, prefix=prefix)
    headerfooterpath = iamraw.path.headerfooters(path)
    headerfooter = serializeraw.headerfooter.load_headerfooter(
        headerfooterpath,
        pages=pages,
    )

    # TODO: ENABLE LATER
    # sizeandborderpath = hey.path.sizeandborder(path, prefix=prefix)
    sizeandborderpath = iamraw.path.sizeandborder(path)
    sizeandborder = serializeraw.border.load_pageborders(
        sizeandborderpath,
        pages=pages,
    )

    result = texmex.create_pagetextcontentnavigators(
        headerfooter=headerfooter,
        navigators=navigators,
        pages=pages,
        sizeandborder=sizeandborder,
        validate_leftright=validate_leftright,
    )
    return result
