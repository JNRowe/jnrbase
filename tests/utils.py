#
# coding=utf-8
"""utils - Utility functions for tests"""
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
    from unittest.mock import patch
except ImportError:
    from mock import patch

from jnrbase.compat import StringIO


def func_attr(name, value):
    """Decorator to set an attribute on a function

    Args:
        name (str): Attribute name to set
        value: Value to set attribute to
    """
    def decorator(f):
        setattr(f, name, value)
        return f
    return decorator


def requires_exec(command=True):
    """Mark test as requiring external process"""
    return func_attr('requires_exec', command)


def mock_stdout(f):
    """Decorator to setup mock for ``stdout``"""
    return patch('sys.stdout', new_callable=StringIO)(f)
