:Author: James Rowe <jnrowe@gmail.com>
:Date: 2017-11-24
:Copyright: GPL v3
:Manual section: 1
:Manual group: user

jnrbase
=======

Common utility functionality
----------------------------

SYNOPSIS
--------

    jnrbase [option]... <command>

DESCRIPTION
-----------

:mod:`jnrbase` provides an unsorted collection of library functionality, and
this program provides access to some of that from the shell.

It isn’t really meant to be a heavily used user facing program, but as the
functionality is occasionally useful providing direct access can be a fun
bonus.

OPTIONS
-------

.. program:: jnrbase

.. option:: --version

    Show the version and exit.

.. option:: --help

    Show help message and exit.

COMMANDS
--------

``certs``
~~~~~~~~~

.. program:: jnrbase certs

Find location of system certificates

.. option:: --help

    Show help message and exit.

``config``
~~~~~~~~~~

.. program:: jnrbase config

Find location of system certificates

.. option:: -n, --name <filename>

    Config file to read from.

.. option:: -l, --local / --no-local

    Read local :file:`.{package}rc` files.

.. option:: --help

    Show help message and exit.

``dirs``
~~~~~~~~

.. program:: jnrbase dirs

Extract or list values from config

.. option:: --help

    Show help message and exit.

``dirs cache``
''''''''''''''

.. program:: jnrbase dirs cache

Display cache dir honouring XDG basedir

.. option:: --help

    Show help message and exit.

``dirs config``
'''''''''''''''

.. program:: jnrbase dirs config

Display config dir honouring XDG basedir

.. option:: --help

    Show help message and exit.

``dirs data``
'''''''''''''

.. program:: jnrbase dirs data

Display data dir honouring XDG basedir


.. option:: --help

    Show help message and exit.

``find-tag``
~~~~~~~~~~~~

.. program:: jnrbase find-tag

Find tag for git repository

.. option:: -m, --match <glob>

    Limit the selection of matches with glob.

.. option:: -s, --strict

    Always generate a result.

.. option:: -d, --directory <dir>

    Git repository to operate on.

.. option:: --help

    Show help message and exit.

``gen-text``
~~~~~~~~~~~~

.. program:: jnrbase gen-text

Create output from Jinja template

.. option:: -e, --env <filename>

    JSON data to generate output with.

.. option:: --help

    Show help message and exit.

``messages``
~~~~~~~~~~~~

.. program:: jnrbase messages

Format messages for users

.. option:: --help

    Show help message and exit.

``messages fail``
'''''''''''''''''

.. program:: jnrbase messages fail

Format a failure message

.. option:: --help

    Show help message and exit.

``messages info``
'''''''''''''''''

.. program:: jnrbase messages info

Format an informational message

.. option:: --help

    Show help message and exit.

``messages success``
''''''''''''''''''''

.. program:: jnrbase messages success

Format a success message

.. option:: --help

    Show help message and exit.

``messages warn``
'''''''''''''''''

.. program:: jnrbase messages warn

Format a warning message

.. option:: --help

    Show help message and exit.

``pip-requires``
~~~~~~~~~~~~~~~~

.. program:: jnrbase pip-requires

Parse pip requirements file

.. option:: --help

    Show help message and exit.

``pretty-time``
~~~~~~~~~~~~~~~

.. program:: jnrbase pretty-time

Format timestamp for human consumption

.. option:: --help

    Show help message and exit.

``time``
~~~~~~~~

.. program:: jnrbase time

Time the output of a command

.. option:: --help

    Show help message and exit.

BUGS
----

None known.

AUTHOR
------

Written by `James Rowe <mailto:jnrowe@gmail.com>`__

RESOURCES
---------

Full documentation: http://jnrbase.readthedocs.io/

Issue tracker: https://github.com/JNRowe/jnrbase/issues/

COPYING
-------

Copyright © 2014-2018  James Rowe.

jnrbase is free software: you can redistribute it and/or modify it under the
terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

jnrbase is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
jnrbase.  If not, see <http://www.gnu.org/licenses/>.
