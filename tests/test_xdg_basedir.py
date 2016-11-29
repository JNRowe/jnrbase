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

from functools import partial

from expecter import expect

from jnrbase import xdg_basedir

from .utils import func_attr


exists_result = partial(func_attr, 'exists_result')
getenv_result = partial(func_attr, 'getenv_result')


@getenv_result('~/.xdg/cache')
def test_cache_no_args(getenv_give_default):
    expect(xdg_basedir.user_cache('jnrbase')).contains('/.xdg/cache/jnrbase')


def test_cache_no_home(getenv_give_default):
    expect(xdg_basedir.user_cache('jnrbase')) == '/.cache/jnrbase'


def test_cache_osx(monkeypatch):
    monkeypatch.setattr(xdg_basedir.sys, 'platform', 'darwin')
    expect(xdg_basedir.user_cache('jnrbase')).contains('/Caches')


@getenv_result('~/.xdg/config')
def test_config_no_args(getenv_give_default):
    expect(xdg_basedir.user_config('jnrbase')).contains('/.xdg/config/jnrbase')


def test_config_no_home(getenv_give_default):
    expect(xdg_basedir.user_config('jnrbase')) == '/.config/jnrbase'


@getenv_result('~/.xdg/local')
def test_data_no_args(getenv_give_default):
    expect(xdg_basedir.user_data('jnrbase')).contains('/.xdg/local/jnrbase')


def test_data_no_home(getenv_give_default):
    expect(xdg_basedir.user_data('jnrbase')) == '/.local/share/jnrbase'


def test_osx_paths(monkeypatch):
    monkeypatch.setattr(xdg_basedir.sys, 'platform', 'darwin')
    expect(xdg_basedir.user_data('jnrbase')).contains(
        '/Library/Application Support/jnrbase'
    )


@exists_result(False)
def test_get_configs_all_missing(path_exists_force):
    expect(xdg_basedir.get_configs('jnrbase')) == []


def test_get_configs(path_exists_force):
    expect(len(xdg_basedir.get_configs('jnrbase'))) == 2


def test_get_configs_custom_dirs(monkeypatch, path_exists_force):
    monkeypatch.setenv('XDG_CONFIG_DIRS', 'test1:test2')
    expect(len(xdg_basedir.get_configs('jnrbase'))) == 3


def test_get_configs_osx(monkeypatch, path_exists_force):
    monkeypatch.setattr(xdg_basedir.sys, 'platform', 'darwin')
    expect(xdg_basedir.get_configs('jnrbase')[-1]).contains('/Library/')


def test_get_data(monkeypatch):
    path_results = [True, False]
    monkeypatch.setattr(xdg_basedir.path, 'exists',
                        lambda s: path_results.pop())
    monkeypatch.setenv('XDG_DATA_HOME', '~/.xdg/local')
    monkeypatch.setenv('XDG_DATA_DIRS', '/usr/share:test2')
    expect(xdg_basedir.get_data('jnrbase', 'photo.jpg')) == \
        '/usr/share/jnrbase/photo.jpg'


@exists_result(False)
def test_get_data_no_files(monkeypatch):
    with expect.raises(IOError):
        xdg_basedir.get_data('jnrbase', 'photo.jpg')
