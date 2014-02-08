#
# coding=utf-8
"""xdg_basedir - XDG base directory support"""
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

# See http://standards.freedesktop.org/basedir-spec/basedir-spec-latest.html

import sys

from os import (getenv, path)


#: Allow OSX directory structure
ALLOW_DARWIN = True

# See https://developer.apple.com/library/ios/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/MacOSXDirectories/MacOSXDirectories.html
# for the Apple directory documentation


def user_cache(pkg):
    """Return a cache location honouring $XDG_CACHE_HOME.

    :param str pkg: Package name
    :rtype: ``str``

    """
    if ALLOW_DARWIN and sys.platform == 'darwin':
        user_dir = path.expanduser('~/Library/Caches')
    else:
        user_dir = getenv('XDG_CACHE_HOME',
                          path.join(getenv('HOME', '/'), '.cache'))
    return path.join(user_dir, pkg)


def user_config(pkg):
    """Return a config location honouring $XDG_CONFIG_HOME.

    :param str pkg: Package name
    :rtype: ``str``

    """
    if ALLOW_DARWIN and sys.platform == 'darwin':
        user_dir = path.expanduser('~/Library/Preferences')
    else:
        user_dir = getenv('XDG_CONFIG_HOME',
                          path.join(getenv('HOME', '/'), '.config'))
    return path.join(user_dir, pkg)


def user_data(pkg):
    """Return a data location honouring $XDG_DATA_HOME.

    :param str pkg: Package name
    :rtype: ``str``

    """
    if ALLOW_DARWIN and sys.platform == 'darwin':
        user_dir = '~/Library/Application Support'
    else:
        user_dir = getenv('XDG_DATA_HOME', path.join(getenv('HOME', '/'),
                          '.local/share'))
    return path.join(user_dir, pkg)


def get_configs(pkg, name='config'):
    """Return all configs for given package.

    :param str pkg: Package name
    :param name name: Configuration file name
    :rtype: ``list`` of ``str``

    """
    dirs = [user_config(pkg), ]
    dirs.extend(path.join(d, pkg)
                for d in getenv('XDG_CONFIG_DIRS', '/etc/xdg').split(':'))
    configs = []
    for dir in reversed(dirs):
        test_path = path.join(dir, name)
        if path.exists(test_path):
            configs.append(test_path)
    return configs


def get_data(pkg, name):
    """Return top-most data file for given package.

    :param str pkg: Package name
    :param name name: Data file name
    :rtype: ``str``

    """
    dirs = [user_data(pkg), ]
    dirs.extend(path.join(d, pkg)
                for d in getenv('XDG_DATA_DIRS',
                                '/usr/local/share/:/usr/share/').split(':'))
    for dir in dirs:
        test_path = path.join(dir, name)
        if path.exists(test_path):
            return test_path
    raise IOError('No data file %r for %r' % (name, pkg))


def get_data_dirs(pkg):
    """Return all data directories for given package.

    :param str pkg: Package name
    :rtype: ``list`` of ``str``

    """
    dirs = [user_data(pkg), ]
    dirs.extend(path.join(d, pkg)
                for d in getenv('XDG_DATA_DIRS',
                                '/usr/local/share/:/usr/share/').split(':'))
    return [dir for dir in dirs if path.isdir(dir)]