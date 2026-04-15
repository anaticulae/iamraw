.. _bugs:

bugs
====

open
----

no unique text size
~~~~~~~~~~~~~~~~~~~

.. code-block:: none

    E       stderr:
    E       [ERROR] Traceback (most recent call last):
    E         File "C:/kiwi/kiwi/decider/.virtual/lib/site-packages/utilo/feature.py", line 330, in run_hook_safely
    E           result = hook(pages=pages)
    E         File "C:/kiwi/kiwi/decider/.virtual/lib/site-packages/groupme/feature/footer.py", line 68, in work
    E           pagetextnavigators=pagetextnavigators,
    E         File "C:/kiwi/kiwi/decider/.virtual/lib/site-packages/groupme/feature/footer.py", line 97, in extract_footerheader
    E           ).result() for strategy in strategies
    E         File "C:/kiwi/kiwi/decider/.virtual/lib/site-packages/groupme/feature/footer.py", line 97, in <listcomp>
    E           ).result() for strategy in strategies
    E         File "C:/kiwi/kiwi/decider/.virtual/lib/site-packages/groupme/footer/strategy/common.py", line 41, in result
    E           pageheight=pageheight,
    E         File "C:/kiwi/kiwi/decider/.virtual/lib/site-packages/groupme/footer/strategy/common.py", line 59, in cluster_pages
    E           with_box = prepare_clustering(pagenavigators)
    E         File "C:/kiwi/kiwi/decider/.virtual/lib/site-packages/groupme/footer/strategy/common.py", line 94, in prepare_clustering
    E           textsize = htf.document_textsize(pagetextnavigators)
    E         File "C:/kiwi/kiwi/decider/.virtual/lib/site-packages/hey/textnavigator/fonts.py", line 162, in document_textsize
    E           return statistics.mode(collected)
    E         File "C:/usr/python/372/lib/statistics.py", line 506, in mode
    E           'no unique mode; found %d equally common values' % len(table)
    E       statistics.StatisticsError: no unique mode; found 2 equally common values
    E
    E       [ERROR] while processing footer
    E       [ERROR] no unique mode; found 2 equally common values
    E       [ERROR] failed: footer
    E       [ERROR] Traceback (most recent call last):

closed
------
