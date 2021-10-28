# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import collections
import concurrent.futures
import contextlib
import os

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
    loaded = utila.yaml_load(path, safe=False)
    assert isinstance(loaded, list), type(loaded)
    assert all(isinstance(item, iamraw.Finding) for item in loaded), str(loaded)
    loaded = select_pages(loaded, pages)
    result = iamraw.select_findings(loaded, msgids)
    return result


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
        assert istemplate_replaced(item.solution.description), message
        assert isinstance(item.number, int) or item.number is None
    dumped = yaml.dump(findings)
    return dumped


def write_grouped(
    findings: iamraw.Findings,
    dest: str,
    overwrite: bool = True,
    private: bool = False,
) -> list:
    result = []
    grouped = bypage(findings)
    writer = utila.file_replace if overwrite else utila.file_create
    for item in grouped:
        page = fname(item.page)
        outpath = os.path.join(dest, page)
        dumped = dump_findings(item.content)
        writer(outpath, dumped, private=private)
        result.append(outpath)
    return result


def load_grouped(
    source: str,
    pages: tuple = None,
    sort: bool = True,
    worker=10,
) -> iamraw.PageFindings:
    if pages is None:
        # load all findings
        pages = [
            pagenumber(item, none=True) for item in utila.file_list(source)
        ]
        # remove invalid file names
        pages = utila.not_none(pages)
    # yaml parsing is cpu bound, therefore we need a process pool instead
    # of thread pool.
    executor = utila.select_executor()
    result = []
    with executor(max_workers=worker) as executor:
        todo = {
            executor.submit(load_fast_findings, source, page): page
            for page in pages
        }
        for job in concurrent.futures.as_completed(todo):
            data = job.result()
            if not data:
                continue
            result.append(data)
    if sort:
        result.sort(key=lambda x: x.page)
    return result


def bypage(items: iamraw.Findings) -> iamraw.PageFindings:
    """Group `items` by location.page of `Finding`. Sort the groups
    ascending by page number."""
    pages = collections.defaultdict(list)
    for item in items:
        assert item.location is not None, f'require location {item.location}'
        pages[item.location.page].append(item)

    result = [
        iamraw.PageFinding(page=page, content=pages[page])
        for page in sorted(pages.keys())
    ]
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


def load_fast_findings(source: str, page: int) -> iamraw.PageFinding:
    name = fname(page)
    source = os.path.join(source, name)
    if not os.path.exists(source):
        return None
    findings = load_findings(source)
    return iamraw.PageFinding(page=page, content=findings)


def findings_from_path(
    path: str,
    worker: int = 10,
    useronly: bool = True,
    msgid: set = None,
    pages: tuple = None,
) -> iamraw.PageFindings:
    """Load Findings from `path` directory and group them by page as
    `PageFindings`."""
    if not utila.iterable(path):
        path = (path,)
    assert all(os.path.isdir(item) for item in path)
    # load findings from multiple directories
    files = [
        utila.file_list(
            item,
            absolute=True,
            include='yaml',
            recursive=True,
        ) for item in path
    ]
    # resolve multiple directory tree
    files = utila.flatten(files)
    if useronly:
        files = [
            item for item in files if utila.file_name(item).endswith('_user')
        ]
    # limit worker by max file count
    worker = utila.mins(worker, len(files))
    # ensure to have at least one worker when collection now file
    worker = utila.maxs(1, worker)
    # yaml parsing is cpu bound, therefore we need a process pool instead
    # of thread pool.
    executor = utila.select_executor()
    with executor(max_workers=worker) as executor:
        todo = {
            executor.submit(load_findings, path, msgid, pages): path
            for path in files
        }
        findings = []
        for job in concurrent.futures.as_completed(todo):
            data = job.result()
            findings.extend(data)
    result = bypage(findings)
    return result


def fname(page: int) -> str:
    """\
    >>> fname(-5)
    '_05'
    >>> fname(1)
    '001'
    >>> fname(333)
    '333'
    """
    if page < 0:
        return '_' + f'{page*-1}'.zfill(2)
    return f'{page}'.zfill(3)


def pagenumber(page: str, none: bool = True) -> int:
    """\
    >>> pagenumber('010')
    10
    >>> pagenumber(fname(-10))
    -10
    """
    if page[0] == '_':
        page = '-' + page[1:]
    with contextlib.suppress(ValueError):
        return int(page)
    if none:
        # handle error case
        return None
    raise ValueError(f'could not convert to int: {page}')


NOT_REPLACED = utila.compiles(r"""
\{\{[\w\_]*\}\}
""")


def istemplate_replaced(text: str) -> bool:
    """Check if some pattern `{% %}` is not replaced.

    >>> istemplate_replaced('hello')
    True
    >>> istemplate_replaced('%}')
    False
    >>> istemplate_replaced('{{myname_is_helm}}')
    False
    >>> istemplate_replaced('<configo.holyvalue.data.HolyValue object at 0x00000260AEA64220>,')
    False
    """
    if not text:
        return True
    if '{%' in text:
        return False
    if '%}' in text:
        return False
    if NOT_REPLACED.search(text):
        return False
    if 'HolyValue object at' in text:
        return False
    return True
