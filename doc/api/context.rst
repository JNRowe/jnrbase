.. module:: jnrbase.context

context
=======

Functions
---------

.. autofunction:: chdir(path)

.. _context-examples:

Examples
--------

.. testsetup::

    from os import listdir

    from jnrbase.context import chdir

.. doctest::

    >>> sorted(listdir('.')[:2])
    ['.travis.yml', 'README.rst']
    >>> with chdir('doc'):
    ...     sorted(listdir('.'))[:3]
    ['NEWS.rst', 'alternatives.rst', 'api']
    >>> sorted(listdir('.')[:2])
    ['.travis.yml', 'README.rst']
