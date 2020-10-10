# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utila
import yaml

import iamraw


def load_findings(
        path: str,
        msgids: set = None,
        pages: tuple = None,
) -> iamraw.Findings:
    """Load list of `Finding`s which was produced by linter

    Args:
        path(str): path to file with lists of `Finding`
        msgids(set): set of selected Findings; if msgids is None, select all
        pages(tuple): accepted pages
    Returns:
        list of Finding
    Raises:
        Assertion: if file is corrupt
    """
    loaded = utila.yaml_from_raw_or_path(path, safe=False)
    assert isinstance(loaded, list), type(loaded)
    assert all([isinstance(item, iamraw.Finding) for item in loaded]), str(loaded) # yapf:disable
    loaded = select_pages(loaded, pages)
    result = iamraw.select_findings(loaded, msgids)
    return result


def select_pages(findings, pages: tuple = None) -> list:
    if not pages:
        return findings
    selected = []
    for finding in findings:
        try:
            skip = utila.should_skip(finding.location.page, pages)
            if skip:
                continue
        except AttributeError:
            continue
        else:
            selected.append(finding)
    return selected


def dump_findings(findings: list) -> str:
    assert isinstance(findings, list), type(findings)
    for item in findings:
        if not item.solution:
            continue
        try:
            description = item.solution.description
        except AttributeError:
            continue
        message = f'template is not fully replaced:\n{description}'
        # ensure that the user could not see any not fully replaced templates
        assert utila.istemplate_replaced(item.solution.description), message
        assert isinstance(item.number, int) or item.number is None
    dumped = yaml.dump(findings)
    return dumped
