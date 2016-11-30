.. currentmodule:: jnrbase.json_datetime

json_datetime
=============

.. class:: DatetimeEncoder

    Custom JSON encoding for supporting ``datetime`` objects.

    See also: :class:`json.JSONEncoder`

.. autofunction:: json_to_datetime

.. function:: dump(...)

    Simple :func:`json.dump` wrapper using :class:`DatetimeEncoder`.

.. function:: dumps(...)

    Simple :func:`json.dumps` wrapper using :class:`DatetimeEncoder`.

.. function:: load(...)

    Simple :func:`json.load` wrapper using :func:`json_to_datetime`.

.. function:: loads(...)

    Simple :func:`json.loads` wrapper using :func:`json_to_datetime`.
