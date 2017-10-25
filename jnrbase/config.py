#
"""config - Configuration loading support."""
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

from configparser import ConfigParser
from os import environ, path

from .human_time import parse_timedelta
from .iso_8601 import parse_datetime, parse_delta
from .xdg_basedir import get_configs


def read_configs(pkg, name='config', *, local=True):
    """Process configuration file stack.

    We export the time parsing functionality of ``jnrbase`` as custom
    converters for :class:`configparser.ConfigParser`:

    ===================  ===========================================
    Method               Function
    ===================  ===========================================
    ``.getdatetime()``   :func:`~jnrbase.iso_8601.parse_datetime`
    ``.gethumantime()``  :func:`~jnrbase.human_time.parse_timedelta`
    ``.gettimedelta()``  :func:`~jnrbase.iso_8601.parse_delta`
    ===================  ===========================================

    Args:
        pkg (str): Package name to use as base for config files
        name (str): File name to search for within config directories
        local (bool): Whether to include config files from current directory
    Returns:
        configparser.ConfigParser: Parsed configuration files
    """
    configs = get_configs(pkg, name)
    if local:
        localrc = path.abspath('.{}rc'.format(pkg))
        if path.exists(localrc):
            configs.append(localrc)

    cfg = ConfigParser(converters={
        'datetime': parse_datetime,
        'humandelta': parse_timedelta,
        'timedelta': parse_delta,
    })
    cfg.read(configs, 'utf-8')
    cfg.configs = configs

    if 'NO_COLOUR' in environ:
        cfg.colour = False
    elif pkg in cfg and 'colour' in cfg[pkg]:
        cfg.colour = cfg[pkg].getboolean('colour')
    else:
        cfg.colour = True

    return cfg
