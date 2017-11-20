.. module:: jnrbase.entry
   :synopsis: Simple, lazy, module executing support

entry
=====

Functions
---------

.. autofunction:: entry_point

.. _entry-examples:

Examples
--------

.. testsetup::

    from jnrbase.entry import entry_point

.. doctest::

    >>> @entry_point
    ... def main():
    ...     return 255
