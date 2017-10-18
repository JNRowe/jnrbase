Upgrading notes
===============

..
  Much of this stuff is automated locally, but I’m describing the process for
  other people who will not have access to the same release tools I use.  The
  first thing I recommend that you do is find/write a tool that allows you to
  automate all of this, or you’re going to miss important steps at some point.

Beyond the high-level you can find in NEWS.rst_, you’ll find some more specific
upgrading advice in this document.

.. contents::
   :local:

Python 2 removal (0.5.0)
------------------------

Since the merge of :pr:`2`, Python 2 is no longer been supported.  If you’re
using ``jnrbase`` in a project that requires Python 2 support two paths
available:

* Pin your dependency, for example you can use ``jnrbase<0.5.0`` in pip_
  requirement files
* Upgrade *your* project to Python 3

If you choose to upgrade *your* project, plenty of documents exist to help.
Start with the official :ref:`porting guide <python:pyporting-howto>`, and end
with a thumb through the extensive :ref:`”what’s new” documents
<python:whatsnew-index>` from the Python documentation.

Feel free to ask me for advice or help too.  I have enjoyed porting projects to
Python 3 over the past ten years [1]_ , and this offer is even open to people
who are not using ``jnrbase``.

Switching to ``ConfigParser`` (0.6.0)
-------------------------------------

Since the merge of :pr:`3`, :mod:`jnrbase.config` has been using
:class:`~configparser.ConfigParser`.  Although :pypi:`configobj` has always
been awesome, it is — unfortunately — no longer maintained.

The biggest changes you’ll probably notice are that the getters are named
differently.  For example, :meth:`as_bool` becomes
:meth:`~configparser.ConfigParser.getboolean`.  For the list of default getters
see the :class:`configparser.ConfigParser` documentation.

A significant improvement that has been made is adding the time parsers from
:mod:`jnrbase` as custom getters for the :obj:`ConfigObj` objects returned by
``read_configs``.  See the :func:`~jnrbase.config.read_configs` documentation
for the list of supported functions.

.. [1] My earliest `public commit`_ for Python 3 support I can find is in
       ``pyisbn``

.. _NEWS.rst: https://github.com/JNRowe/jnrbase/blob/master/NEWS.rst
.. _pip: https://pip.pypa.io/
.. _public commit: https://github.com/JNRowe/pyisbn/commit/d63b2b884c862f9ee5fb24359376f7f363da22a5
