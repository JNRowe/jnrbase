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

    jnrbase [option]… <command>

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

.. click:: jnrbase.cmdline:certs
   :prog: jnrbase certs

.. click:: jnrbase.cmdline:config_
   :prog: jnrbase config

.. click:: jnrbase.cmdline:dirs
   :prog: jnrbase dirs
   :show-nested:

.. click:: jnrbase.cmdline:find_tag
   :prog: jnrbase find-tag

.. click:: jnrbase.cmdline:gen_text
   :prog: jnrbase gen-text

.. click:: jnrbase.cmdline:messages
   :prog: jnrbase messages
   :show-nested:

.. click:: jnrbase.cmdline:pip_requires
   :prog: jnrbase pip-requires

.. click:: jnrbase.cmdline:pretty_time
   :prog: jnrbase pretty-time


.. click:: jnrbase.cmdline:time
   :prog: jnrbase time

BUGS
----

None known.

AUTHOR
------

Written by `James Rowe <mailto:jnrowe@gmail.com>`__

RESOURCES
---------

Full documentation: https://jnrbase.readthedocs.io/

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
