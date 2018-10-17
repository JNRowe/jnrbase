Dependency choices
==================

A lot of the value derived from this package is provided by its dependencies,
and this section explains the reasoning behind the choices.

.. note::

    The notes here aren’t meant to be unbiased, and you should use whatever
    works for you.  I keep it here mainly as a reference for myself.

The following headings are references to the ``extras`` identifiers for the
given functionality.

.. contents::
   :local:

``colour``
----------

.. literalinclude:: ../extra/requirements-colour.txt

See :ref:`click_for_color-label`.

``doc``
-------


:pypi:`Sphinx` is a no-brainer.  There is simply no better documentation
generator.  Built on a base of simple, stable choices, like :pypi:`jinja2` and
:pypi:`pygments`.

:pypi:`sphinx_rtd_theme` is the theme used by the excellent `Read the Docs`_
site, and having local builds closely mirror hosted documentation is clearly
a good call.


``iso_8601``
------------

.. literalinclude:: ../extra/requirements-iso_8601.txt

:pypi:`ciso8601` is an extremely fast parser for ISO-8601 compatible dates and
datetimes.  It is *hundreds* of times faster than many alternatives, and
*thousands* of times faster than some.

.. code-block:: console

    $ dt="2017-11-11T07:29:13
    $ python -m timeit -s 'from parsedatetime import Calendar; p = Calendar()' \
        "p.parse('$dt')"
    1000 loops, best of 3: 544 usec per loop
    $ python -m timeit -s 'from dateutil import parser' "parser.parse('$dt')"
    10000 loops, best of 3: 199 usec per loop
    $ python -m timeit -s 'from datetime import datetime' \
        "datetime.strptime('$dt', '%Y-%m-%dT%H:%M:%S')"
    10000 loops, best of 3: 48.7 usec per loop
    $ python -m timeit -s 'from pyrfc3339 import parse' "parse('${dt}Z')"
    10000 loops, best of 3: 40.6 usec per loop
    $ python -m timeit -s 'from ciso8601 import parse_datetime' \
        "parse_datetime('2017-11-11T07:29:13')"
    1000000 loops, best of 3: 0.573 usec per loop

I really can’t recommend it enough, especially as it will force you to use
standardised timestamps in your applications.

``net``
-------

.. literalinclude:: ../extra/requirements-net.txt

The use of :pypi:`httplib2` is a difficult choice to make.  A few years ago
there was no real competition at all, but…

A large chunk of the Python community appears to have coalesced around
``requests`` in recent years, but it isn’t suited to the environments I work
in.  The way it bundles packages means that nearly every system I use piles
patches on top of it to work around problems, if they bother to support it at
all.

With the missing packages and randomly patched source, it is a complete
nightmare to debug.  And with that, simply not an option.

.. note::

    ``httplib2`` isn’t immune to this, since 0.7.0 the :pypi:`socks` package is
    bundled.  However, the functionality isn’t used all that often and the
    removal patches are all small, simple and *most importantly* uniform across
    systems.

``template``
------------

.. literalinclude:: ../extra/requirements-template.txt

See :ref:`click_for_color-label`.

:pypi:`html2text` was chosen as it supports the systems I use, and is packaged
by the major distributions.  An alternative that produced |reST| would be taken
in a heartbeat.

:pypi:`jinja2` is the only choice for templating in my eyes.  Not only is the
package well designed, it is also already in use by many of the projects I use
via ``Sphinx``.

:pypi:`Pygments` is without contenders.  It has lexers for basically every
language_ imaginable, and an enormous number of styles_.

``test``
--------

.. literalinclude:: ../extra/requirements-test.txt
    :lines: 2-

:pypi:`hiro` is a cool little package for modifying system time for use in
tests, and works really well.  If you need to fiddle the time thousands of
times in a testsuite then libfaketime_ may be a better choice, but for regular
use ``hiro`` is great.

Over the years I’ve been the umpire of a ping pong championship between
:pypi:`nose2` and :pypi:`pytest`.  I prefer ``nose2`` over ``pytest`` in almost
every way, but it isn’t maintained that well.  There have been times in the
past where the pinned :pypi:`six` dependency has broken ``nose2`` for ``pip``
users and as I write this it doesn’t work with current Python releases.

Once you've chosen ``pytest`` jump straight on :pypi:`pytest-cov`, and
:pypi:`pytest-randomly`.  :pypi:`coverage` is obviously important, and
randomising test order to shake out unstated dependencies is cheap way to
improve test trustworthiness.

.. |reST| replace:: :abbr:`reST (reStructuredText)`

.. _Read the Docs: https://readthedocs.org
.. _language: http://pygments.org/languages.html
.. _styles: http://pygments.org/styles.html
.. _libfaketime: http://www.code-wizards.com/projects/libfaketime/
