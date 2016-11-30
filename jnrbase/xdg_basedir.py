#
# coding=utf-8
"""xdg_basedir - XDG base directory support."""
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

# See http://standards.freedesktop.org/basedir-spec/basedir-spec-latest.html

import sys

from os import (getenv, path)


#: Allow macOS directory structure
ALLOW_DARWIN = True


def user_cache(pkg):
    """Return a cache location honouring :envvar:`XDG_CACHE_HOME`.

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
        list of str
    """
    dirs = [user_config(pkg), ]
    dirs.extend(path.expanduser(path.sep.join([d, pkg]))
                for d in getenv('XDG_CONFIG_DIRS', '/etc/xdg').split(':'))
    configs = []
    for dir in reversed(dirs):
        test_path = path.join(dir, name)
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
    for dir in dirs:
        test_path = path.join(dir, name)
        if path.exists(test_path):
            return test_path
    raise IOError('No data file %r for %r' % (name, pkg))


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
    return [dir for dir in dirs if path.isdir(dir)]
