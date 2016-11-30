.. currentmodule:: jnrbase.template

template
========

.. autodata:: FILTERS
   :annotation: = {<name>: <filter function>, ...}

.. autofunction:: jinja_filter

.. autofunction:: colourise
.. autofunction:: highlight
.. autofunction:: html2text
.. autofunction:: regexp
.. autofunction:: relative_time

.. autofunction:: setup

Examples
--------

.. testsetup::

    from jnrbase.template import (FILTERS, regexp)

.. doctest::

    >>> FILTERS['regexp']('hello', 'l', 'L')
    'heLLo'
    >>> regexp('hello', 'l', 'L')
    'heLLo'
