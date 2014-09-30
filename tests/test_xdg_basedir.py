#
# coding=utf-8
"""test_xdg_basedir - Test XDG basedir support"""
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

from mock import patch

from jnrbase import xdg_basedir


@patch('jnrbase.xdg_basedir.getenv')
def test_cache_no_args(getenv):
    getenv.return_value = '~/.xdg/cache'
    assert '/.xdg/cache/jnrbase' in xdg_basedir.user_cache('jnrbase')


@patch('jnrbase.xdg_basedir.getenv')
def test_cache_no_home(getenv):
    getenv.side_effect = lambda k, v: v
    assert xdg_basedir.user_cache('jnrbase') == '/.cache/jnrbase'


@patch('jnrbase.xdg_basedir.getenv')
def test_config_no_args(getenv):
    getenv.return_value = '~/.xdg/config'
    assert '/.xdg/config/jnrbase' in xdg_basedir.user_config('jnrbase')


@patch('jnrbase.xdg_basedir.getenv')
def test_config_no_home(getenv):
    getenv.side_effect = lambda k, v: v
    assert xdg_basedir.user_config('jnrbase') == '/.config/jnrbase'


@patch('jnrbase.xdg_basedir.getenv')
def test_data_no_args(getenv):
    getenv.return_value = '~/.xdg/local'
    assert '/.xdg/local/jnrbase' in xdg_basedir.user_data('jnrbase')


@patch('jnrbase.xdg_basedir.getenv')
def test_data_no_home(getenv):
    getenv.side_effect = lambda k, v: v
    assert xdg_basedir.user_data('jnrbase') == '/.local/share/jnrbase'


@patch('jnrbase.xdg_basedir.sys')
def test_osx_paths(sys):
    sys.platform = 'darwin'
    assert '/Library/Application Support/jnrbase' in \
        xdg_basedir.user_data('jnrbase')


@patch('jnrbase.xdg_basedir.path', wraps=path)
def test_get_configs_all_missing(path):
    path.exists.return_value = False
    assert xdg_basedir.get_configs('jnrbase') == []


@patch('jnrbase.xdg_basedir.path', wraps=path)
def test_get_configs(path):
    path.exists.return_value = True
    assert len(xdg_basedir.get_configs('jnrbase')) == 2


@patch('jnrbase.xdg_basedir.path', wraps=path)
def test_get_configs_custom_dirs(path):
    path.exists.return_value = True
    with patch.dict('os.environ', {'XDG_CONFIG_DIRS': 'test1:test2'}):
        assert len(xdg_basedir.get_configs('jnrbase')) == 3


@patch('jnrbase.xdg_basedir.sys')
@patch('jnrbase.xdg_basedir.path', wraps=path)
def test_get_configs_osx(path, sys):
    sys.platform = 'darwin'
    path.exists.return_value = True
    assert '/Library/' in xdg_basedir.get_configs('jnrbase')[-1]


@patch('jnrbase.xdg_basedir.path', wraps=path)
def test_get_data(path):
    path.exists.side_effect = [False, True]
    with patch.dict('os.environ', {
        'XDG_DATA_HOME': '~/.xdg/local',
        'XDG_DATA_DIRS': '/usr/share:test2',
    }):
        assert xdg_basedir.get_data('jnrbase', 'photo.jpg') == \
            '/usr/share/jnrbase/photo.jpg'
