.. module:: jnrbase.cmdline
   :synopsis: Command line functionality for jnrbase

cmdline
=======

.. note::
   This module requires click_, which :program:`pip` users can install with the
   ``jnrbase[cmdline]`` requirement.

.. _click: https://pypi.org/project/click/

For information on the command line interface itself, see the :doc:`jnrbase
manpage <../jnrbase.1>`.

Support functions
-----------------

.. autofunction:: get_default

.. autofunction:: text_arg

.. _cmdline-examples:

Examples
--------

.. code-block:: console

    $ jnrbase --version
    jnrbase, version 0.9.0
    $ jnrbase pretty-time 2018-01-18T00:00
    about six hours ago
    $ jnrbase config rdial 'run wrappers' mutt
    -c mutt mail
