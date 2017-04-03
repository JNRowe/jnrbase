.. currentmodule:: jnrbase.timer

timer
=====

.. autoclass:: Timing

Examples
--------

.. testsetup::

    from time import sleep

    from jnrbase.timer import Timing

.. doctest::

    >>> with Timing() as t:
    ...     sleep(0.25)
    >>> t.elapsed >= 0.25
    True
