.. module:: jnrbase.human_time
   :synopsis: Handle human readable date formats

human_time
==========

Functions
---------

.. autofunction:: human_timestamp

.. autofunction:: parse_timedelta

.. _human_time-examples:

Examples
--------

.. testsetup::

    from datetime import datetime, timedelta

    from jnrbase.human_time import human_timestamp, parse_timedelta


    now = datetime.utcnow()

.. doctest::

    >>> human_timestamp(now - timedelta(days=1))
    'yesterday'
    >>> human_timestamp(now - timedelta(hours=4))
    'about four hours ago'

    >>> parse_timedelta('3d')
    datetime.timedelta(3)
    >>> parse_timedelta('1y')
    datetime.timedelta(365)
