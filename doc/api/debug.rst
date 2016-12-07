.. currentmodule:: jnrbase.debug

debug
=====

.. autoclass:: DebugPrint

.. autofunction:: noisy_wrap

.. autofunction:: enter
.. autofunction:: exit

Examples
--------

.. testsetup::

    from jnrbase.debug import (enter, exit)

.. doctest::

    >>> @enter()
    ... def f():
    ...     print('Hello')
    >>> f()
    Entering <function f at 0x...>
    Hello
    >>> f = exit(f)
    >>> f()
    Entering <function f at 0x...>
    Hello
    Exiting <function f at 0x...>
    >>> enter(lambda: None)()
    Entering <function <lambda> at 0x...>