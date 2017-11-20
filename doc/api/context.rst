.. module:: jnrbase.context
   :synopsis: Environment modifying context handlers support

context
=======

Functions
---------

.. autofunction:: chdir(path)

.. autofunction:: env(**kwargs)

.. _context-examples:

Examples
--------

.. testsetup::

    from os import getenv, listdir

    from jnrbase.context import chdir, env

.. doctest::

    >>> sorted(listdir('.')[:2])
    ['.travis.yml', 'README.rst']
    >>> with chdir('doc'):
    ...     sorted(listdir('.'))[:3]
    ['NEWS.rst', 'alternatives.rst', 'api']
    >>> sorted(listdir('.')[:2])
    ['.travis.yml', 'README.rst']

.. doctest::

    >>> with env(SHELL='oi'):
    ...     getenv('SHELL')
    'oi'
