# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os

# path
import iamraw.path as path
# abbreviation
from iamraw.abbreviation import Abbreviation
from iamraw.abbreviation import AbbreviationList
from iamraw.abbreviation import AbbreviationListLookup
from iamraw.abbreviation import AbbreviationLists
from iamraw.abbreviation import AbbreviationPosition
from iamraw.abbreviation import AbbreviationResult
from iamraw.abbreviation import Abbreviations
from iamraw.abbreviation import ExtractedTextAbbreviation
from iamraw.abbreviation import ExtractedTextAbbreviations
# annotation
from iamraw.annotation import Annotation
from iamraw.annotation import HyperLink
from iamraw.annotation import Link
from iamraw.annotation import PageAnnotation
from iamraw.annotation import PageAnnotations
from iamraw.annotation import PageLink
from iamraw.annotation import hyperlink_annotations
from iamraw.annotation import pagelink_annotations
# bib
from iamraw.bibliography import BibliographyReference
from iamraw.bibliography import BibliographyReferences
# border
from iamraw.border import Border
from iamraw.border import Borders
# bounding
from iamraw.bounding import BoundingBox
from iamraw.bounding import BoundingBoxes
from iamraw.bounding import PageBoundings
from iamraw.bounding import PageBoundingsList
from iamraw.bounding import between
from iamraw.bounding import split_x
from iamraw.bounding import split_y
# boxes
from iamraw.boxes import Box
from iamraw.boxes import HorizontalLine
from iamraw.boxes import PageContentBoxes
from iamraw.boxes import PageContentHorizontals
from iamraw.boxes import PagesWithBoxList
from iamraw.boxes import PagesWithHorizontalList
# captions
from iamraw.caption import Caption
from iamraw.caption import Captions
from iamraw.caption import PageContentCaption
from iamraw.caption import PageContentCaptions
# code
from iamraw.code import PageContentCode
from iamraw.code import PageContentCodes
from iamraw.code import PeaceOfCode
from iamraw.code import PeaceOfCodes
# content
from iamraw.content import ContentBoundingBox
from iamraw.content import ContentBoundingBoxes
# distance
from iamraw.distance import AreaDistance
from iamraw.distance import AreaDistances
from iamraw.distance import PageContentAreaDistance
from iamraw.distance import PageContentAreaDistances
# docinfo
from iamraw.docinfo import DocInfo
from iamraw.docinfo import DocumentType
from iamraw.docinfo import Generator
from iamraw.docinfo import SectionLookup
# docref
from iamraw.docref import DocRef
from iamraw.docref import DocRefs
# document
from iamraw.document import Boxed
from iamraw.document import Char
from iamraw.document import Chars
from iamraw.document import Document
from iamraw.document import Line
from iamraw.document import Lines
from iamraw.document import Page
from iamraw.document import PageObject
from iamraw.document import Pages
from iamraw.document import PageSize
from iamraw.document import PageSizes
from iamraw.document import TextContainer
from iamraw.document import TextContainers
from iamraw.document import UnicodeChar
from iamraw.document import VerticalTextContainer
from iamraw.document import VerticalTextContainers
from iamraw.document import VirtualChar
# figures
from iamraw.figure import Figure
from iamraw.figure import Figures
# findings
from iamraw.findings import BoundingLocation
from iamraw.findings import Finding
from iamraw.findings import FindingLevel
from iamraw.findings import Findings
from iamraw.findings import Location
from iamraw.findings import PageFinding
from iamraw.findings import PageFindings
from iamraw.findings import RangedLocation
from iamraw.findings import select_findings
# fonts
from iamraw.fonts import DEFAULT_STRETCH
from iamraw.fonts import DEFAULT_STYLE
from iamraw.fonts import DEFAULT_WEIGHT
from iamraw.fonts import Font
from iamraw.fonts import FontFlag
from iamraw.fonts import FontFlags
from iamraw.fonts import PageFontContent
from iamraw.fonts import PageFontContents
from iamraw.fonts import Stretch
from iamraw.fonts import Style
from iamraw.fonts import Weight
from iamraw.fontstore import NO_FONT
from iamraw.fontstore import FontChunk
from iamraw.fontstore import FontChunks
from iamraw.fontstore import FontContentStore
from iamraw.fontstore import FontStore
# footnotes
from iamraw.footnotes import PageContentFootnote
from iamraw.footnotes import PageContentFootnotes
# formula
from iamraw.formula import Formula
from iamraw.formula import FormulaRaw
from iamraw.formula import Formulas
from iamraw.formula import FormulasRaw
from iamraw.formula import MathChar
from iamraw.formula import MathChars
from iamraw.formula import PageContentFormula
from iamraw.formula import PageContentFormulas
from iamraw.formula import PageContentRawFormula
from iamraw.formula import PageContentRawFormulas
# headerfooter
from iamraw.headerfooter import FixedFooterInformation
from iamraw.headerfooter import FixedHeaderInformation
from iamraw.headerfooter import FooterInformation
from iamraw.headerfooter import FootJudgedNote
from iamraw.headerfooter import FootNote
from iamraw.headerfooter import FootNoteMerged
from iamraw.headerfooter import FootNotes
from iamraw.headerfooter import FootRawNote
from iamraw.headerfooter import HeaderImages
from iamraw.headerfooter import HeaderInformation
from iamraw.headerfooter import HeaderTitle
from iamraw.headerfooter import MovingFooterInformation
from iamraw.headerfooter import PageContentFooterHeader
from iamraw.headerfooter import PageContentFooterHeaders
from iamraw.headerfooter import PageInformation
from iamraw.headerfooter import PagesFooterInformation
from iamraw.headerfooter import RawText
# headlines
from iamraw.headlines import Headline
from iamraw.headlines import Headlines
from iamraw.headlines import PagesHeadlineList
from iamraw.headlines import headlines_totoc
# hits
from iamraw.hits import PageContentHit
from iamraw.hits import PageContentHits
# href
from iamraw.href import ExtractedHyperLink
from iamraw.href import ExtractedHyperLinks
# images
from iamraw.images import ImageInformation
from iamraw.images import ImageInformations
from iamraw.images import PageContentImageInfo
from iamraw.images import PageContentImageInfos
# lang
from iamraw.lang import Language
from iamraw.lang import simplelang
# layout
from iamraw.layout import Layout
from iamraw.layout import Layouts
# likelihood
from iamraw.likelihood import Likelihood
from iamraw.likelihood import PageContentLikelihood
from iamraw.likelihood import PageContentLikelihoods
# lines
from iamraw.line import PageContentLine
from iamraw.line import PageContentLines
# list
from iamraw.list import ListType
from iamraw.list import PageContentList
from iamraw.list import PageContentLists
from iamraw.list import PageList
# magic
from iamraw.magic import PageContentContentType
from iamraw.magic import PageContentContentTypes
from iamraw.magic import PageContentType
# pages
from iamraw.page import PageSizeBorder
from iamraw.page import PageSizeBorderList
# content
from iamraw.pagecontent import PageContent
from iamraw.pagecontent import PageContents
# pdf
from iamraw.pdfinfo import InvalidPDF
from iamraw.pdfinfo import PDFDate
from iamraw.pdfinfo import PDFInfo
from iamraw.pdfinfo import PDFVersion
# person
from iamraw.person import NoPerson
from iamraw.person import Person
from iamraw.person import Persons
# quote
from iamraw.quote import ExtractedQuotation
from iamraw.quote import ExtractedQuotations
from iamraw.quote import PageContentBlockQuotes
from iamraw.quote import PageContentBlockQuotesList
# sections
from iamraw.sections import AbbreviationTable
from iamraw.sections import Abstract
from iamraw.sections import AreaItem
from iamraw.sections import AreaItems
from iamraw.sections import Bibliography
from iamraw.sections import CiteContent
from iamraw.sections import CitePart
from iamraw.sections import CodeTable
from iamraw.sections import DocumentSection
from iamraw.sections import FigureTable
from iamraw.sections import MainPart
from iamraw.sections import MultipleSection
from iamraw.sections import NotImplementedItem
from iamraw.sections import PartOfDocMixin
from iamraw.sections import PartsOfDoc
from iamraw.sections import SectionMixin
from iamraw.sections import Sections
from iamraw.sections import SectionsList
from iamraw.sections import TableOfContent
from iamraw.sections import TableTable
# solution
from iamraw.solution import Doctails
from iamraw.solution import ProblemStatus
from iamraw.solution import Solution
from iamraw.solution import Solutions
from iamraw.solution import Text
from iamraw.solution import Web
# spacestation
from iamraw.spacestation import DocumentCharDist
from iamraw.spacestation import DocumentWordDist
# style
from iamraw.style import DocTextStyle
from iamraw.style import PageTextProperties
from iamraw.style import PageTextPropertiesList
from iamraw.style import TextProperties
from iamraw.style import TextProperty
# table
from iamraw.table import PageContentTableBounding
from iamraw.table import PageContentTableBoundings
from iamraw.table import TableBounding
from iamraw.table import TableBoundings
# text
from iamraw.text import ChapterText
from iamraw.text import ChapterTextList
from iamraw.text import ContentType
from iamraw.text import DocumentContent
from iamraw.text import HeadlineWithContent
from iamraw.text import PageContentText
from iamraw.text import PageContentTexts
from iamraw.text import PageNumber
from iamraw.text import Paragraph
from iamraw.text import ParagraphContent
from iamraw.text import ParagraphItem
from iamraw.text import Paragraphs
from iamraw.text import TextSection
from iamraw.text import TextSections
from iamraw.text import Undefined
# textposition
from iamraw.textposition import PageContentTextPosition
from iamraw.textposition import PageContentTextPositions
from iamraw.textposition import TextPosition
from iamraw.textposition import TextPositions
# title
from iamraw.title import PROF_DR
from iamraw.title import AcademicTitle
# title
from iamraw.titlepage import THESIS
from iamraw.titlepage import Institution
from iamraw.titlepage import Matrikel
from iamraw.titlepage import TitleDate
from iamraw.titlepage import TitlePage
from iamraw.titlepage import TitlePages
from iamraw.titlepage import TitleThesisType
# table of content
from iamraw.toc import Section
from iamraw.toc import SectionList
from iamraw.toc import SectionRaw
from iamraw.toc import Toc
from iamraw.toc import TocLinkMixin
from iamraw.toc import TocLinkMixins
from iamraw.toc import create_toc
from iamraw.toc import merge_toc
from iamraw.toc import tosection
from iamraw.toc import tosectionraw
# webconfig
from iamraw.webconfig import WebConfig
# whitepage
from iamraw.whitepage import PageContentWhitepage
from iamraw.whitepage import PageContentWhitepages
from iamraw.whitepage import WhitePage

__version__ = '4.41.1'

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
