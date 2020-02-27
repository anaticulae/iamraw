# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================
import iamraw
from serializeraw.border import load_pageborders
from serializeraw.document import load_document
from serializeraw.fontstore import create_fontstore_frompath
from serializeraw.headerfooter import load_headerfooter
from serializeraw.textposition import load_textpositions


def create_pagetextnavigators_frompath(
        path: str,
        prefix='',
        pages=None,
) -> iamraw.PageTextNavigators:
    """Load all resources from one `path` to create PageTextNavigator
    for the selected list of `pages` with an optional `prefix` in loaded
    items.

    Args:
        path(str): Path to folder which contains all data to construct.
        prefix(str): Optional prefix to difference items in folder.
        pages(tuple): Tuple of pages to load.
    Returns:
        A list of selected PageTextNavigators.

    Example:
        rawmaker__oneline_text_text.yaml with `oneline` as prefix to
        separate instances.
    """
    text = iamraw.path.text(path, prefix=prefix)
    text = load_document(text, pages=pages)

    textposition = iamraw.path.textposition(path, prefix=prefix)
    textposition = load_textpositions(textposition, pages=pages)
    fontstore = create_fontstore_frompath(
        path,
        prefix=prefix,
        pages=pages,
    )

    navigators = iamraw.create_pagetextnavigators(text, textposition, fontstore)
    return navigators


def create_pagetextcontentnavigators_frompath(
        path: str,
        prefix: str = '',
        pages: tuple = None,
        validate_leftright: bool = True,
) -> iamraw.PageTextContentNavigators:
    """Load `PageTextContentNavigators` from `path`.

    Args:
        path(str): `path` where loaded data is located in
        prefix(str): prefix loaded resources
        pages(tuple): selected pages
        validate_leftright(bool): do not check writing over ``content border``.
    Returns:
        List of loaded PageTextContentNavigators depending on `pages`.
    """
    navigators = create_pagetextnavigators_frompath(
        path=path,
        prefix=prefix,
        pages=pages,
    )

    # TODO: ENABLE LATER
    # headerfooterpath = hey.path.headerfooters(path, prefix=prefix)
    headerfooterpath = iamraw.path.headerfooters(path)
    headerfooter = load_headerfooter(
        headerfooterpath,
        pages=pages,
    )

    # TODO: ENABLE LATER
    # sizeandborderpath = hey.path.sizeandborder(path, prefix=prefix)
    sizeandborderpath = iamraw.path.sizeandborder(path)
    sizeandborder = load_pageborders(
        sizeandborderpath,
        pages=pages,
    )

    result = iamraw.create_pagetextcontentnavigators(
        navigators=navigators,
        headerfooter=headerfooter,
        sizeandborder=sizeandborder,
        validate_leftright=validate_leftright,
        pages=pages,
    )
    return result
