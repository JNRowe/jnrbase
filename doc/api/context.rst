.. currentmodule:: jnrbase.context

context
=======

.. autofunction:: chdir(path)

Examples
--------

.. testsetup::

    from os import listdir

    from jnrbase.context import chdir

.. doctest::

    >>> sorted(listdir('.')[:3])
    ['.noseids', '.travis.yml', 'README.rst']
    >>> with chdir('doc'):
    ...     sorted(listdir('.'))[:3]
    ['alternatives.rst', 'api', 'background.rst']
    >>> sorted(listdir('.')[:3])
    ['.noseids', '.travis.yml', 'README.rst']
