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
    ['contextlib2>=0.5.4;python_version<"3.4"', ..., 'mock>=0.7.1;python_version<"3.3"']
