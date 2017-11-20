#
"""path_context - Environment modifying context handlers support."""
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

import contextlib
import os


@contextlib.contextmanager
def chdir(path):
    """Context handler to temporarily switch directories.

    Args:
        path (str): Directory to change to

    Yields:
        Execution context in ``path``
    """
    old = os.getcwd()
    try:
        os.chdir(path)
        yield
    finally:
        os.chdir(old)


@contextlib.contextmanager
def env(**kwargs):
    """Context handler to temporarily alter environment.

    If you supply a value of ``None``, then the associated key will be deleted
    from the environment.

    Args:
        kwargs: Environment variables to override

    Yields:
        Execution context with modified environment
    """
    old = os.environ.copy()
    try:
        for k, v in kwargs.items():
            if v is None:
                del os.environ[k]
            else:
                os.environ[k] = v
        yield
    finally:
        os.environ = old
