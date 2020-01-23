User-visible changes
====================

.. See doc/upgrading.rst for a more explantory discussion of major changes

.. contents::
   :local:

1.2.0 - 2020-01-23
------------------

* ``httplib2`` certificate handling is deprecated, as it has become untenable
  to support the various ``httplib2`` releases
* Python 3.5 is no longer supported

1.1.0 - 2018-11-21
------------------

* Click_ 7.0, or newer, is now required for ``[colour]`` extra
* ``gettext`` support for the command line module has been removed [#]_
* sphinx_ 1.8 and sphinx-click_ are now required to build docs

.. _sphinx: http://www.sphinx-doc.org/
.. _sphinx-click: https://pypi.org/project/sphinx-click/

1.0.0 - 2018-09-05
------------------

* API is now frozen; changes will follow semver_

.. _semver: https://semver.org/

0.11.0 - 2018-07-01
-------------------

* This release is the final release before 1.0.0; shake it and report what
  falls out!
* Python 3.7 is now supported

0.10.0 - 2018-01-18
-------------------

* This is the last planned release before 1.0.0, `report problems`_ and ask
  questions *now*
* Type hints, see :pep:`483`, have been add throughout the library
* sphinx_autodoc_typehints_ is required to build documentation

.. _report problems: https://github.com/JNRowe/jnrbase/issues
.. _sphinx_autodoc_typehints: https://pypi.org/project/sphinx_autodoc_typehints/

0.9.0 - 2017-11-24
------------------

* As advertised, ``pager``'s default value for ``$LESS`` has been removed
* ``timedelta`` objects are now supported by ``json_datetime``
* Functionality that may be useful from the command line is now available via
  ``jnrbase`` command

0.8.0 - 2017-11-20
------------------

* As advertised, ``debug``'s ``enter`` and ``exit`` have been removed
* ``context.env`` wrapper to temporarily alter environment variables
* ``graphviz`` is no longer required to build docs

0.7.0 - 2017-10-25
------------------

* As advertised, support for naïve datetimes has been removed from ``iso_8601``
* ``Timing`` now uses a ``datetime.timedelta`` for its ``elapsed`` attribute
* ``Timing`` now uses ``human_timestamp`` for its verbose output
* ``debug``’s ``enter`` and ``exit`` have been renamed to ``on_enter`` and
  ``on_exit`` respectively
* The deprecated ``debug.enter`` and ``debug.exit`` names will be removed in
  v0.8.0.
* httplib2_ v0.10, or newer, is required for ``jnrbase[net]``
* click_ is now required for ``jnrbase[template]``
* ``jnrbase[template]`` requires html2text_ 2016.5.29 or newer and Pygments
  v2.1 or newer
* Tests now require pytest-randomly_

.. _click: https://pypi.org/project/click/
.. _html2text: https://pypi.org/project/html2text/
.. _httplib2: https://pypi.org/project/httplib2/
.. _pytest-randomly: https://pypi.org/project/pytest-randomly/

0.6.0 - 2017-10-18
------------------

* This package is no longer considered an alpha, but given its new beta status
  large changes may still be made
* ``jnrbase.config`` now uses Python’s configparser_ for loading config files
* ``jnrbase.config`` exposes ``jnrbase``’s ``parse_{datetime,{time,}delta}``
  functions for value conversions
* Support for naïve datetimes will be removed in v0.7.0
* Tests now require pytest_
* configobj_ is no longer required

.. _configparser: http://docs.python.org/3/library/configparser.html
.. _pytest: https://pypi.org/project/pytest/
.. _configobj: https://pypi.org/project/configobj/

0.5.0 - 2017-09-24
------------------

* Python 2 support has been removed… but, if you really need it file an issue_
  or peg the ``jnrbase`` dependency to ``<0.5``
* Python 3.5 is the minimum supported version… but, if you desperately need
  support for 3.{2..4} file an issue_
* Many functions now use keyword-only arguments for option setting arguments,
  as defined in :PEP:`3102`

    ===========================    ====================================
    Class/function                 Option
    ===========================    ====================================
    ``config.read_configs``        ``local``
    ``git.find_tag``               ``strict`` and ``git_dir``
    ``iso_8601.parse_datetime``    ``naive``
    ``pager.pager``                ``pager``
    ``template.highlight``         ``lexer`` and ``formatter``
    ``template.html2text``         ``width`` and ``ascii_replacements``
    ``template.regexp``            ``count`` and ``flags``
    ``timer.Timing``               ``verbose``
    ===========================    ====================================

* ``iso_8601``’s ``UTC`` class has been removed in favour of the standard
  library’s ``datetime.timezone``
* Jinja2_ v2.9, or newer, is required for ``jnrbase[template]``

.. _Jinja2: https://pypi.org/project/Jinja2/

0.4.0 - 2017-04-03
------------------

* New ``safe_hasattr`` to workaround Python 2 oddness
* ``parse_datetime`` can generate naïve timestamps
* Python 3.6 is now supported

0.3.0 - 2016-12-21
------------------

* ``debug.{enter,exit}`` output now includes the function name
* ``Timer`` has been renamed to ``Timing`` to match :PEP:`343` naming
* contextlib2_ is required with Python v3.4, or earlier
* Python 3.5 is now supported
* Python 2.6 support has been removed… but, if you need it file an issue_

.. _contextlib2: https://pypi.org/project/contextlib2/
.. _issue: https://github.com/JNRowe/jnrbase/issues

0.2.0 - 2016-12-14
------------------

* First public release, start of a maintained package release process

0.1.0 - 2014-01-28
------------------

* Initial release

.. rubric:: Footnotes

.. [#] Co-workers: Use Delphine’s ``retext`` tool as a replacement.
