#
# coding=utf-8
"""git - Utilities for git support."""
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

from subprocess import (check_output, CalledProcessError)

from jnrbase.compat import PY2
from jnrbase.context import chdir


def find_tag(matcher='v[0-9]*', strict=True, git_dir='.'):
    """Find closest tag for a git repository.

    .. note:: This defaults to `Semantic Version`_ tag matching.

    Args:
        matcher (str): Glob-style tag pattern to match
        strict (bool): Allow commit-ish, if no tag found
        git_dir (str): Repository to search
    Returns:
        Matching tag name

    .. _Semantic Version: http://semver.org/
    """
    command = 'git describe --abbrev=12 --dirty'.split()
    with chdir(git_dir):
        try:
            stdout = check_output(command + ['--match=%s' % matcher, ])
        except CalledProcessError:
            if strict:
                raise
            stdout = check_output(command + ['--always', ])

    if not PY2:  # pragma: Python 3
        stdout = stdout.decode('ascii', 'replace')
    return stdout.strip()
