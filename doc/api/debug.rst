.. module:: jnrbase.debug
   :synopsis: Miscellaneous debugging support

debug
=====

.. autoclass:: DebugPrint

Functions
---------

.. autofunction:: noisy_wrap

.. autofunction:: on_enter
.. autofunction:: on_exit

.. _debug-examples:

Examples
--------

.. testsetup::

    from jnrbase.debug import on_enter, on_exit

.. doctest::

    >>> @on_enter()
    ... def f():
    ...     print('Hello')
    >>> f()
    Entering 'f'(<function f at 0x...>)
    Hello
    >>> f = on_exit(f)
    >>> f()
    Entering 'f'(<function f at 0x...>)
    Hello
    Exiting 'f'(<function f at 0x...>)
    >>> on_enter(lambda: None)()
    Entering '<lambda>'(<function <lambda> at 0x...>)
