#
"""config - Configuration loading support."""
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

from configparser import ConfigParser
from os import environ
from pathlib import Path

from .human_time import parse_timedelta
from .iso_8601 import parse_datetime, parse_delta
from .xdg_basedir import get_configs


def read_configs(__pkg: str, __name: str = 'config', *,
                 local: bool = True) -> ConfigParser:
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
        __pkg: Package name to use as base for config files
        __name: File name to search for within config directories
        local: Whether to include config files from current directory
    Returns:
        Parsed configuration files
    """
    configs = get_configs(__pkg, __name)
    if local:
        localrc = Path('.{}rc'.format(__pkg)).absolute()
        if localrc.exists():
            configs.append(localrc)

    cfg = ConfigParser(
        converters={
            'datetime': parse_datetime,
            'humandelta': parse_timedelta,
            'timedelta': parse_delta,
        })
    for fname in configs:
        with fname.open() as f:
            cfg.read_file(f, 'utf-8')
    cfg.configs = configs

    if 'NO_COLOUR' in environ or 'NO_COLOR' in environ:
        cfg.colour = False
    elif __pkg in cfg:
        if 'colour' in cfg[__pkg]:
            cfg.colour = cfg[__pkg].getboolean('colour')
        if 'color' in cfg[__pkg]:
            cfg.colour = cfg[__pkg].getboolean('color')
    else:
        cfg.colour = True

    return cfg
