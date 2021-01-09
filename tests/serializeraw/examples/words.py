# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import iamraw
from iamraw import Headline

# TODO: search and refactor strings with automic tool
# ignore lines to long
# pylint:disable=C0301
EXAMPLE = [
    iamraw.PageContentText(
        6,
        [
            (Headline(
                title='CHAPTER 1', level=1, raw_level=None, page=6,
                container=0), []),
            (Headline(
                title='RestructuredText Tutorial',
                level=2,
                raw_level=None,
                page=6,
                container=1), []),
        ],
    ),
    iamraw.PageContentText(
        8,
        [
            (Headline(
                title='CHAPTER 2', level=1, raw_level=None, page=8,
                container=0), []),
            (Headline(
                title='RestructuredText Guide',
                level=2,
                raw_level=None,
                page=8,
                container=1), []),
            (Headline(
                title='Basics', level=3, raw_level=None, page=8, container=2
            ), [
                'Improving upon the pattern established at http://markdown-guide.readthedocs.org/en/latest/basics.html, sections to add:',
                '0l', '0l', '0l', '0l', '0l', '0l', '0l', '0l', '0l', '0l',
                '0l', '0l', '0l', '0l', '0l'
            ]),
        ],
    ),
    iamraw.PageContentText(
        9,
        [
            (Headline(
                title='Blockquotes',
                level=3,
                raw_level=None,
                page=9,
                container=1,
            ), [
                'To enclose a segment of text in blockquotes, one must add a tab at the start of a paragraph.',
                'RestructuredText:', '1b', '1b', '1b', '1b', 'Output:', '0b'
            ]),
            (Headline(
                title='Code: Block',
                level=3,
                raw_level=None,
                page=9,
                container=10), ['TODO']),
        ],
    ),
    iamraw.PageContentText(
        10,
        [
            (Headline(
                title='CHAPTER 3',
                level=1,
                raw_level=None,
                page=10,
                container=0), []),
            (Headline(
                title='RestructuredText Customizations',
                level=2,
                raw_level=None,
                page=10,
                container=1), ['Sphinx:']),
        ],
    ),
    iamraw.PageContentText(
        12,
        [
            (Headline(
                title='CHAPTER 4',
                level=1,
                raw_level=None,
                page=12,
                container=0), []),
            (Headline(
                title='Sphinx Tutorial',
                level=2,
                raw_level=None,
                page=12,
                container=1), []),
            (Headline(
                title='Step 1', level=3, raw_level=None, page=12, container=2),
             []),
            (Headline(
                title='Getting Set Up',
                level=3,
                raw_level=None,
                page=12,
                container=3
            ), [
                'Philosophy',
                'Sphinx is what is called a documentation generator.',
                'This means that it takes a bunch of source files in plain text, and generates a bunch of other awesome things, mainly HTML.',
                'For our use case you can think of it as a program that takes in plain text files in reStructuredText format, and outputs HTML.',
                '0b',
                'So as a user of Sphinx, your main job will be writing these text files.',
                'This means that you should be minimally familiar with reStructuredText as a language.',
                'Its similar to Markdown in a lot of ways, if you are already familiar with Markdown.',
                'Installing Sphinx', 'The first step is installing Sphinx.',
                'Sphinx is a python project, so it can be installed like any other python library.',
                'Every Operating System should have Python pre-installed, so you should just have to run:',
                '1b', 'Note:',
                'Advanced users can install this in a virtualenv if they wish.',
                'Also, pip install Sphinx works fine if you have Pip.'
            ]),
        ],
    ),
    iamraw.PageContentText(
        13,
        [
            (Headline(
                title=None, level=None, raw_level=None, page=13, container=0
            ), [
                'Getting Started',
                'Now you are ready to creating documentation.',
                'Create a directory called crawler.',
                'Inside that directory you should create a docs directory, and move into it:',
                '4b',
                'Then you can create the Sphinx project skeleton in this directory:',
                '0b',
                'accepting all the defaults, calling the project Crawler, and giving it a 1.0 version.',
                'Your file system should now look similar to this:', '1b', '1b',
                '1b',
                'We have a top-level docs directory in the main project directory.',
                'Inside of this is:', 'index.rst:',
                'This is the index file for the documentation, or what lives at /. It normally contains a Table of Contents',
                'that will link to all other pages of the documentation.',
                'conf.py:', 'which allows for customization of Sphinx.',
                'You wont need to use this too much yet, but its good to be',
                'familiar with this file.', 'Makefile:',
                'This ships with Sphinx, and is the main interface for local development, and shouldnt be changed.',
                '_build:', 'The directory that your output files go into.',
                '_static:',
                'The directory to include all your static files, like images.',
                '_templates:',
                'Allows you to override Sphinx templates to customze look and feel.',
                'Building docs',
                'Lets build our docs into HTML to see how it works.',
                'Simply run:', '2b',
                'This should run Sphinx in your shell, and output HTML.',
                'At the end, it should say something about the documents being ready in _build/html.',
                'You can now open them in your browser by typing:', '3b',
                'This should display a rendered HTML page that says Welcome to Crawlers documentation! at the top.',
                'make html is the main way you will build HTML documentation locally.',
                'It is simply a wrapper around a more complex call to Sphinx.'
            ]),
        ],
    ),
    iamraw.PageContentText(
        14,
        [
            (Headline(
                title='Documenting a Project',
                level=3,
                raw_level=None,
                page=14,
                container=1
            ), [
                'Now that we have our basic skeleton, lets document the project.',
                'As you might have guessed from the name, well be documenting a basic web crawler.',
                'For this project, well have the following pages:', '1l', '1l',
                '1l', '1l', '1l', '1l', 'Lets start with the Support page.',
                'Support docs',
                'Its always important that users can ask questions when they get stuck.',
                'There are many ways to handle this, but normal approaches are to have an IRC channel and mailing list.',
                'Go ahead and put this markup in your support.rst:', '0b', '0b',
                '0b', '0b', '0b', 'Hyperlink Syntax',
                'The main new markup here is the link syntax.',
                'The link text is set by putting a _ after some text.',
                'The ` is used to group text, allowing you to include multiple words in your link text.',
                'You should use the `, even when the link text is only one word.',
                'This keeps the syntax consistent.',
                'The link target is defined at the bottom of the section with .. _<link text>: <target>.',
                'Installation docs',
                'Installation documentation is really important.',
                'Anyone who is coming to the project will need to install it.',
                'For our example, we are installing a basic Python script, so it will be pretty easy.',
                'Include the following in your install.rst:'
            ]),
        ],
    ),
    iamraw.PageContentText(
        15,
        [(
            Headline(
                title=None, level=None, raw_level=None, page=15, container=0),
            [
                '2b',
                '2b',
                '2b',
                '2b',
                '2b',
                '2b',
                'Code Example Syntax',
                'This snippet introduces a couple of simple concepts.',
                'The syntax for displaying code is ::. When it is used at the end of a sentence, Sphinx is smart and displays one : in the output, and knows there is a code example in the following indented block.',
                'Sphinx, like Python, uses meaningful whitespace.',
                'Blocks of content are structured based on the indention level they are on.',
                'You can see this concept with our code-block directive above.',
                'Table of Contents Tree (toctree)',
                'Now would be a good time to introduce the toctree.',
                'One of the main concepts in Sphinx is that it allows multiple pages to be combined into a cohesive hierarchy.',
                'The toctree directive is a fundamental part of this structure.',
                'A simple toctree directive looks like this:',
                '0b',
                '0b',
                '0b',
                'This will then output a Table of Contents in the page where this occurs.',
                'It will output the top-level headers of the pages as listed.',
                'This also tells Sphinx that the other pages are sub-pages of the current page.',
                'You should go ahead and include the above toctree directive in your index.rst file.',
                'Build Docs Again',
                'Now that you have a few pages of content, go ahead and build your docs again:',
                '1b',
                'If you open up your index.html, you should see the basic structure of your docs from the included toctree directive.',
            ],
        ),
         (Headline(
             title='Aside: Other formats',
             level=3,
             raw_level=None,
             page=15,
             container=21), [])],
    ),
    iamraw.PageContentText(
        16,
        [
            (Headline(
                title=None, level=None, raw_level=None, page=16, container=0
            ), [
                'Make a manpage',
                'The beauty of Sphinx is that it can output in multiple formats, not just HTML.',
                'All of those formats share the same base format though, so you only have to change things in one place.',
                'So you can generate a manpage for your docs:', '4b',
                'This will place a manpage in _build/man.',
                'You can then view it with:', '0b',
                'Create a single page document',
                'Some people prefer one large HTML document, instead of having to look through multiple pages.',
                'This is another area where Sphinx shines.',
                'You can write your documentation in multiple files to make editing and updating easier.',
                'Then if you want to distribute a single page HTML version:',
                '1b',
                'This will combine all of your HTML pages into a single page.',
                'Check it out by opening it in your browser:', '2b',
                'Youll notice that it included the documents in the order that your TOC Tree was defined.'
            ]),
            (Headline(
                title='Step 2', level=3, raw_level=None, page=16, container=12),
             []),
            (Headline(
                title='Referencing Code',
                level=3,
                raw_level=None,
                page=16,
                container=13
            ), [
                'Lets go ahead and add a cookbook to our documentation.',
                'Users will often come to your project to solve the same problems.',
                'Including a Cookbook or Examples section will be a great resource for this content.',
                'In your cookbook.rst, add the following:', '3b', '3b', '3b',
                '3b', '3b', '3b', '3b'
            ]),
        ],
    ),
    iamraw.PageContentText(
        17,
        [
            (Headline(
                title=None, level=None, raw_level=None, page=17, container=0),
             ['0b', '0b', '0b', '0b', '0b', '0b', '0b', '0b', '0b', '0b']),
        ],
    ),
    iamraw.PageContentText(
        18,
        [
            (Headline(
                title='CHAPTER 5',
                level=1,
                raw_level=None,
                page=18,
                container=0), []),
            (Headline(
                title='Sphinx Guide',
                level=2,
                raw_level=None,
                page=18,
                container=1), []),
        ],
    ),
    iamraw.PageContentText(
        20,
        [
            (Headline(
                title='CHAPTER 6',
                level=1,
                raw_level=None,
                page=20,
                container=0), []),
            (Headline(
                title='Sphinx Customizations',
                level=2,
                raw_level=None,
                page=20,
                container=1), ['Utilities:']),
        ],
    ),
    iamraw.PageContentText(
        22,
        [
            (Headline(
                title='CHAPTER 7',
                level=1,
                raw_level=None,
                page=22,
                container=0), []),
            (Headline(
                title='Testing your Documentation',
                level=2,
                raw_level=None,
                page=22,
                container=1
            ), [
                'If you want to confirm that your docs build successfully, you add this to your tox.ini file:',
                '0b', '0b', '0b', '0b', '0b', '0b', '0b', '0b', '0b', '0b',
                'TODO:', 'Explain in depth what this actually does.', 'TODO:',
                'Explain what tox is.'
            ]),
        ],
    ),
    iamraw.PageContentText(
        24,
        [
            (Headline(
                title='CHAPTER 8',
                level=1,
                raw_level=None,
                page=24,
                container=0), []),
            (Headline(
                title='Indices and tables',
                level=2,
                raw_level=None,
                page=24,
                container=1), ['2l', '2l', '2l']),
        ],
    ),
]

HEADLINES = [
    [
        Headline(
            title='CHAPTER 1', level=1, raw_level=None, page=6, container=0),
        Headline(
            title='RestructuredText Tutorial',
            level=2,
            raw_level=None,
            page=6,
            container=1)
    ],
    [
        Headline(
            title='CHAPTER 2', level=1, raw_level=None, page=8, container=0),
        Headline(
            title='RestructuredText Guide',
            level=2,
            raw_level=None,
            page=8,
            container=1),
        Headline(title='Basics', level=3, raw_level=None, page=8, container=2)
    ],
    [
        Headline(
            title='Blockquotes', level=3, raw_level=None, page=9, container=1),
        Headline(
            title='Code: Block', level=3, raw_level=None, page=9, container=10)
    ],
    [
        Headline(
            title='CHAPTER 3', level=1, raw_level=None, page=10, container=0),
        Headline(
            title='RestructuredText Customizations',
            level=2,
            raw_level=None,
            page=10,
            container=1)
    ],
    [
        Headline(
            title='CHAPTER 4', level=1, raw_level=None, page=12, container=0),
        Headline(
            title='Sphinx Tutorial',
            level=2,
            raw_level=None,
            page=12,
            container=1),
        Headline(title='Step 1', level=3, raw_level=None, page=12, container=2),
        Headline(
            title='Getting Set Up',
            level=3,
            raw_level=None,
            page=12,
            container=3)
    ],
    [
        Headline(
            title='Documenting a Project',
            level=3,
            raw_level=None,
            page=14,
            container=1)
    ],
    [
        Headline(
            title='Aside: Other formats',
            level=3,
            raw_level=None,
            page=15,
            container=21)
    ],
    [
        Headline(
            title='Step 2', level=3, raw_level=None, page=16, container=12),
        Headline(
            title='Referencing Code',
            level=3,
            raw_level=None,
            page=16,
            container=13)
    ],
    [
        Headline(
            title='CHAPTER 5', level=1, raw_level=None, page=18, container=0),
        Headline(
            title='Sphinx Guide', level=2, raw_level=None, page=18, container=1)
    ],
    [
        Headline(
            title='CHAPTER 6', level=1, raw_level=None, page=20, container=0),
        Headline(
            title='Sphinx Customizations',
            level=2,
            raw_level=None,
            page=20,
            container=1)
    ],
    [
        Headline(
            title='CHAPTER 7', level=1, raw_level=None, page=22, container=0),
        Headline(
            title='Testing your Documentation',
            level=2,
            raw_level=None,
            page=22,
            container=1)
    ],
    [
        Headline(
            title='CHAPTER 8', level=1, raw_level=None, page=24, container=0),
        Headline(
            title='Indices and tables',
            level=2,
            raw_level=None,
            page=24,
            container=1)
    ],
]
