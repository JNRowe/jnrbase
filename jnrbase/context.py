#
"""path_context - Environment modifying context handlers support."""
# Copyright © 2014-2018  James Rowe <jnrowe@gmail.com>
#
# SPDX-License-Identifier: GPL-3.0-or-later
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
from pathlib import Path
from typing import ContextManager, Dict, Union


@contextlib.contextmanager
def chdir(__path: Path) -> ContextManager:
    """Context handler to temporarily switch directories.

    Args:
        __path: Directory to change to

    Yields:
        Execution context in ``path``
    """
    old = Path.cwd()
    try:
        os.chdir(str(__path))
        yield
    finally:
        os.chdir(str(old))


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
        # This apparent duplication is because ``putenv`` doesn’t update
        # ``os.environ``, and ``os.environ`` changes aren’t propagated to
        # subprocesses.
        for key, value in old.items():
            os.environ[key] = value  # NOQA: B003
            os.putenv(key, value)
        for key, value in kwargs.items():
            if value is None:
                del os.environ[key]
            else:
                os.environ[key] = value  # NOQA: B003
                os.putenv(key, value)
        yield
    finally:
        os.environ.clear()
        for key, value in old.items():
            os.environ[key] = value  # NOQA: B003
            os.putenv(key, value)
