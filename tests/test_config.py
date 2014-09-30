#
# coding=utf-8
"""test_config - Test configuration support"""
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

from os import path

from io import StringIO

from mock import patch

from jnrbase.compat import (open, text)
from jnrbase.config import read_configs


@patch('jnrbase.config.open', wraps=open)
@patch('jnrbase.xdg_basedir.path', wraps=path)
@patch('jnrbase.config.path', wraps=path)
def test_config_loading(config_path, basedir_path, open):
    open.return_value = StringIO(text(''))
    config_path.exists.return_value = True
    basedir_path.exists.return_value = True
    with patch.dict('os.environ', {'XDG_CONFIG_DIRS': 'test1:test2'}):
        cfg = read_configs('jnrbase')
        assert len(cfg.configs) == 4
        assert '/.jnrbaserc' in cfg.configs[-1]


@patch('jnrbase.config.path', wraps=path)
def test_config_loading_missing_files(path):
    path.exists.return_value = False
    assert read_configs('jnrbase').configs == []


def test_no_colour_from_env():
    with patch.dict('os.environ', {'NO_COLOUR': 'set'}):
        cfg = read_configs('jnrbase')
    assert cfg.colour is False


def test_colour_default():
    with patch.dict('os.environ', clear=True):
        cfg = read_configs('jnrbase')
    assert cfg.colour is True
