# Changelog

Every noteable change is logged here.

## v4.72.3

### Feature

* add strategy parameter (336360fb7a86)
* add table, figure and toc path (1a9303f7322f)

## v4.72.2

### Feature

* add optional filename (23e298466be7)

## v4.72.1

### Feature

* add method to visit toc (560774db3212)

## v4.72.0

### Feature

* add list of navigators (ab4f0071c483)
* add document content type (c165bc8aafe5)

### Fix

* dump and load raw page and raw level (74d598c794c9)

## v4.71.2

### Feature

* add parameter to skip select images (06885ed18cb0)
* add pages parameter to shrink figure loader (21b493116ac2)

### Fix

* make loader path independent (5bbf3e1478ba)

## v4.71.1

### Fix

* skip reference for comparing (140969794fd7)

## v4.71.0

### Feature

* add POC identifier (c05f36a150fa)
* add figure identifier (3b23423cb881)
* add table identifier (396d84161b68)
* add reference where caption references (e7cd5124109f)

## v4.70.3

### Feature

* add more text styles (65d17399a50c)

### Fix

* do not fail on empty data (9b2ca96a226f)
* ensure that dimension is dumped correctly (7296b6394a65)

## v4.70.2

### Feature

* add parameter to define minimal line width (8231c550ea91)

### Fix

* align hidden text token correctly (c9c2f3af5e0e)

## v4.70.1

### Feature

* add bounding attribute (6eb0f8847c7c)

## v4.70.0

### Feature

* add visible method (9f6da94434e6)
* add method to hide text style (ceb11eb3c233)
* add state parameter to select different container (8a113ce6bd4e)
* add text state to select different content (24b3f6b6fed6)
* add method to dump ptn (83e235c08ebc)

### Fix

* fix text container loader (2012d151f0cb)

## v4.69.0

### Feature

* add text line style (66b3a7313f5a)
* add method to check that text line is underlined (7506241601c3)
* dump underline style (55ce540b4845)
* add underline parameter (5c452f52cdf0)
* make headline loader backward compatible (55ea5155a774)
* add confidence value (719acdbf91a9)

## v4.68.0

### Feature

* dump and load strategy field if given (dd4e94e3f96e)
* add headline group with strategy field (64b708234b7c)
* add method to check if strategy exists (b0565135d22b)

## v4.67.0

### Feature

* shorten naming (c547ec57299f)
* add xdist_max parameter to grouping (dfad82bc2910)
* add parameter to group lines by xdist (430aecfb4e81)
* add method to determine xdist change (65ffb5ed4a9f)
* make interface more configurable (6dd5ff5b5357)
* add default path to doctextstyle loader (4d16a19dffbd)
* add docstyle display method (4696549ceb74)

### Documentation

* extend interface documentation (eedae0a8de7e)

## v4.66.2

### Fix

* add newline after changing rawmaker behavior (1e73e844856e)
* dump strategy correctly (37bf41945525)

## v4.66.1

### Feature

* add state to vertical container (63a724812ddd)

### Fix

* load vertical container correctly (18dcd5952cf7)

## v4.66.0

### Feature

* ensure that year is int or not defined (017591cb3865)
* add length method (be6d5824c474)

### Fix

* add missing attribute (69976ecd78e1)
* adjust file name (53dbbcb8fe5a)

## v4.65.1

### Fix

* add index section to public API (0f75500de9d6)

## v4.65.0

### Feature

* add index data structure (6a94c9927943)

## v4.64.0

### Feature

* serialize text container state (6626b9bec04a)
* add property to access raw text state (8f8344b06269)
* add option to hide and show token (7ebf2b3f4963)
* backup old data structure (5fa39b37c100)
* do not dump default container type (f983ffae077e)
* use secure loader (163e39b9977c)

## v4.63.0

### Feature

* add option to skip pages (757b49b91609)
* add method to dump and load color statistics (ea53991fed7d)

### Fix

* make document text feed determine stable against floating bounds (f5c0468ab5d9)

## v4.62.0

### Feature

* add magic parameter to convert highnote (3b1f725e8912)

## v4.61.0

### Feature

* add raw field (d07c9c310560)

## v4.60.0

### Feature

* allow other bounding than BoundingBox (dea071897a30)
* add method to split TextInfo by position (d7242a1d1a36)

## v4.59.1

### Feature

* make bib table iterable (9d473876f4a2)

### Fix

* fix bib serializer (d45175c85b7e)

## v4.59.0

### Feature

* add separate footnote style serializer (67730c1e9283)
* add separate footnote style (5aba6bdd04ba)
* add method to serialize new bib table (5cadbf555095)
* add bib table data type (3be596f3a0db)

## v4.58.0

### Feature

* use location based index to select sub contents correctly (1bdbb96eaf34)
* add location dependent hash (fbcbdc34bc54)

## v4.57.2

### Fix

* solve naming conflict (1969544a68df)

## v4.57.1

### Feature

* add method to verify if line is a list (da1ce51b06af)

### Fix

* add toc style to serializer (776e56076fdc)

## v4.57.0

### Feature

* add method to check if sentence is a quote (45aa462ecda9)
* add quotation mark (695f281e4042)

## v4.56.0

### Feature

* add strategy option (c3d9955e3d78)
* add method to search area (5e6ebbd13baa)

## v4.55.0

### Feature

* move methods from words (fe122559a422)
* add data type to mark sentence types (29d246efaa8c)

## v4.54.0

### Feature

* add option to hash list content (c69feb0fa301)
* add pdfpage attribute (32c605a6d5d4)
* improve language lookup (f34a14f4eadf)

## v4.53.1

### Feature

* extend public interface (07519401d91f)
* shorten debug information (92e9b3f09b13)

## v4.53.0

### Feature

* use extracted mixin to store used extraction strategy (81fd8b79af1b)
* do not use toc.numbered anymore (365043f43347)
* improve raw repr of bounding location (10b1bda145a3)
* add magister (c112b5add586)
* add rotated property (828843b97ad2)
* improve error message (67a1bd999d5e)
* add method to determine pdf path (da0903e4a67c)

### Fix

* abstract method is not required (b81e21b78c3a)

## v4.52.4

### Fix

* make loader more robust (16b2e9b969ed)

## v4.52.3

### Feature

* add high density double column layout (486fe5f571f9)
* add basic class to store extraction/strategy information (363394e0fc3c)

## v4.52.2

### Feature

* add overlap parameter (6e45c52bd86b)

### Fix

* change default type (9c265c642094)

## v4.52.1

### Feature

* add pdfpage attribute (23e93a408828)
* add caption type (d9a27e7529a4)
* add number, label and text (cf064a73c6bb)

## v4.52.0

### Feature

* add footer number bounding location (c953de84941c)
* add attribute to store style of extracted toc (aa087ae73d83)

## v4.51.1

### Feature

* add method to insert content (6777c2f75a29)

## v4.51.0

### Feature

* add method to copy empty navigator hull (876707cdc4fe)
* add option to load oneline headlines (7c971e99754f)
* add raw number property (e3c014a6ce43)
* move serializer methods from textflow project (03f43902f28c)
* add undefined toc state (8430464180d5)

### Fix

* realign merge text style (c0aef239872e)

## v4.50.0

### Feature

* add toc state with only some levels (9159419e1c8f)
* add cmd line converter (d697a3c73566)
* replace document size with single page size (ed9f82e94741)
* add width and height property (1fa0ab8d3853)
* add optional page dimension for every page (d174418b7ab7)

## v4.49.0

### Feature

* allow footnotes without footnote number (67a4b2ce208d)
* add enum to save to style (ec860a7b7adf)

### Documentation

* adjust modules path (cca0cec4f3ed)
* Happy New Year! (7cb7c7eb463b)

## v4.48.0

### Feature

* add parameter to create numbered toc (ac81d7c2413a)
* add attribute to distinguish between numbered and stepped toc (443328a43dcb)
* add level data structure (940f3b8a1c26)

### Documentation

* Happy New Year! (f8a5219dccf7)

## v4.47.0

### Feature

* add raw footnote representation (c2be3dd6efc0)
* add method to rotate navigator (156598f6a866)
* shorten developer view (1357f9a2ffa2)

## v4.46.0

### Feature

* add more debugging information (59f62f61c0ff)
* add option to return data instead of group indexes (e26009fcff04)
* add method to print ptn content (1f7de8ae657a)

## v4.45.1

### Feature

* make headline hash able (b6c39ac22d59)

### Fix

* fixes headline access for data without loaded headlines (55741659ed11)

## v4.45.0

### Feature

* move path methods from groupme (519a3437f67a)
* make pagenumber sortable (a283a77ac776)
* use complex data type (bda58e3baba2)
* use safe loader (d5311fa520a8)
* add complex data type (df3330776dfa)

## v4.44.1

### Feature

* add optional replacement for every advice (581e19f80f5d)
* add hint to add reason for this hint (475b6232d2c9)

## v4.44.0

### Feature

* add TextAdvice to improve text style (928d1dfbc63d)
* reduce verbosity of missing headlines (cde202c8a825)

### Fix

* reduce debugging content (8a706f026e40)

## v4.43.1

### Feature

* support tuple as bounding (2834b5350094)
* add bounding data type (822649fb321a)
* add formula page line data type (85118a31a332)

## v4.43.0

### Feature

* add pdf font raw name (99ad6c3d696d)

## v4.42.0

### Feature

* add label bounding attribute (1e48de436d5c)
* add label attribute (ea936f75208c)

## v4.41.3

### Feature

* add default file name (9d704eb791e0)

## v4.41.2

### Feature

* add sentences path determiner (8a8a5c8223cc)

### Fix

* do not fail on empty list item (ab24d807b46e)

## v4.41.1

### Feature

* add translation lookup (5484023e8c73)

## v4.41.0

### Feature

* add method to dump and load translation (38b5f6d3ecf9)
* add translation to transform navigator indexes (920fc01253b6)
* add backup parameter to use baml sources (a8870040f781)
* add option to change path file type (a667436e3a77)
* introduce caption result and caption code (86f8d8b84a69)

## v4.40.0

### Feature

* extend debugging information (482de255ad21)
* add attribute to store groups of list item length (4942ca0082ff)

## v4.39.1

### Feature

* use plain old data (1a05e115761e)

## v4.39.0

### Feature

* add default codes loader (2d1488e4ca21)
* add codero result path (ee168ce444d2)
* use real holy values (8068ec649a76)
* detect Holy Value as non replaced variable (32e8f12b4ccc)

### Fix

* decrease debugging level (8122db65cd83)
* do not fail on passing None (70533348a8db)

## v4.38.1

### Feature

* extends replacement check for jinja templates (f4fa0a1cba4f)

## v4.38.0

### Feature

* add abbreviation lookup (f39226fae817)
* add abbreviation list (c0901bc322e4)

### Fix

* use updated holy values (02e86926feaa)

## v4.37.1

### Fix

* use a more stable hash algorithm (413555b19b98)

## v4.37.0

### Feature

* load findings from multiple directories (b7c60e22a933)
* add parameter to load findings by pages (898b8606b933)

## v4.36.2

### Feature

* add figure flag (079d75c55510)

## v4.36.1

### Feature

* add method to load findings from path (92f507f64ffd)

## v4.36.0

### Feature

* move method to store and serialize WebConfig (92a92d44b0dc)
* move method to write and load grouped findings (6f2c6272f14f)

## v4.35.0

### Feature

* add image content hash from file name (d7924a24df60)
* add path append flag (27013e95f05d)
* add attribute to store image hash value (84a00c40dc6d)

## v4.34.2

### Feature

* add path append flag (0ca917de65c1)

## v4.34.1

### Fix

* skip invalid image information (9538e12daaa4)

## v4.34.0

### Feature

* add parameter to skip hidden images (738c41eb860b)
* add hidden flag to hide images (34bc3838e2fd)

## v4.33.3

### Feature

* move image info loader method (4e070763b91e)

## v4.33.2

### Feature

* add attribute language (608f788b196e)
* add Enum to describe used language (503085581275)

### Fix

* do not use pdfinfo if file does not exist (bd9df60b2b76)

## v4.33.1

### Fix

* change expected behavior (74ddb391cd1a)

### Documentation

* move comment from protocol (91a60cbe13d6)

## v4.33.0

### Feature

* add method to load and dump docinfo (00e49c1425e2)
* unite Generator doc type (d0392577bcdc)
* rename base to undefined (0d6d143d9316)
* add sections lookup (1ee20ecac774)
* add docinfo class (e5a08a87cb5f)
* move document generator from protocol (7708084d40b9)

## v4.32.0

### Feature

* add PartOfDoc datatype (a931e1666a50)

## v4.31.1

### Feature

* add attribute to store code bounding (cf89dc20772e)

## v4.31.0

### Feature

* add option to create ptcn from file (9c3236c17f6f)
* add code storage, loading and dumping (7d8593ef187f)

## v4.30.0

### Feature

* use middle strategy to insert horizontal lines (e4930981cc9f)

## v4.29.0

### Feature

* add option to insert horizontal lines (9e43c8664744)
* ease importing section types (aebc71171e34)
* add codetable (eb86a2fca6e1)

## v4.28.1

### Feature

* rename to project experience (703252ca5ec1)

## v4.28.0

### Feature

* add paper as DocumentType (349114402487)
* clarify headlines converter (5ee94ce7cd42)
* add ebd flag (9a818807abcc)
* add list of pages layouts (5f5f2e1ee45f)

## v4.27.0

### Feature

* define page layout information (a742573324e7)

## v4.26.0

### Feature

* add text alignment Enum (3d51be113f35)

### Fix

* remove senseless import (b61edef185e8)

## v4.25.4

### Feature

* add style property to FootNoteMerged (4d154a130962)

## v4.25.3

### Feature

* use multiple of 4 to render multiple rectangle (4352977234b1)
* add optional line number to BoundingLocation (92eab3d414f6)

### Documentation

* improve documentation (2f56033518eb)

## v4.25.2

### Feature

* add prefix to adjust default path (4fd4287e6814)
* add prefix option to horizontals loader (3128542c74e9)
* add default path (f34ef74145dc)

## v4.25.1

### Fix

* handle empty font flag (47350b4a8f1e)

## v4.25.0

### Feature

* add method to remove lines from ptn (fd6f98aea0ce)
* add loader shortcut (44bb251bda8f)
* add option to disable bounding check while inserting (848d19759df3)
* use dataclass as PageTextNavigator (d0edeacc6ed7)
* makes ptn comparable (e78c86d3f29d)
* add container id to rebuild parsed container (5e4155a2d4f2)

### Documentation

* extend docs to ensure that hashing and comparing works (ef20d8f9dfdb)

## v4.24.3

### Feature

* add selective font header loading (352acccb440c)

## v4.24.2

### Feature

* make fontstore comparable (42267a33929c)

## v4.24.1

### Fix

* enable loading note/number style (5e32d75c7134)

## v4.24.0

### Feature

* make FooteNoteMerged serialize able (fef6142365da)
* add FootNote which contain multiple Notes (a7ff36964094)
* use improved converter (a4f87a91a865)

## v4.23.0

### Feature

* improve title pattern (4c245f6d57da)
* add acknowledgments section (9f9ea3f269c5)

## v4.22.3

### Feature

* add default sections file name (a521248c4cfd)

### Fix

* add missing classes to serializer (fa7b1858ade0)

## v4.22.2

### Feature

* add CiteContent to define content of CitePart (48c8b9cedf0f)
* add CitePart data type (ef6784dd014b)
* add habil doc data type (73b396c1dccb)

## v4.22.1

### Feature

* add tablero result path (a4286f6c954e)

### Documentation

* adjust interface documentation (a1f746a6975c)

## v4.22.0

### Feature

* add method to load and dump content bounding box (499c48a39027)
* add ContentBoundingBox (737efd652660)
* add option to pass page numbers as int (ea7fa18e029e)

## v4.21.1

### Feature

* add support for BoundingBox and tuple (8d0ae7ce6e92)

## v4.21.0

### Feature

* make valid yaml header (203e77c59da3)
* use yamlpages fast loader/writer (d17cb31afc06)
* use fast yaml loader and writer (b1dded930d34)
* add single list as yamlpages loader/writer (1e9f29554ca1)
* use improved dumper/loader (75adcc08d24d)
* add method to dump yamlpages to str (eec1806ac6e1)
* add improved yaml loader and writer (c2ccfc1ecc1d)

### Fix

* skip empty content (371fdeb69e27)

## v4.20.0

### Feature

* add option to load invalid pdf info (8b25e3b37a94)
* add SectionRaw str converter (f4d1a59e90c6)
* add navigator shortcuts (e69ccddb9e65)

## v4.19.0

### Feature

* move PDFInfo from rawmaker (2bb2c426fab9)

## v4.18.0

### Feature

* add spacestation paths (4b94f3b5ea79)
* move spacestation serialize and data structure (97a6c0139b1a)

## v4.17.7

### Fix

* add missing new yaml ctor (ba3ef1b430b9)

## v4.17.6

## v4.17.5

### Fix

* ensure that hack is loaded correctly (b3532edffcd2)

## v4.17.4

## v4.17.3

### Fix

* adjust test to different layout parsing (18ff89440055)

## v4.17.2

### Feature

* convert to dataclass (ce95dee6e353)
* add outlines path (1126d36ccdac)

## v4.17.1

### Feature

* add another prof-dr-matching rule (93678fc55e9e)

## v4.17.0

### Feature

* add separate page dimension (279f2998f901)
* add default footer path (5d31d69d6cf4)

### Fix

* skip empty page (2a9fd34f084c)

## v4.16.0

### Feature

* enable between, after, before for ptn (0b77ed0d1bab)

## v4.15.0

### Feature

* add option to dump None position (d7ec631fbdea)
* add image info loader to public API (cb23b761a56e)

## v4.14.3

### Feature

* improve text connector (16ce09f6f66c)
* move words path result methods (7d6050f48463)

## v4.14.2

### Fix

* allow dumping empty elements (2f063424d362)

## v4.14.1

### Feature

* make TextInfo hash-able (9b507c095fe7)
* add tuple unpacking (ab33a827b883)

## v4.14.0

### Feature

* add method to determine most common fontid (2c07608bd6df)
* add method to count number of included character (390016c88266)

## v4.13.0

### Feature

* move dot to separate module, extend documentation (f73896a287c8)
* add Boxed data type (ec272d01ac88)

## v4.12.1

### Feature

* add bounding to FootNote (a2aa971a9808)

### Fix

* round footer range (807bf428063c)

## v4.12.0

### Feature

* add yrange of content (0ea5dd8c0011)

## v4.11.4

### Feature

* add footnotes loader (8e2a0e01ddb3)

## v4.11.3

### Feature

* add page information (7c1b4407b03f)

## v4.11.2

### Feature

* move function to merge different AcademicTitle's (c6c508d702d1)

### Fix

* enable content outside pages (7a324e1dee3f)

## v4.11.1

### Fix

* extend master title pattern (c7aeb6f81f76)

## v4.11.0

### Feature

* precise academic shortcut (e5d4f036cde7)
* add default file name (ad3b1713bbe5)
* add default level to overwrite None (02acd7e6e66b)

## v4.10.3

### Feature

* skip comparing raw and confidence field (c2317cdc395f)

## v4.10.2

### Fix

* fix author access label (a4d0a08cf128)

## v4.10.1

### Feature

* bib loader, use person and noperson instead of dict (e8439a01cec7)

## v4.10.0

### Feature

* enable complex author parsing (864ee932a3af)
* add data structure and serializer for extract quote (1251ed81a68a)

## v4.9.0

### Feature

* add method to dump and load `word spaces` (893f43397a56)
* add option to define default file name (c9a6d436061e)

## v4.8.0

### Feature

* add general page content loader (64f508f2bed4)

### Documentation

* Happy New Year! (7540138dea64)

## v4.7.0

### Feature

* increase required logging level (264314763877)
* add default loading file names (9c9c568739b3)
* do not compare raw content of bib ref (2c490d1296dc)
* add raw_pdfpage item to describe where references is detected (a7b508d032af)

## v4.6.0

### Feature

* introduce negative person parsing result (6d07156d1b87)

## v4.5.0

### Feature

* make object subscriptable (0bc7e8a2ebfc)
* add method to dump and store docref's (467c60d70b75)
* add data structure to store extracted hyperlinks (04ef41d197ea)
* add accessed field to bib ref (4a1a3bd8b836)

## v4.4.2

## v4.4.1

### Fix

* decrease the level of error to inform instead of abort (900b0f5c5773)

## v4.4.0

### Feature

* ensure that math characters are correctly (5a100e5bb7ca)
* add raw property (590d8cbd2893)
* add default load file name (37d50e98fde1)
* add default file name (fe3349180863)

## v4.3.0

### Feature

* add decoration field and update serializer (7d73fa8b3127)
* add `single` method to merge textpagenavigators (099486ec81e8)

## v4.2.0

### Feature

* extend list serializer to handle multiple list pages (b92e45fc9591)
* add default file name for list loader (252ecc3df033)
* add method to remove selected magic data from ptcn (7392ed71bbbb)
* add str method to ease debugging (bbe64a5cfef3)
* add method to determine path to magic result (47c8c5bb0d1d)
* add default magic file name to magic loader (bc65ee28b840)
* add option to load findings by page number (c9bd945bd2c8)

## v4.1.0

### Feature

* add default file name to page number loader (443f38505a52)
* add field `position` to store location of caption (49c0ea17753d)
* log error if no font information is provided (4cf888f98d77)
* add SectionsList data type (14af976c2756)
* add method to determine textdistance from content navigator (6d687b12ab48)

## v4.0.1

### Feature

* add dumping BoundingBox and tuple as location (1ac82ebd559a)

## v4.0.0

### Feature

* ensure that number is represented as int (6763bbb64504)
* introduce datatype to represent list of PageSize (774cfd564413)

### Fix

* select the most common item as font size of textstyle (8260bc1204e2)

## v3.2.0

### Feature

* add method to determine section path (0d8ca172455a)
* add width property to CharStyle (6a65cb9feb34)
* add level 4 docstyle fields (8a069e333410)
* add default name to load border hits (94af0dc6452c)
* move data structure/loader from hey project (b17200b10e97)
* extend pattern to support negative page numbers (51be24ecdd1b)
* add missing raw field to headline dumper (ee82d10f52d3)
* add page attribute to TextProperty (f2ce67a5fc61)

## v3.1.1

### Fix

* extend missing API externalization (58d558ca6cb1)

## v3.1.0

### Feature

* move findings serializer/data from protocol (b14220f63ce5)

## v3.0.0

### Feature

* add method to convert headlines to toc (4ff739e135b6)
* rename text to title and introduce more raw_ fields (55369d63e59e)
* add raw_ representation to enable comparing more data (414e2b537c3c)
* add bounding to MultilineGroup (56d2d571f80d)
* add methods to convert caption to raw (06113436ff5f)
* add paths for `caption` package (c676e796db11)
* add Abstract and TableTable objects (17fc2297c786)

## v2.4.2

### Feature

* add method to dump and load leftright page border (007fcf0f6cea)

## v2.4.1

## v2.4.0

### Feature

* add rotation to signal rotated text/chars (ab04e0d1a9af)
* complain about wrongly used data type (200f81b0b53d)
* add location of parsing source (efd8ba2927a8)
* increase readability of yaml files (f92b6bfb0358)

## v2.3.0

### Feature

* add path method for extracted images and formulas (d1f674467a44)
* improve readability of raw formula serializer (4184931e513d)

### Documentation

* add formula dump and load test (752271d57182)

## v2.2.0

### Feature

* move method to dump, load and store doctextstyle (68f0dfeb0325)

## v2.1.0

### Feature

* add data structure to store raw formulas (db3b5f44b3ee)

### Fix

* ensure to dump valid lists (ddddd080760b)

## v2.0.0

### Feature

* replace text structure with more complex from words project (6ddaf6f98331)
* extend public API (3489c5b6d08d)
* inform about asserting data type (3c57ba2eaf44)
* move methods to store, load and dump distance from groupme (25545f8d1821)

### Fix

* ensure to handle section content border correctly (88f1178446e5)
* add number of char when determining text style statistics (b104c8da7ba6)

## v1.31.3

## v1.31.2

## v1.31.1

### Feature

* move caption dump, load and store methods (c37aff69e795)

## v1.31.0

### Feature

* add method to dump, load and store figures (172b4cc8e6b6)

## v1.30.1

### Feature

* skip empty page dumping (ee350310479c)

## v1.30.0

### Feature

* add images information loader (187db4111d5a)

## v1.29.0

### Feature

* add method to store, dump and load formulas (a66a44367de6)

## v1.28.0

### Feature

* add between method to check that BoundingBox is in range (853e7d8906af)

## v1.27.2

## v1.27.1

## v1.27.0

### Feature

* add method to dump, load and store block quotes (9fc2c7b5d5e2)

## v1.26.0

### Feature

* improve list representation (569262579085)
* introduce data types to store PageListContent (564fc68b7485)
* log font accessing error (14e584c0bf3b)

### Documentation

* extend interface documentation (1a0b8fd882cd)

## v1.25.8

### Feature

* add method to dump and load image information (c53d7c2e37e7)
* add publisher, yearend, hyperlink entree (96771683bd31)

## v1.25.7

### Feature

* add data structure to store, dump and load bibliography (d6494f4802e1)
* add datatype for multiple title pages (0682b765effd)
* extend list of document types (c304fb9c58d2)

### Fix

* fix some style issues (bcd28e80def4)

## v1.25.6

### Fix

* fix missing path renaming (5ee5b34343e4)

## v1.25.5

### Fix

* make interface less strict (566bf36c7d33)

## v1.25.4

## v1.25.3

### Feature

* introduce parameter to avoid double data generating (a94fe2b83655)

## v1.25.2

### Feature

* load None level headlines correctly (ab312d3113f7)
* enable prefix path (4beb16db5933)
* add method to create pagetextcontentnavigator from file (8d7ba7696493)

### Documentation

* extend interface documentation (431f761f07e2)

## v1.25.1

### Feature

* extend supported Roman numbers (98891c096aab)

### Fix

* handle empty text feed correctly (67d01a7838dc)

## v1.25.0

### Feature

* add parameter to define used accuracy to determine text size (16dc02a72429)
* add data type to store and parse pdf dates (6e1fa97ec4b9)
* extend public iamraw API (a3a35f154dae)
* add method to convert `table of content` to string (a33cb894c0b9)

## v1.24.2

### Fix

* fix path to new rawmaker generator (83e6b0abc443)
* replace with words code (c4c8de538eba)

## v1.24.1

### Fix

* add missing dump/load of raw_location (2c03a0355d31)

## v1.24.0

### Feature

* introduce SectionRaw to store collecting information (7575b1d5263b)

### Fix

* fix default toc loading resource (6dab98115caf)
* replace private variable access (cc9c1d13a2db)

## v1.23.4

## v1.23.3

### Feature

* add sections type (56eef79eeeee)
* add datatype of multiple persons (ed31ce8955ac)

## v1.23.2

### Fix

* support loading invalid boxes (edd42eb35d9d)

## v1.23.1

### Fix

* harden text load against bad parsed headlines (9e9db240e069)

## v1.23.0

### Feature

* support loading text without headlines (196724f949cd)

### Fix

* ensure to handle None headlines correctly (a98d9f59c9e9)

## v1.22.3

## v1.22.2

### Fix

* change TextInfo to describe distances to page (efa02e5a24e6)
* fix left and right border of pagecontentnavigator (8981feeee1a2)

## v1.22.1

### Feature

* add method to store, load and dump text abbreviations (17c58e6c4a8c)

### Fix

* adjusted expected tuple length, add missing import (f0946f5fb460)
* update person matching pattern (e5bcfb11d066)

## v1.22.0

### Feature

* move method to count text lines (23da6cd36e39)
* add abbreviation table dumper and loader (56da7752d915)
* move TitleThesisType (2125d62d2d7a)
* add PageContentText (d2b38aa0f5f2)

## v1.21.3

## v1.21.2

### Feature

* add further navigator accessing strategy (029453a35f0f)
* add item assignment operation (4d43e0781ac7)
* add method to create pagetextnavigator from file (e39627b1e215)
* extend public API (79c1867af19f)

## v1.21.1

### Fix

* add missing if statement (c5c523fd34ec)

## v1.21.0

### Feature

* introduce mean field to describe alternative top border (3dc39fde61bd)
* add copy method to solve todo (16a2d8fde286)
* solve todo due introducing better data structure (34f48585344f)
* add bounding selector strategy to PageTextNavigator (524f2df1e439)

## v1.20.6

## v1.20.5

## v1.20.4

## v1.20.3

### Fix

* solve linter warning (8ca78d6ee9f9)

## v1.20.2

### Fix

* add missing VerticalText loader (3c173b3f25ba)

## v1.20.1

### Feature

* add flag to decide which text direction to select (60846bf9cef3)

## v1.20.0

### Feature

* add vertical container to store vertical text chunks (bc4a9e976c93)

### Fix

* update to new font definition (d76a00c4062d)

## v1.19.1

### Feature

* extend public API (83f1496a73f4)

## v1.19.0

### Feature

* add parameter fontflag to describe style of printed font (a26e0dab4504)
* add Enum to describe font flags (4dca7da0f824)

## v1.18.7

### Feature

* add default path handler to simplify code (ea0e98faa591)

## v1.18.6

### Feature

* fulfill Latin and Greek replacement table (0b4b084d394d)

### Fix

* access page content correctly (19ee83dd78c9)

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

