.. currentmodule:: jnrbase.timer

timer
=====

.. autoclass:: Timing

Examples
--------

.. testsetup::

    from datetime import timedelta
    from time import sleep

    from jnrbase.timer import Timing

.. doctest::

    >>> with Timing() as t:
    ...     sleep(0.25)
    >>> t.elapsed >= timedelta(milliseconds=250)
    True
