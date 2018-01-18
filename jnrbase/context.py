#
"""path_context - Environment modifying context handlers support."""
# Copyright © 2014-2018  James Rowe <jnrowe@gmail.com>
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

from typing import ContextManager, Dict, Union


@contextlib.contextmanager
def chdir(__path: str) -> ContextManager:
    """Context handler to temporarily switch directories.

    Args:
        __path: Directory to change to

    Yields:
        Execution context in ``path``
    """
    old = os.getcwd()
    try:
        os.chdir(__path)
        yield
    finally:
        os.chdir(old)


@contextlib.contextmanager
def env(**kwargs: Union[Dict[str, str], None]) -> ContextManager:
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
        os.environ.clear()
        # This apparent duplication is because putenv doesn’t update
        # os.environ, and os.environ changes aren’t propagated to subprocesses.
        for k, v in old.items():
            os.environ[k] = v  # NOQA: B003
            os.putenv(k, v)
        for k, v in kwargs.items():
            if v is None:
                del os.environ[k]
            else:
                os.environ[k] = v  # NOQA: B003
                os.putenv(k, v)
        yield
    finally:
        os.environ.clear()
        for k, v in old.items():
            os.environ[k] = v  # NOQA: B003
            os.putenv(k, v)
