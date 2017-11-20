.. module:: jnrbase.attrdict
   :synopsis: Dictionary with attribute access

attrdict
========

Classes
-------

.. autoclass:: AttrDict
   :special-members: __delattr__, __getattr__, __setattr__

.. autoclass:: ROAttrDict
   :special-members: __setattr__

.. _attrdict-examples:

Examples
--------

.. testsetup::

    from jnrbase.attrdict import AttrDict, ROAttrDict

.. doctest::

    >>> ad = AttrDict(a=1, b=2)
    >>> ad.a
    1
    >>> ad.b += 1
    >>> ad.b
    3

    >>> ro_ad = ROAttrDict()
    >>> ro_ad.c = 1
    Traceback (most recent call last):
      ...
    AttributeError: <class 'jnrbase.attrdict.ROAttrDict'> is read-only
