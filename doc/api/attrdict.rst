.. currentmodule:: jnrbase.attrdict

attrdict
========

.. autoclass:: AttrDict

Examples
--------

.. testsetup::

    from jnrbase.attrdict import AttrDict

.. doctest::

    >>> ad = AttrDict(a=1, b=2)
    >>> ad.a
    1
    >>> ad.b += 1
    >>> ad.b
    3
