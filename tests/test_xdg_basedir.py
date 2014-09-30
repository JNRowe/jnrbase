#
"""test_xdg_basedir - Test XDG basedir support"""
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

from pytest import raises

from jnrbase import xdg_basedir

from .utils import mock_path_exists, mock_platform, patch_env


def test_cache_no_args():
    with patch_env({'XDG_CACHE_HOME': '~/.xdg/cache'}):
        assert '/.xdg/cache/jnrbase' in xdg_basedir.user_cache('jnrbase')


def test_cache_no_home():
    with patch_env(clear=True):
        assert xdg_basedir.user_cache('jnrbase') == '/.cache/jnrbase'


@mock_platform()
def test_cache_macos():
    assert '/Caches' in xdg_basedir.user_cache('jnrbase')


def test_config_no_args():
    with patch_env({'XDG_CONFIG_HOME': '~/.xdg/config'}):
        assert '/.xdg/config/jnrbase' in xdg_basedir.user_config('jnrbase')


def test_config_no_home():
    with patch_env(clear=True):
        assert xdg_basedir.user_data('jnrbase') == '/.local/share/jnrbase'


def test_data_no_args():
    with patch_env({'XDG_DATA_HOME': '~/.xdg/local'}):
        assert '/.xdg/local/jnrbase' in xdg_basedir.user_data('jnrbase')


def test_data_no_home():
    with patch_env(clear=True):
        assert xdg_basedir.user_data('jnrbase') == '/.local/share/jnrbase'


@mock_platform()
def test_macos_paths():
    assert '/Library/Application Support/jnrbase' \
        in xdg_basedir.user_data('jnrbase')


@mock_path_exists(False)
def test_get_configs_all_missing():
    assert xdg_basedir.get_configs('jnrbase') == []


@mock_path_exists()
def test_get_configs():
    assert len(xdg_basedir.get_configs('jnrbase')) == 2


@mock_path_exists()
def test_get_configs_custom_dirs():
    with patch_env({'XDG_CONFIG_DIRS': 'test1:test2'}):
        assert len(xdg_basedir.get_configs('jnrbase')) == 3


@mock_platform()
@mock_path_exists()
def test_get_configs_macos():
    assert '/Library/' in xdg_basedir.get_configs('jnrbase')[-1]


@mock_path_exists([True, False])
def test_get_data():
    with patch_env({'XDG_DATA_HOME': '~/.xdg/local',
                    'XDG_DATA_DIRS': '/usr/share:test2'}):
        assert xdg_basedir.get_data('jnrbase', 'photo.jpg') \
            == '/usr/share/jnrbase/photo.jpg'


@mock_path_exists(False)
def test_get_data_no_files():
    with expect.raises(FileNotFoundError):
    with raises(FileNotFoundError, match='No data file'):
        xdg_basedir.get_data('jnrbase', 'photo.jpg')
