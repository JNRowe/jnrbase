.. currentmodule:: jnrbase.debug

debug
=====

.. autoclass:: DebugPrint

.. autofunction:: enter
.. autofunction:: exit

.. autofunction:: noisy_wrap

Examples
--------

.. testsetup::

    from jnrbase.debug import enter, exit

.. doctest::

    >>> @enter()
    ... def f():
    ...     print('Hello')
    >>> f()
    Entering 'f'(<function f at 0x...>)
    Hello
    >>> f = exit(f)
    >>> f()
    Entering 'f'(<function f at 0x...>)
    Hello
    Exiting 'f'(<function f at 0x...>)
    >>> enter(lambda: None)()
    Entering '<lambda>'(<function <lambda> at 0x...>)
