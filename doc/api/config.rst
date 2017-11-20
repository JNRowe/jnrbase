.. module:: jnrbase.config
   :synopsis: Configuration loading support

config
======

Functions
---------

.. autofunction:: read_configs

.. _config-examples:

Examples
--------

.. testsetup::

    from mock import patch

    from jnrbase.config import read_configs

.. doctest::

    >>> cfg = read_configs('jnrbase')
    >>> assert cfg.colour
    >>> with patch.dict('os.environ', {'NO_COLOUR': 'true'}):
    ...     cfg = read_configs('jnrbase')
    >>> assert not cfg.colour
