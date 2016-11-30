.. currentmodule:: jnrbase.entry

entry
=====

.. autofunction:: entry_point

Examples
--------

.. testsetup::

    from jnrbase.entry import entry_point

.. doctest::

    >>> @entry_point
    ... def main():
    ...     return 255
