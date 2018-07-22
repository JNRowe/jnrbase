#
"""xdg_basedir - XDG base directory support."""
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
#
# SPDX-License-Identifier: GPL-3.0+

# See http://standards.freedesktop.org/basedir-spec/basedir-spec-latest.html

import sys
from os import getenv, path
from typing import List


#: Allow macOS directory structure
ALLOW_DARWIN = True


def user_cache(__pkg: str) -> str:
    """Return a cache location honouring :envvar:`XDG_CACHE_HOME`.

    .. envvar:: XDG_CACHE_HOME

        See XDG base directory spec.

    Args:
        __pkg: Package name
    """
    if ALLOW_DARWIN and sys.platform == 'darwin':
        user_dir = '~/Library/Caches'
    else:
        user_dir = getenv('XDG_CACHE_HOME',
                          path.sep.join([getenv('HOME', ''), '.cache']))

    return path.expanduser(path.sep.join([user_dir, __pkg]))


def user_config(__pkg: str) -> str:
    """Return a config location honouring :envvar:`XDG_CONFIG_HOME`.

    .. envvar:: XDG_CONFIG_HOME

        See XDG base directory spec.

    Args:
        __pkg: Package name
    """
    if ALLOW_DARWIN and sys.platform == 'darwin':
        user_dir = '~/Library/Preferences'
    else:
        user_dir = getenv('XDG_CONFIG_HOME',
                          path.sep.join([getenv('HOME', ''), '.config']))
    return path.expanduser(path.sep.join([user_dir, __pkg]))


def user_data(__pkg: str) -> str:
    """Return a data location honouring :envvar:`XDG_DATA_HOME`.

    .. envvar:: XDG_DATA_HOME

        See XDG base directory spec.

    Args:
        __pkg: Package name
    """
    if ALLOW_DARWIN and sys.platform == 'darwin':
        user_dir = '~/Library/Application Support'
    else:
        user_dir = getenv('XDG_DATA_HOME',
                          path.sep.join([getenv('HOME', ''), '.local/share']))
    return path.expanduser(path.sep.join([user_dir, __pkg]))


def get_configs(__pkg: str, __name: str = 'config') -> List[str]:
    """Return all configs for given package.

    Args:
        __pkg: Package name
        __name: Configuration file name
    """
    dirs = [user_config(__pkg), ]
    dirs.extend(path.expanduser(path.sep.join([d, __pkg]))
                for d in getenv('XDG_CONFIG_DIRS', '/etc/xdg').split(':'))
    configs = []
    for dname in reversed(dirs):
        test_path = path.join(dname, __name)
        if path.exists(test_path):
            configs.append(test_path)
    return configs


def get_data(__pkg: str, __name: str) -> str:
    """Return top-most data file for given package.

    Args:
        __pkg: Package name
        __name: Data file name
    """
    dirs = [user_data(__pkg), ]
    dirs.extend(path.expanduser(path.sep.join([d, __pkg]))
                for d in getenv('XDG_DATA_DIRS',
                                '/usr/local/share/:/usr/share/').split(':'))
    for dname in dirs:
        test_path = path.join(dname, __name)
        if path.exists(test_path):
            return test_path
    raise FileNotFoundError('No data file {!r} for {!r}'.format(__name, __pkg))


def get_data_dirs(__pkg: str) -> List[str]:
    """Return all data directories for given package.

    Args:
        __pkg: Package name
    """
    dirs = [user_data(__pkg), ]
    dirs.extend(path.expanduser(path.sep.join([d, __pkg]))
                for d in getenv('XDG_DATA_DIRS',
                                '/usr/local/share/:/usr/share/').split(':'))
    return [d for d in dirs if path.isdir(d)]
