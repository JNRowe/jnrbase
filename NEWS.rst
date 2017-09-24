User-visible changes
====================

.. contents::

0.5.0 - 2017-09-24
------------------

* Python 2 support has been removed… but, if you really need it file an issue_
  or peg the ``jnrbase`` dependency to ``<0.5``
* Python 3.5 is the minimum supported version… but, if you desperately need
  support for 3.{2..4} file an issue_
* Many functions now use `keyword-only arguments`_ for option setting
  arguments

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

.. _keyword-only arguments: https://www.python.org/dev/peps/pep-3102/
.. _Jinja2: https://pypi.python.org/pypi/Jinja2

0.4.0 - 2017-04-03
------------------

* New ``safe_hasattr`` to workaround Python 2 oddness
* ``parse_datetime`` can generate naïve timestamps
* Python 3.6  is now supported

0.3.0 - 2016-12-21
------------------

* ``debug.{enter,exit}`` output now includes the function name
* ``Timer`` has been renamed to ``Timing`` to match PEP-343 naming
* contextlib2_ is required with Python v3.4, or earlier
* Python 3.5 is now supported
* Python 2.6 support has been removed… but, if you need it file an issue_

.. _contextlib2: https://pypi.python.org/pypi/contextlib2
.. _issue: https://github.com/JNRowe/jnrbase/issues

0.2.0 - 2016-12-14
------------------

* First public release, start of a maintained package release process

0.1.0 - 2014-01-28
------------------

* Initial release
