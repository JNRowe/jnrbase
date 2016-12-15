.. currentmodule:: jnrbase.colourise

colourise
=========

.. note::
   This module requires click_, which ``pip`` users can install with
   the ``jnrbase[colour]`` requirement.

.. _click: https://pypi.python.org/pypi/click

Text formatting
'''''''''''''''

.. autofunction:: _colourise
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

Examples
--------

Text formatting
'''''''''''''''

.. need to figure out way to expose colouring in a sane manner

.. testsetup::

    from jnrbase import colourise
    from jnrbase.colourise import (fail, info, success, warn)


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
