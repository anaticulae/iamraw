# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

# Unicode special minus sign

USER_CHARACTER = [
    "'",
    '!',
    '"',
    '&',
    ',',
    '/',
    ':',
    ';',
    '?',
    'ß',
    '–',  # special minus sign
    '‘',
    '’',
    '‚',
    '“',
    '”',
    '„',
    '…',
    r'\(',
    r'\)',
    r'\-',
    r'\.',
    r'\[',
    r'\]',
    r'\d',
    r'\w',
]

UC_NWS = ''.join(USER_CHARACTER)
UC = UC_NWS + ' '  # user content with whitespace
UC_WS_NL = UC + r'\s'  # content with whitespace, newline

UC_NWS = f'[{UC_NWS}]'
UC = f'[{UC}]'
UC_WS_NL = f'[{UC_WS_NL}]'
