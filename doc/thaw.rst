``jnrbase`` Evolution
=====================

The idea for :mod:`jnrbase` began in January 2014, and lasted throughout most of
the year in a sort of idling back burner way.  The problem was simply one of
support, if you wanted to support users who depended on pip_ or setuptools_ you
couldn't reliably use ``extras`` on dependencies.  And without ``extras`` you
either had to break the project up in to many tiny ones, or force all the
optional dependencies on all the users.

Two -- nearly three -- years later, and the situation has changed somewhat.
Given the combination of pip_ now reasonably supporting ``extras`` and frankly
it becoming decreasingly common for installation in the circles I move in, it is
time to resurrect this project.

The future
----------

As of 2016-12-01, branches already exist for all my public projects.
:mod:`jnrbase` support hasn't been merged to ``master`` on any of them so far
though, but it likely just a matter of time.

Should the functionality show itself to be useful, or should I feel the need to
add dependencies on :mod:`jnrbase` on group maintained projects, the trajectory
could change.  So, consider it fluid for now and if you have questions `feel free
to ask`_!

.. _pip: http://www.pip-installer.org/
.. _setuptools: https://pypi.python.org/pypi/setuptools
.. _feel free to ask: jnrowe@gmail.com
