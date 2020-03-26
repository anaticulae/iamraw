# Changelog

Every noteable change is logged here.

## v1.18.5

## v1.18.4

### Feature

* add flag to disable logging (ac407fd498df)

## v1.18.3

## v1.18.2

### Feature

* move code from hey project (8d0b5e7861f0)
* add new typing information (8701a7f3d2af)
* use new default loader feature (9f79acb2ba52)
* extend default sections (eac9f91d2bb4)

## v1.18.1

### Feature

* extend interface to define default items/ctor (3078fb219a53)
* extend sections interface (6c7ca8ee5946)
* add default section and optional section constructor (96d5c633722a)
* add key function to sort text alphabetically (683b544890cc)

### Fix

* improve interface definition (64750c2743e1)
* do not dump methods/callable (753045406f3a)

## v1.18.0

### Feature

* skip empty text navigators (12a645a60097)
* add datatype to describe list of FootNotes (43639ff0bafe)
* number - add module to convert Roman to Arabic numbers (da681e8801c9)
* add simple mechanism to sort words alphabetically (c49fe817d8ba)
* add flag to avoid filling navigators with empty navigators (5f794480cb29)

## v1.17.8

### Feature

* move missing code (c4a9c1d08e9b)

## v1.17.7

### Fix

* fix assert_list assetion (00f6f9af5813)

## v1.17.6

### Feature

* extend public API (69937840541c)

## v1.17.5

## v1.17.4

## v1.17.3

### Feature

* extend public API (72fda4bc2236)

## v1.17.2

### Feature

* add texmex package to store text analysis methods (4ebd8ebddd69)
* add method to create TextContainer/Line from string (5b9a4e6df4a1)

## v1.17.1

### Fix

* add missing package import (441455201d58)

## v1.17.0

### Feature

* move textnavigator creator methods (3d65e03021b8)
* move path from hey module (f37a73a66fbc)
* textnavigator and fontstore from `hey` project (f47fe8a6b4ca)

## v1.16.4

### Fix

* ensure that 0 or '' is dumped (302c0894f126)

## v1.16.3

### Feature

* do not add any newline (74617c51d025)

## v1.16.2

### Feature

* improve repr behavior (388ec796cfe8)
* add method to add pages directly (b543bd499e24)
* add append method to simplify code (15781c521afe)

## v1.16.1

### Feature

* add new typing information (d98b8bdad9dd)
* add TextContainers typing information (518bb8493163)

### Fix

* handle newlines in document correctly (73c856a9bce8)

## v1.16.0

### Feature

* add data structure table and load and dumper (cdda340b54ac)
* add line module with dumper and loader (ad3c5c39cb2d)
* add BoundingBoxes to describe list of boxes (eba337f36a1b)

### Fix

* ensure that member have correct data type (09c5122cb202)

## v1.15.1

## v1.15.0

### Feature

* add new datatype and new serialization format (15840ab415ee)
* improve data structure (39b447fded62)
* extend serialization of PageContentFooterHeader (e787addacfdf)

## v1.14.2

### Feature

* add dumping page number and page number raw of extract footer (cecd48b47cba)

## v1.14.1

### Fix

* support FootRawNote without raw representation (f41c2dacd039)

## v1.14.0

### Feature

* split footnote into raw and logical note (b1f867786456)

## v1.13.0

### Feature

* add method to increase area of footer and header (dcb65337c2c7)
* add append method to header and footer information (23034d994ed0)
* add basic methods to ease working with Page (47c72f030300)

## v1.12.12

## v1.12.11

## v1.12.10

## v1.12.9

### Feature

* validate before dump/load to avoid broken data (a0f9a4421c84)
* add method to validate list of <page,content> (db6cda00f23c)

### Documentation

* add general doc structure (e499a0e69015)

## v1.12.8

### Documentation

* Happy New Year! (75fffe64d457)

## v1.12.7

### Feature

* extend interface of TocLink and rename to Mixin (336ace1e1105)

## v1.12.6

### Fix

* support multiple sections (c14d32e8c207)

## v1.12.5

### Fix

* add missing new parameter forwarding (ee3e1051e15a)

## v1.12.4

### Feature

* add `raw` and `page` to Section (2ca652b36790)

### Documentation

* extend module description (8c84babecdb0)

## v1.12.3

### Feature

* extend interface documentation (6473e5c177c0)
* add support dumping list and dict of Whitepages (bedbb5616c9e)

## v1.12.2

### Feature

* add start and end property to Headlines container (75d4801085da)

## v1.12.1

## v1.12.0

### Feature

* add AcademicTitle from `hey` project (d477b96b2e74)
* add Headlines definition to public API (f5b31cff9ea7)
* headline - add ranged container id (d465be4f04d4)

### Documentation

* move definition to top of module (669451b5b9db)

## v1.11.2

### Fix

* skip correct pages - load only parts of bigger sections (354cf956ea6a)

## v1.11.1

### Feature

* add `pages` selector to load defined pages (a46ffec03206)

### Documentation

* fix rst doc list (3624e8a71753)

## v1.11.0

### Feature

* add method to dump and load white pages (377960e6568e)
* add split method to split `BoundingBox`es (64d8082aee7d)
* add MultipleSection to store multiple DocumentSection on a page (b6ef1b0636e0)

### Fix

* fix area computation (91ae4efd4f6a)

### Documentation

* fix docs representation (b5a2695cdeac)

## v1.10.4

## v1.10.3

## v1.10.2

### Fix

* fix document loader and serializer (c49c24939c5b)

## v1.10.1

### Fix

* extend load and dump method with new data (d66509d1aced)

## v1.10.0

### Feature

* add text rise to mark character as superscripts or subscripts (ab6b201059b4)
* add method to determine size of BoundingBox (d6a415367df5)

### Fix

* solve todo to investigate __repr__ method (35c6f613cb02)
* round coordinates to avoid confusing with math accuracy (451566c16066)

## v1.9.0

### Feature

* add method to dump/load footerheader, footnotes (515ad2d3ac3d)

## v1.8.13

## v1.8.12

## v1.8.11

## v1.8.10

## v1.8.9

## v1.8.8

### Documentation

* add translation of different `Institution` parameter (dfb54e37acbe)

## v1.8.7

### Feature

* add `THESIS` to public API (a66c9d0827fb)
* add `Diplomarbeit` to Document-Master-Type (2ddd7e43f10f)

## v1.8.6

## v1.8.5

## v1.8.4

## v1.8.3

## v1.8.2

## v1.8.1

## v1.8.0

### Feature

* add TitlePage to store information of title page of document (1c9237cc050a)

### Documentation

* extend interface documentation (be778a89ab9d)

## v1.7.5

## v1.7.4

## v1.7.3

### Feature

* convert single item list to single value (25195df6e6d0)

## v1.7.2

## v1.7.1

### Feature

* support multiple like hoods on one page (78ed5d5d2464)

## v1.7.0

### Feature

* add pages feature to analyze specific pages (3524fa88f1eb)

### Fix

* do not serialize empty pages (b69e9236c7ab)

## v1.6.0

### Feature

* add method to dump and load text position (ac7b94a10fde)

### Fix

* remove page_count use __len__ instead (5f954a99cef6)
* do not save font index (ba33e76b67fb)

## v1.5.7

### Feature

* skip empty entries (bf3d8f9995a1)

## v1.5.6

### Feature

* add specific page number to dumped boxes/horizontals (4794a0c51549)
* add repr to font to easier write unit tests (20739f310152)

### Documentation

* add information about required environment variables (c96cd32656b0)

## v1.5.5

## v1.5.4

### Feature

* add page number to font serializer (868a0bfb9c32)

## v1.5.3

### Feature

* add page number to page border and bounding (f0995331e968)

### Fix

* fix missing utila API change (7d4734aefd19)

## v1.5.2

### Feature

* add page number to dump/load_boundingboxes (0d869a3793f1)

## v1.5.1

### Fix

* add type check to ease debugging (7f0ea91c1917)

## v1.5.0

### Feature

* add page number to save chunks of annotation (8d33ac652a0f)

## v1.4.3

## v1.4.2

## v1.4.1

### Feature

* add dump and font `None` style, stretch and weight (e90282ee6db4)

## v1.4.0

### Feature

* extend font style attributes belong to pdf 1.7 standard (52098874abaa)

## v1.3.16

### Fix

* add missing `DocumentSection` `Unknown` (a2eed2a64e80)

## v1.3.15

### Fix

* fix datatype of document (a06743f7a582)

## v1.3.14

## v1.3.13

## v1.3.12

## v1.3.11

## v1.3.10

## v1.3.9

## v1.3.8

## v1.3.7

## v1.3.6

### Feature

* extend document loader/dumper with `pagesize` (ac3922469fd2)

## v1.3.5

## v1.3.4

### Fix

* fix error when dumping empty pagenumbers of double page document (d7fa1f23b0eb)

## v1.3.3

## v1.3.2

### Feature

* move method to load and dump pagesnumber from `groupme` project (ad37e4625eb1)

## v1.3.1

### Feature

* move methods to dump and load sections from `hey` (624fd59a9cab)

## v1.3.0

### Feature

* add method to load and dump parse text(list, boxed, table...) (2356ae2fc525)
* move dump/load list from `hey` project (68d077e94ea8)
* move dump/load headlines from `hey` project (a47c49ac7495)
* move dump/load boxedcontent from `hey` (d02e50e164c2)

## v1.2.0

### Feature

* add cache to all yaml loader (863a847d228c)

## v1.1.1

## v1.1.0

### Feature

* add hash method to use Font in dictionary's (70f56329b633)
* extend interface with type hints (cc88720ea324)
* add debug information to border converter (72f779169ba1)
* do not save default font style to serialized files (516a121e7c6e)
* add default font style to public API (ecdc14f86e52)
* add method to validate `Border` and `PageSize` (dd7040d860b9)

## v1.0.0

### Feature

* flip BoundingBox top/down (258694f970ad)

## v0.4.25

### Feature

* add default value for fonts(stretch, weight, style) (71e32d60dfdb)

## v0.4.24

### Feature

* add special unicode char to save special values (f75ff63de092)
* add method to determine the largest box of list of BoundingBoxes (db92ddb94fc5)

### Fix

* improve naming of fontstore-/fontcontent/header (0483a2f11fd7)

## v0.4.23

### Feature

* add method to load and save chapter (3f5e7f071322)

## v0.4.22

## v0.4.21

## v0.4.20

## v0.4.19

## v0.4.18

## v0.4.17

### Feature

* add method to dump and load likelihood (45055a271672)
* add annotation to define `PageLinks` and `Hyperlinks` (070294e147b6)

### Documentation

* extend documentation of load_pageborder (b6d66c9dbc95)

## v0.4.16

### Feature

* add __len__ to determine page count instead of `page_count` (671deda026b6)
* check length of raw data for creating `BoundingBox` (e5542601a0e3)

## v0.4.15

### Feature

* add BoundingBox constructor `from_str` (9f68119d9225)
* make document and page iterable due python protocol (5f0d0a2f33bf)

### Fix

* fix BoundingBox representation to valid python code (3dd9d4b47481)

### Documentation

* extend documentation of document class (c38585d80067)
* fix description of Boxed (ff2cbbb6c7b2)

## v0.4.14

### Feature

* move boxes code from iamraw (572f7709c6a0)

### Documentation

* extend basic readme (be4c0c321b1c)

## v0.4.13

## v0.4.12

### Feature

* add raw method to dump data of box in str (f0cb9795e957)
* extend public API with Boxed object (74ddc24685e8)
* add creation method for bounding box from_list (3d7a52d60aef)

### Fix

* fix dunder repr from BoundingBox (aa694e1e872b)
* fix class method constructor of BoundingBox (2ae1a4ce464f)
* update name of decider box output (24ec4435ad71)

## v0.4.11

### Feature

* introduce BoxedObject to have a simpler parent class (ea01e625b905)
* extend printing objects for debugging (714362b2b172)
* add dump and load fonts (0e42ac1e8f89)

## v0.4.10

### Feature

* add load and dump method to serialize border hits (e920a2e5e4e2)

## v0.4.9

### Fix

* fix order of arguments to archive x0,y0,x1,y1 in raw handling (cf6548689379)

## v0.4.8

### Feature

* support empty pages which result in Border(None,None..) (25be66d59ac7)

## v0.4.7

### Feature

* add border to represent single object and page size (b03614e9c4a9)

## v0.4.6

## v0.4.5

## v0.4.4

## v0.4.3

## v0.4.2

## v0.4.1

### Feature

* deliver as double package of iamraw and serializeraw (b4d8eee78884)
* add API to public iamraw API (265329d9e5b9)

## v0.4.0

### Feature

* merge library serializeraw to reduce upgrade complexity (5bc565baeaf0)

## v0.3.1

## v0.3.0

### Feature

* move create_toc from rawmaker (c86d8d633568)

## v0.2.3

### Feature

* add field to extract text from document, page, line (7e30ded6f287)

## v0.2.2

### Fix

* add missing data files to make package installable with requirements (a7f8e4ce45dc)

## v0.2.1

### Fix

* add missing url, install requirements when installing package (25e32ff7efb7)

## v0.2.0

### Feature

* add data structure of common document (7b0d8311cac9)

## v0.1.2

### Fix

* add level to root(toc) to simplify algorithms (b6c92925053d)

## v0.1.1

## v0.1.0

### Feature

* add Toc and Section to store a table of content with section's (75b2cf970cd0)

## v0.0.0 Initial release

