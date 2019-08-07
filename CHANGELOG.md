# Changelog

Every noteable change is logged here.

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

