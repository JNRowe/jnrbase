.. module:: jnrbase.colourise
   :synopsis: Output colourisation support

colourise
=========

.. note::
   This module requires click_, which :program:`pip` users can install with the
   ``jnrbase[colour]`` requirement.

.. _click: https://pypi.org/project/click/

Constants
---------

.. autodata:: COLOUR

Functions
---------

.. autofunction:: _colourise

Text formatting
'''''''''''''''

.. autofunction:: fail
.. autofunction:: info
.. autofunction:: success
.. autofunction:: warn

Message formatting
''''''''''''''''''

.. autofunction:: pfail
.. autofunction:: pinfo
.. autofunction:: psuccess
.. autofunction:: pwarn

.. _colourise-examples:

Examples
--------

Text formatting
'''''''''''''''

.. need to figure out way to expose colouring in a sane manner

.. testsetup::

    from jnrbase import colourise
    from jnrbase.colourise import fail, info, success, warn


    colourise.COLOUR = False

.. doctest::

    >>> fail('Error!')
    'Error!'
    >>> info('Cats are not dogs')
    'Cats are not dogs'
    >>> success('Excellent')
    'Excellent'
    >>> warn('Ick')
    'Ick'
