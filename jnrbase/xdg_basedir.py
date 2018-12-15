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
ALLOW_DARWIN = True  # type: bool

__LOCATIONS = {
    'cache': ('Caches', '.cache'),
    'config': ('Preferences', '.config'),
    'data': ('Application Support', '.local/share'),
}  # type: Dict[str, Tuple[str, str]]


def __user_location(__pkg: str, type_) -> str:
    """Utility function to look up XDG basedir locations

    Args:
        __pkg: Package name
        __type: Location type
    """
    if ALLOW_DARWIN and sys.platform == 'darwin':
        user_dir = '~/Library/{}'.format(__LOCATIONS[type_][0])
    else:
        user_dir = getenv(
            'XDG_{}_HOME'.format(type_.upper()),
            path.sep.join([getenv('HOME', ''), __LOCATIONS[type_][1]])
        )
    return path.expanduser(path.sep.join([user_dir, __pkg]))


def __xdg_lookup(name):
    def tmpl(__pkg: str) -> str:
        """Return a {0} location honouring :envvar:`XDG_{1}_HOME`.

        .. envvar:: XDG_{1}_HOME

            See XDG base directory spec.

        Args:
            __pkg: Package name
        """
        return __user_location(__pkg, name)

    tmpl.__doc__ = tmpl.__doc__.format(name, name.upper())
    return tmpl


user_cache = __xdg_lookup('cache')
user_config = __xdg_lookup('config')
user_data = __xdg_lookup('data')


def get_configs(__pkg: str, __name: str = 'config') -> List[str]:
    """Return all configs for given package.

    Args:
        __pkg: Package name
        __name: Configuration file name
    """
    dirs = [
        user_config(__pkg),
    ]
    dirs.extend(
        path.expanduser(path.sep.join([d, __pkg]))
        for d in getenv('XDG_CONFIG_DIRS', '/etc/xdg').split(':')
    )
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
    for dname in get_data_dirs(__pkg):
        test_path = path.join(dname, __name)
        if path.exists(test_path):
            return test_path
    raise FileNotFoundError('No data file {!r} for {!r}'.format(__name, __pkg))


def get_data_dirs(__pkg: str) -> List[str]:
    """Return all data directories for given package.

    Args:
        __pkg: Package name
    """
    dirs = [
        user_data(__pkg),
    ]
    dirs.extend(
        path.expanduser(path.sep.join([d, __pkg])) for d in
        getenv('XDG_DATA_DIRS', '/usr/local/share/:/usr/share/').split(':')
    )
    return [d for d in dirs if path.isdir(d)]
