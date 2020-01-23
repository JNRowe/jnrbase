#
"""git - Utilities for git support."""
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

from pathlib import Path
from subprocess import CalledProcessError, check_output

from .context import chdir


def find_tag(__matcher: str = 'v[0-9]*',
             *,
             strict: bool = True,
             git_dir: Path = Path('.')) -> str:
    """Find closest tag for a git repository.

    Note:
        This defaults to `Semantic Version`_ tag matching.

    Args:
        __matcher: Glob-style tag pattern to match
        strict: Allow commit-ish, if no tag found
        git_dir: Repository to search
    Returns:
        Matching tag name

    .. _Semantic Version: http://semver.org/
    """
    command = 'git describe --abbrev=12 --dirty'.split()
    with chdir(git_dir):
        try:
            stdout = check_output(command + [
                '--match={}'.format(__matcher),
            ])
        except CalledProcessError:
            if strict:
                raise
            stdout = check_output(command + [
                '--always',
            ])

        stdout = stdout.decode('ascii', 'replace')
    return stdout.strip()
