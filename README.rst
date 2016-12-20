jnrbase - Common utility functionality
======================================

.. image:: https://img.shields.io/travis/JNRowe/jnrbase/master.svg?style=plastic
   :target: https://travis-ci.org/JNRowe/jnrbase
   :alt: Test state on master

.. image:: https://img.shields.io/coveralls/JNRowe/jnrbase/master.svg?style=plastic
   :target: https://coveralls.io/repos/JNRowe/jnrbase
   :alt: Coverage state on master

.. image:: https://img.shields.io/pypi/v/jnrbase.svg?style=plastic
   :target: https://pypi.python.org/pypi/jnrbase
   :alt: Current PyPI release

.. image:: https://img.shields.io/pypi/JNRowe/jnrbase.svg?style=plastic
   :target: https://pypi.python.org/pypi/jnrbase
   :alt: Number of downloads from PyPI

.. warning::
   This package is not ready to be used right now, and it will change
   significantly before it is.

``jnrbase`` is a collection of common utility libraries that are used in various
Open Source projects that I (JNRowe) work on.  Feel free to use it, and
especially improve it, in your projects!

``jnrbase`` is released under the `GPL v3`_ license.

Requirements
------------

``jnrbase``'s dependencies outside of the standard library are dependent on the
functionality you require, ranging from none to the following:

============  ==============================
Extra tag     Dependencies
============  ==============================
``colour``    click_
``config``    configobj_
``iso_8601``  ciso8601_, pytz_
``net``       httplib2_
``template``  html2text_, Jinja2_, Pygments_
============  ==============================

It should work with any version of Python_ 2.7 or newer, including Python 3.
If ``jnrbase`` doesn't work with the version of Python you have installed, file
an issue_ and I'll endeavour to fix it.

The module has been tested on many UNIX-like systems, including Linux and OS X,
but it should work fine on other systems too.

To run the tests you'll need nose2_.  Once you have nose2_ installed you can
run the tests with the following commands::

    $ nose2 tests

Contributors
------------

I'd like to thank the following people who have contributed to ``jnrbase``.

Patches
'''''''

* <your name here>

Bug reports
'''''''''''

* <your name here>

Ideas
'''''

* <your name here>

If I've forgotten to include your name I wholeheartedly apologise.  Just drop me
a mail_ and I'll update the list!

Bugs
----

If you find any problems, bugs or just have a question about this package either
file an issue_ or drop me a mail_.

If you've found a bug please attempt to include a minimal testcase so I can
reproduce the problem, or even better a patch!

.. _GPL v3: http://www.gnu.org/licenses/
.. _click: https://pypi.python.org/pypi/click
.. _configobj: https://pypi.python.org/pypi/configobj
.. _ciso8601: https://pypi.python.org/pypi/ciso8601
.. _pytz: https://pypi.python.org/pypi/pytz
.. _httplib2: https://pypi.python.org/pypi/httplib2
.. _html2text: https://pypi.python.org/pypi/html2text
.. _jinja2: https://pypi.python.org/pypi/jinja2
.. _pygments: https://pypi.python.org/pypi/pygments
.. _Python: http://www.python.org/
.. _issue: https://github.com/JNRowe/jnrbase/issues
.. _nose2: https://pypi.python.org/pypi/nose2/
.. _mail: jnrowe@gmail.com
