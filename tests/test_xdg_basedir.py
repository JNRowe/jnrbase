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

import os

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

from expecter import expect

from jnrbase import xdg_basedir


def test_cache_no_args():
    with patch.dict('os.environ', {'XDG_CACHE_HOME': '~/.xdg/cache'}):
        expect(xdg_basedir.user_cache('jnrbase')).contains(
            '/.xdg/cache/jnrbase'
        )


def test_cache_no_home():
    with patch.dict('os.environ', clear=True):
        expect(xdg_basedir.user_cache('jnrbase')) == '/.cache/jnrbase'


def test_cache_osx():
    with patch.object(xdg_basedir.sys, 'platform', 'darwin'):
        expect(xdg_basedir.user_cache('jnrbase')).contains('/Caches')


def test_config_no_args():
    with patch.dict('os.environ', {'XDG_CONFIG_HOME': '~/.xdg/config'}):
        expect(xdg_basedir.user_config('jnrbase')).contains(
            '/.xdg/config/jnrbase'
        )


def test_config_no_home():
    with patch.dict('os.environ', clear=True):
        expect(xdg_basedir.user_config('jnrbase')) == '/.config/jnrbase'


def test_data_no_args():
    with patch.dict('os.environ', {'XDG_DATA_HOME': '~/.xdg/local'}):
        expect(xdg_basedir.user_data('jnrbase')).contains(
            '/.xdg/local/jnrbase'
        )


def test_data_no_home():
    with patch.dict('os.environ', clear=True):
        expect(xdg_basedir.user_data('jnrbase')) == '/.local/share/jnrbase'


def test_osx_paths():
    with patch.object(xdg_basedir.sys, 'platform', 'darwin'):
        expect(xdg_basedir.user_data('jnrbase')).contains(
            '/Library/Application Support/jnrbase'
        )


@patch.object(os.path, 'exists', lambda s: False)
def test_get_configs_all_missing():
    expect(xdg_basedir.get_configs('jnrbase')) == []


@patch.object(os.path, 'exists', lambda s: True)
def test_get_configs():
    expect(len(xdg_basedir.get_configs('jnrbase'))) == 2


@patch.object(os.path, 'exists', lambda s: True)
def test_get_configs_custom_dirs():
    with patch.dict('os.environ', {'XDG_CONFIG_DIRS': 'test1:test2'}):
        expect(len(xdg_basedir.get_configs('jnrbase'))) == 3


@patch.object(os.path, 'exists', lambda s: True)
def test_get_configs_osx():
    with patch.object(xdg_basedir.sys, 'platform', 'darwin'):
        expect(xdg_basedir.get_configs('jnrbase')[-1]).contains('/Library/')


@patch.object(os.path, 'exists')
def test_get_data(exists):
    path_results = [True, False]
    exists.side_effect = lambda s: path_results.pop()
    with patch.dict('os.environ', {'XDG_DATA_HOME': '~/.xdg/local'}):
        with patch.dict('os.environ', {'XDG_DATA_DIRS': '/usr/share:test2'}):
            expect(xdg_basedir.get_data('jnrbase', 'photo.jpg')) == \
                '/usr/share/jnrbase/photo.jpg'


@patch.object(os.path, 'exists', lambda s: False)
def test_get_data_no_files():
    with expect.raises(IOError):
        xdg_basedir.get_data('jnrbase', 'photo.jpg')
