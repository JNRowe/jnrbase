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

Copyright © 2014-2017  James Rowe.

jnrbase is free software: you can redistribute it and/or modify it under the
terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

jnrbase is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
jnrbase.  If not, see <http://www.gnu.org/licenses/>.
