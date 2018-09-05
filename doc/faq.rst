Frequently Asked Questions
==========================

..
    Ask them, and perhaps they’ll become frequent enough to be added here ;)

.. contents::
   :local:

.. todo::

   Transfer relevant FAQs from rdep FAQ documents

.. _click_for_color-label:

Why require ``click`` just for ``jnrbase[colour]``?
---------------------------------------------------

For the majority of use cases I have for coloured output we’re already working
with command line programs, and command line programs that I write will already
be using click_.

.. _click: https://pypi.org/project/click/

Why is there no support for naïve ``datetime`` objects?
-------------------------------------------------------

Because that way leads to madness.  I learnt this the hard way, so I don’t want
to have to relearn it in the future.

Note that it is entirely reasonable to convert :obj:`~datetime.datetime` objects
to naïve format for internal usage, in fact I do so myself for the significant
speed boost it can provide when processing *heaps* of objects.
