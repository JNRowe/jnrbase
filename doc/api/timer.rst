.. currentmodule:: jnrbase.timer

timer
=====

.. autoclass:: Timer

Examples
--------

.. testsetup::

    from time import sleep

    from jnrbase.timer import Timer

.. doctest::

    >>> with Timer() as t:
    ...     sleep(0.25)
    >>> t.elapsed >= 0.25
    True
