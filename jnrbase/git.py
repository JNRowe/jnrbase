#
# coding=utf-8
"""git - Utilities for git support."""
# Copyright © 2014  James Rowe <jnrowe@gmail.com>
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

from subprocess import (CalledProcessError, check_output)

from jnrbase.context import chdir


def find_tag(matcher='v[0-9]*', strict=True, git_dir='.'):
    """Find closest tag for a git repository.

    ..note:: This defaults to `Semantic Version`_ tag matching.

    :param str matcher: Glob-style tag pattern to match
    :param bool strict: Allow commit-ish, if no tag found
    :param str git_dir: Repository to search
    :rtype: str
    :return: Matching tag name

    .. _Semantic Version: http://semver.org/
    """
    with chdir(git_dir):
        try:
            stdout = check_output(['git', 'describe', '--match=%s' % matcher,
                                   '--abbrev=8', '--dirty'])
        except CalledProcessError:
            if strict:
                raise
            stdout = check_output(['git', 'describe', '--always', '--abbrev=8',
                                   '--dirty'])

        return stdout.strip()
