# Changelog

Every noteable change is logged here.

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

