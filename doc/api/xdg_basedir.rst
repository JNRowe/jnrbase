.. module:: jnrbase.xdg_basedir
   :synopsis: XDG base directory support

xdg_basedir
===========

Constants
---------

.. autodata:: ALLOW_DARWIN

Functions
---------

.. autofunction:: user_cache
.. autofunction:: user_config
.. autofunction:: user_data

.. autofunction:: get_configs
.. autofunction:: get_data

.. autofunction:: get_data_dirs

.. _xdg_basedir-examples:

Examples
--------

.. testsetup::

    from jnrbase.xdg_basedir import (user_cache, user_config, user_data,
                                     get_configs, get_data)

.. doctest::
   :options: +SKIP

    >>> user_cache('rdial')
    '/home/jay/.cache/rdial'
    >>> user_config('awesome')
    '/home/jay/.config/awesome'
    >>> user_data('gnupg')
    '/home/jay/.local/share/gnupg'

    >>> get_configs('taskwarrior', 'uda.rc')
    ['/home/jay/.config/taskwarrior/uda.rc']
    >>> get_data('git_certs', 'github.com.pem')
    '/home/jay/.local/share/git_certs/github.com.pem'
    >>> get_data('awesome', 'icons/awesome.svg')
    '/usr/share/awesome/icons/awesome.svg'
