.. module:: jnrbase.template
   :synopsis: Jinja templating support

template
========

.. note::
   This module requires html2text_, Jinja2_, and Pygments_. :program:`pip`
   users can install them with the ``jnrbase[template]`` requirement.

.. _html2text: https://pypi.org/project/html2text/
.. _jinja2: https://pypi.org/project/jinja2/
.. _pygments: https://pypi.org/project/pygments/

Constants
---------

.. autodata:: FILTERS
   :annotation: = {<name>: <filter function>, …}

Functions
---------

.. autofunction:: jinja_filter

.. autofunction:: colourise
.. autofunction:: highlight
.. autofunction:: html2text
.. autofunction:: regexp
.. autofunction:: relative_time

.. autofunction:: setup

.. _template-examples:

Examples
--------

.. testsetup::

    from jnrbase.template import FILTERS, regexp

.. doctest::

    >>> FILTERS['regexp']('hello', 'l', 'L')
    'heLLo'
    >>> regexp('hello', 'l', 'L')
    'heLLo'
