#
# coding=utf-8
"""compat - Python 2/3 compatibility support."""
# Copyright © 2014-2016  James Rowe <jnrowe@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

try:
    from contextlib import suppress
except ImportError:
    from contextlib2 import suppress
from sys import version_info

PY2 = version_info[0] == 2

if PY2:  # pragma: Python 2
    basestring = basestring
    text = unicode

    import codecs
    open = codecs.open

    try:
        from cStringIO import StringIO
    except ImportError:  # pragma: no cover
        from StringIO import StringIO
else:  # pragma: Python 3
    basestring = str
    text = str

    open = open

    from io import StringIO  # NOQA

if PY2:  # pragma: Python 2
    def mangle_repr_type(klass):
        """Encode Unicode ``__repr__`` as strings for Python 2.

        See :func:`object.__repr__`

        Args:
            klass (class): Class to patch ``__repr__`` on
        """
        klass.__repr_unicode__ = klass.__repr__

        def wrapper(self):
            return self.__repr_unicode__().encode('utf-8')
        klass.__repr__ = wrapper
        return klass

    def safe_hasattr(obj, attr_name):
        """Check object for attribute existence.

        See :func:`hasattr`

        Args:
            attr_name (str): Attribute to test for
        """
        safe = object()
        with suppress(AttributeError):
            result = getattr(obj, attr_name, safe)
        return result is not safe

else:  # pragma: Python 3
    safe_hasattr = hasattr
    mangle_repr_type = lambda x: x
