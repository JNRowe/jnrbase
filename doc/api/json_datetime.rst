.. module:: jnrbase.json_datetime
   :synopsis: :abbr:`JSON (JavaScript Object Notation)` datetime support

json_datetime
=============

Functions
---------

.. autofunction:: json_serialise

    Implemented with :func:`functools.singledispatch`.

.. The singledispatch decorator breaks autofunction here

.. function:: datetime_serialise(__o: datetime.datetime) -> str

    Specialisation of :func:`json_serialise` for :obj:`datetime.datetime`
    objects.

.. function:: timedelta_serialise(__o: datetime.timedelta) -> str

    Specialisation of :func:`json_serialise` for :obj:`datetime.timedelta`
    objects.

.. autofunction:: json_using_iso8601

.. function:: dump(…)

    Simple :func:`json.dump` wrapper using :func:`json_serialise`.

.. function:: dumps(…)

    Simple :func:`json.dumps` wrapper using :func:`json_serialise`.

.. function:: load(…)

    Simple :func:`json.load` wrapper using :func:`json_using_iso8601`.

.. function:: loads(…)

    Simple :func:`json.loads` wrapper using :func:`json_using_iso8601`.

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
