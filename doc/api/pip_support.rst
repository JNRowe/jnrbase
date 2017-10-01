.. currentmodule:: jnrbase.pip_support

pip_support
===========

.. autofunction:: parse_requires

Examples
--------

.. testsetup::

    from jnrbase.pip_support import parse_requires

.. doctest::
   :options: +ELLIPSIS

    >>> parse_requires('extra/requirements-test.txt')
    ['click>=3.0', ..., 'pytest-cov>=1.8']
