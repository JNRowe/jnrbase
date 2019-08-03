jnrbase - Common utility functionality
======================================

|status| |travis| |coveralls| |pypi| |pyvers| |readthedocs| |develop|

``jnrbase`` is a collection of common utility libraries that are used in the
Python projects that I (JNRowe_) work on.  Feel free to use it — and perhaps
improve it — in your projects!

``jnrbase`` is released under the `GPL v3`_ license.

Requirements
------------

``jnrbase``’s dependencies outside of the standard library are dependent on the
functionality you require, ranging from none to the following:

============  ====================================
Extra tag     Dependencies
============  ====================================
``colour``    click_ ≥ 7.0
``iso_8601``  ciso8601_ ≥ 2.0.1
``net``       httplib2_
``template``  html2text_, Jinja2_ ≥ 2.9, Pygments_
============  ====================================

It should work with any version of Python_ 3.6 or newer.  If ``jnrbase``
doesn’t work with the version of Python you have installed, file an issue_ and
I’ll endeavour to fix it.

The module has been tested on Linux, and occasionally on OSX, but it should
work fine on other systems too.

To run the tests you’ll need pytest_.  Once you have pytest_ installed you can
run the tests with the following commands:

.. code:: console

    $ pytest tests

Contributors
------------

I’d like to thank the following people who have contributed to ``jnrbase``.

Patches
'''''''

* Nathan McGregor

Bug reports
'''''''''''

* Delphine Beauchemin
* Brandon Cady

Ideas
'''''

* Ryan Sutton

If I’ve forgotten to include your name I wholeheartedly apologise.  Just drop
me a mail_ or open an issue_, and I’ll update the list!

Bugs
----

If you find any problems, bugs or just have a question about this package
either file an issue_ or drop me a mail_.

If you’ve found a bug please attempt to include a minimal testcase so I can
reproduce the problem, or even better a fix!

.. _JNRowe: https://github.com/JNRowe
.. _GPL v3: http://www.gnu.org/licenses/
.. _click: https://pypi.org/project/click/
.. _ciso8601: https://pypi.org/project/ciso8601/
.. _httplib2: https://pypi.org/project/httplib2/
.. _html2text: https://pypi.org/project/html2text/
.. _jinja2: https://pypi.org/project/jinja2/
.. _pygments: https://pypi.org/project/pygments/
.. _Python: http://www.python.org/
.. _issue: https://github.com/JNRowe/jnrbase/issues
.. _pytest: https://pypi.org/project/pytest/
.. _mail: jnrowe@gmail.com

.. |travis| image:: https://img.shields.io/travis/JNRowe/jnrbase/master.png
   :target: https://travis-ci.org/JNRowe/jnrbase
   :alt: Test state on master

.. |develop| image:: https://img.shields.io/github/commits-since/JNRowe/jnrbase/latest.png
   :target: https://github.com/JNRowe/jnrbase
   :alt: Recent developments

.. |pyvers| image:: https://img.shields.io/pypi/pyversions/jnrbase.png
   :alt: Supported Python versions

.. |status| image:: https://img.shields.io/pypi/status/jnrbase.png
   :alt: Development status

.. |coveralls| image:: https://img.shields.io/coveralls/github/JNRowe/jnrbase/master.png
   :target: https://coveralls.io/repos/JNRowe/jnrbase
   :alt: Coverage state on master

.. |pypi| image:: https://img.shields.io/pypi/v/jnrbase.png
   :target: https://pypi.org/project/jnrbase/
   :alt: Current PyPI release

.. |readthedocs| image:: https://img.shields.io/readthedocs/jnrbase/stable.png
   :target: https://jnrbase.readthedocs.io/
   :alt: Documentation
