#
"""utils - Utility functions for tests"""
# Copyright © 2014-2017  James Rowe <jnrowe@gmail.com>
#
# This file is part of jnrbase.
#
# jnrbase is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# jnrbase is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# jnrbase.  If not, see <http://www.gnu.org/licenses/>.

import sys

from functools import partial
from os import path
from unittest.mock import patch


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


def mock_path_exists(result=True):
    """Decorator to setup mock for ``os.path.exists``

    If given a list, it will return the values in LIFO order.

    If given a mapping, it will return the value associated with the given key
    or False.

    Args:
        result: Value to return from mock object
    """
    if isinstance(result, bool):
        matcher = lambda s: result  # NOQA: E731
    elif isinstance(result, dict):
        matcher = lambda s: result.get(s, False)  # NOQA: E731
    else:
        matcher = lambda s: result.pop()  # NOQA: E731
    return patch.object(path, 'exists', matcher)


def mock_platform(result='darwin'):
    """Decorator to setup mock for ``sys.platform``"""
    return patch.object(sys, 'platform', result)


patch_env = partial(patch.dict, 'os.environ')
