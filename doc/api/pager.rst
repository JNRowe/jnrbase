.. SPDX-License-Identifier: GPL-3.0-or-later

.. module:: jnrbase.pager
   :synopsis: pager pipe support

pager
=====

Functions
---------

.. autofunction:: pager

.. _pager-examples:

Examples
--------

.. testsetup::

    from jnrbase.pager import pager

.. doctest::
   :options: +SKIP

    >>> pager('long text', pager='most')
