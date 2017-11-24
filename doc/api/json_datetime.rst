.. module:: jnrbase.json_datetime
   :synopsis: :abbr:`JSON (JavaScript Object Notation)` datetime support

json_datetime
=============

Functions
---------

.. autofunction:: json_serialise

    Implemented with :func:`functools.singledispatch`.

.. autofunction:: datetime_serialise

    Specialisation of :func:`json_serialise`.

.. autofunction:: json_to_datetime

.. function:: dump(...)

    Simple :func:`json.dump` wrapper using :func:`json_serialise`.

.. function:: dumps(...)

    Simple :func:`json.dumps` wrapper using :func:`json_serialise`.

.. function:: load(...)

    Simple :func:`json.load` wrapper using :func:`json_to_datetime`.

.. function:: loads(...)

    Simple :func:`json.loads` wrapper using :func:`json_to_datetime`.

.. _json_datetime-examples:

Examples
--------

.. testsetup::

    from datetime import datetime, timezone

    from jnrbase.json_datetime import dumps, loads

.. doctest::

    >>> data = {'test': datetime(2016, 11, 30, 18, 35, tzinfo=timezone.utc)}
    >>> dumps(data, indent=None)
    '{"test": "2016-11-30T18:35:00Z"}'
    >>> loads(dumps(data, indent=None)) == data
    True
