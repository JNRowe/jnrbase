.. currentmodule:: jnrbase.template

template
========

.. note::
   This module requires html2text_, Jinja2_, and Pygments_. ``pip`` users can
   install them with the ``jnrbase[template]`` requirement.

.. _html2text: https://pypi.python.org/pypi/html2text
.. _jinja2: https://pypi.python.org/pypi/jinja2
.. _pygments: https://pypi.python.org/pypi/pygments

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
