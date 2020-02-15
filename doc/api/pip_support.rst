.. module:: jnrbase.pip_support
   :synopsis: ``pip`` workarounds support

pip_support
===========

Functions
---------

.. autofunction:: parse_requires

.. _pip_support-examples:

Examples
--------

.. testsetup::

    from pathlib import Path

    from jnrbase.pip_support import parse_requires

.. doctest::
   :options: +ELLIPSIS

    >>> parse_requires(Path('extra/requirements-test.txt'))
    ['click>=7.0', ..., 'pytest-randomly>=1.2']
