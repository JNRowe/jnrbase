.. module:: jnrbase.cmdline
   :synopsis: Command line functionality for jnrbase

cmdline
=======

.. note::
   This module requires click_, which :program:`pip` users can install with the
   ``jnrbase[cmdline]`` requirement.

.. _click: https://pypi.python.org/pypi/click

Functions
---------

.. autofunction:: get_default
.. autofunction:: cli

Generic functions
'''''''''''''''''

.. autofunction:: certs
.. autofunction:: config
.. autofunction:: find_tag
.. autofunction:: pip_requires
.. autofunction:: pretty_time
.. autofunction:: time

Text formatting
'''''''''''''''

.. function:: fail
.. function:: info
.. function:: success
.. function:: warn

.. autofunction:: gen_text

XDG basedir functions
'''''''''''''''''''''

.. function:: dirs
.. function:: cache
.. function:: config
.. function:: data

.. _cmdline-examples:

Examples
--------

.. Messy to include
