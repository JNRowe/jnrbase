#
"""xdg_basedir - XDG base directory support."""
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

# See http://standards.freedesktop.org/basedir-spec/basedir-spec-latest.html

import sys

from os import getenv, path


#: Allow macOS directory structure
ALLOW_DARWIN = True


def user_cache(pkg):
    """Return a cache location honouring :envvar:`XDG_CACHE_HOME`.

    .. envvar:: XDG_CACHE_HOME

        See XDG base directory spec.

    Args:
        pkg (str): Package name
    Returns:
        str
    """
    if ALLOW_DARWIN and sys.platform == 'darwin':
        user_dir = '~/Library/Caches'
    else:
        user_dir = getenv('XDG_CACHE_HOME',
                          path.sep.join([getenv('HOME', ''), '.cache']))

    return path.expanduser(path.sep.join([user_dir, pkg]))


def user_config(pkg):
    """Return a config location honouring :envvar:`XDG_CONFIG_HOME`.

    .. envvar:: XDG_CONFIG_HOME

        See XDG base directory spec.

    Args:
        pkg (str): Package name
    Returns:
        str
    """
    if ALLOW_DARWIN and sys.platform == 'darwin':
        user_dir = '~/Library/Preferences'
    else:
        user_dir = getenv('XDG_CONFIG_HOME',
                          path.sep.join([getenv('HOME', ''), '.config']))
    return path.expanduser(path.sep.join([user_dir, pkg]))


def user_data(pkg):
    """Return a data location honouring :envvar:`XDG_DATA_HOME`.

    .. envvar:: XDG_DATA_HOME

        See XDG base directory spec.

    Args:
        pkg (str): Package name
    Returns:
        str
    """
    if ALLOW_DARWIN and sys.platform == 'darwin':
        user_dir = '~/Library/Application Support'
    else:
        user_dir = getenv('XDG_DATA_HOME',
                          path.sep.join([getenv('HOME', ''), '.local/share']))
    return path.expanduser(path.sep.join([user_dir, pkg]))


def get_configs(pkg, name='config'):
    """Return all configs for given package.

    Args:
        pkg (str): Package name
        name (str): Configuration file name
    Returns:
        list[str]
    """
    dirs = [user_config(pkg), ]
    dirs.extend(path.expanduser(path.sep.join([d, pkg]))
                for d in getenv('XDG_CONFIG_DIRS', '/etc/xdg').split(':'))
    configs = []
    for d in reversed(dirs):
        test_path = path.join(d, name)
        if path.exists(test_path):
            configs.append(test_path)
    return configs


def get_data(pkg, name):
    """Return top-most data file for given package.

    Args:
        pkg (str): Package name
        name (str): Data file name
    Returns:
        str
    """
    dirs = [user_data(pkg), ]
    dirs.extend(path.expanduser(path.sep.join([d, pkg]))
                for d in getenv('XDG_DATA_DIRS',
                                '/usr/local/share/:/usr/share/').split(':'))
    for d in dirs:
        test_path = path.join(d, name)
        if path.exists(test_path):
            return test_path
    raise FileNotFoundError('No data file {!r} for {!r}'.format(name, pkg))


def get_data_dirs(pkg):
    """Return all data directories for given package.

    Args:
        pkg (str): Package name
    Returns:
        str
    """
    dirs = [user_data(pkg), ]
    dirs.extend(path.expanduser(path.sep.join([d, pkg]))
                for d in getenv('XDG_DATA_DIRS',
                                '/usr/local/share/:/usr/share/').split(':'))
    return [d for d in dirs if path.isdir(d)]
