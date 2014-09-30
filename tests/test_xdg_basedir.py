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

from jnrbase import xdg_basedir


def test_cache_no_args(monkeypatch):
    monkeypatch.setattr(xdg_basedir, 'getenv', lambda k, d: '~/.xdg/cache')
    assert '/.xdg/cache/jnrbase' in xdg_basedir.user_cache('jnrbase')


def test_cache_no_home(monkeypatch):
    monkeypatch.setattr(xdg_basedir, 'getenv', lambda k, d: d)
    assert xdg_basedir.user_cache('jnrbase') == '/.cache/jnrbase'


def test_config_no_args(monkeypatch):
    monkeypatch.setattr(xdg_basedir, 'getenv', lambda k, d: '~/.xdg/config')
    assert '/.xdg/config/jnrbase' in xdg_basedir.user_config('jnrbase')


def test_config_no_home(monkeypatch):
    monkeypatch.setattr(xdg_basedir, 'getenv', lambda k, d: d)
    assert xdg_basedir.user_config('jnrbase') == '/.config/jnrbase'


def test_data_no_args(monkeypatch):
    monkeypatch.setattr(xdg_basedir, 'getenv', lambda k, d: '~/.xdg/local')
    assert '/.xdg/local/jnrbase' in xdg_basedir.user_data('jnrbase')


def test_data_no_home(monkeypatch):
    monkeypatch.setattr(xdg_basedir, 'getenv', lambda k, d: d)
    assert xdg_basedir.user_data('jnrbase') == '/.local/share/jnrbase'


def test_osx_paths(monkeypatch):
    monkeypatch.setattr(xdg_basedir.sys, 'platform', 'darwin')
    assert '/Library/Application Support/jnrbase' in \
        xdg_basedir.user_data('jnrbase')


def test_get_configs_all_missing(monkeypatch):
    monkeypatch.setattr(xdg_basedir.path, 'exists', lambda s: False)
    assert xdg_basedir.get_configs('jnrbase') == []


def test_get_configs(monkeypatch):
    monkeypatch.setattr(xdg_basedir.path, 'exists', lambda s: True)
    assert len(xdg_basedir.get_configs('jnrbase')) == 2


def test_get_configs_custom_dirs(monkeypatch):
    monkeypatch.setattr(xdg_basedir.path, 'exists', lambda s: True)
    monkeypatch.setenv('XDG_CONFIG_DIRS', 'test1:test2')
    assert len(xdg_basedir.get_configs('jnrbase')) == 3


def test_get_configs_osx(monkeypatch):
    monkeypatch.setattr(xdg_basedir.sys, 'platform', 'darwin')
    monkeypatch.setattr(xdg_basedir.path, 'exists', lambda s: True)
    assert '/Library/' in xdg_basedir.get_configs('jnrbase')[-1]


def test_get_data(monkeypatch):
    path_results = [True, False]
    monkeypatch.setattr(xdg_basedir.path, 'exists',
                        lambda s: path_results.pop())
    monkeypatch.setenv('XDG_DATA_HOME', '~/.xdg/local')
    monkeypatch.setenv('XDG_DATA_DIRS', '/usr/share:test2')
    assert xdg_basedir.get_data('jnrbase', 'photo.jpg') == \
        '/usr/share/jnrbase/photo.jpg'
