``jnrbase`` Evolution
=====================

The idea for |modref| began in January 2014, and lasted throughout the year in
a rather idling on the back burner way.  The problem was simply one of support,
if you wanted to support users who depended on pip_ or setuptools_ you couldn’t
reliably use ``extras`` on dependencies.  And without ``extras`` you either had
to break the project up in to many tiny ones, or force all the optional
dependencies on all the users.

Two — nearly three — years later, and the ecosystem has changed somewhat.
Given the combination of pip_ now supporting ``extras`` and, frankly, it
becoming far less common for installation in the circles I move in, it is
therefore time to resurrect this project.

The future
----------

As of 2017-10-25, branches already exist for all my public projects.  |modref|
support hasn’t been merged to ``master`` on all of them yet, but it is just
a matter of time.

Should the functionality show itself to be useful, or should I feel the need to
add dependencies on |modref| on group maintained projects, the trajectory could
change.  So, consider it fluid for now and if you have questions `feel free to
ask`_!

.. _pip: http://www.pip-installer.org/
.. _setuptools: https://pypi.org/project/setuptools/
.. _feel free to ask: jnrowe@gmail.com
