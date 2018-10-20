.. module:: jnrbase.httplib2_certs
   :synopsis: ``httplib2`` system certs finder

httplib2_certs
==============

.. note::
   This module requires httplib2_, which :program:`pip` users can install with
   the ``jnrbase[net]`` requirement.

.. _httplib2: https://pypi.org/project/httplib2/

Constants
---------

.. autodata:: ALLOW_FALLBACK

.. autodata:: PLATFORM_FILES
   :annotation: = {<sys.platform>: [<file>, ], …}

Functions
---------

.. autofunction:: find_certs

.. _httplib2_certs-examples:

Examples
--------

.. testsetup::

    from jnrbase.httplib2_certs import find_certs

.. doctest::
   :options: +SKIP

    >>> find_certs()
    '/etc/ssl/certs/ca-certificates.crt'
