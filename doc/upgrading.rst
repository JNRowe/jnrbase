Upgrading notes
===============

Beyond the high-level notes you can find in NEWS.rst_, you’ll find some more
specific upgrading advice in this document.

.. contents::
   :local:

Python 2 removal (0.5.0)
------------------------

Since the merge of :pr:`2`, Python 2 is no longer supported.  If you’re using
|modref| in a project that requires Python 2 support then two paths are
available to you:

* Pin your dependency, for example you can use ``jnrbase<0.5.0`` in pip_
  requirement files
* Upgrade *your* project to Python 3

If you choose to upgrade your project, plenty of documents exist to help.
Start with the official :ref:`porting guide <python:pyporting-howto>`, and end
with a thumb through the extensive :ref:`”what’s new” documents
<python:whatsnew-index>` from the Python documentation.

.. note::

    Feel free to ask me for advice or help too.  I have enjoyed porting
    projects to Python 3 over the past ten years [*]_ , and this offer is
    open to people who are not using |modref| too!

Switching to ``ConfigParser`` (0.6.0)
-------------------------------------

Since the merge of :pr:`3`, :func:`~jnrbase.config.read_configs` has been using
:class:`~configparser.ConfigParser`.  Although :pypi:`configobj` has always
been awesome, it is — unfortunately — no longer maintained.

The biggest changes you’ll probably notice are that the getters are named
differently.  For example, ``ConfigObj.as_bool`` becomes
:meth:`~configparser.ConfigParser.getboolean`.  For the list of default getters
see the :class:`configparser.ConfigParser` documentation.

A significant improvement that has been made is adding the time parsers from
|modref| as custom getters for the :obj:`~configparser.ConfigParser` objects
returned by ``read_configs``.  See the :func:`~jnrbase.config.read_configs`
documentation for the list of supported functions.

``httplib2`` cert handling removal (1.2.0)
------------------------------------------

It has become untenable to support ``httplib2`` certificate setup, and I can no
no longer recommend ``httplib2``.  There are various alternatives, all with
equally *odd* support for working system certificates.  It is unclear what
upgrade path one should recommend for users who need stable and repeatable
certificate handling.

See :issue:`30` for more information.

.. rubric:: Footnotes

.. [*] My earliest `public commit`_ for Python 3 support I can find is in
       ``pyisbn``

.. _NEWS.rst: https://github.com/JNRowe/jnrbase/blob/master/NEWS.rst
.. _pip: https://pip.pypa.io/
.. _public commit: https://github.com/JNRowe/pyisbn/commit/d63b2b884c862f9ee5fb24359376f7f363da22a5
