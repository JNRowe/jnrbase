#
"""test_xdg_basedir - Test XDG basedir support."""
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

from pathlib import Path

from pytest import raises

from jnrbase import xdg_basedir

from .utils import func_attr

exists_result = lambda x: func_attr('exists_result', x)  # NOQA: E731


def test_cache_no_args(monkeypatch):
    monkeypatch.setenv('XDG_CACHE_HOME', '~/.xdg/cache')
    assert '/.xdg/cache/jnrbase' in str(xdg_basedir.user_cache('jnrbase'))


def test_cache_no_home(monkeypatch):
    monkeypatch.setattr('os.environ', {})
    monkeypatch.setattr('jnrbase.xdg_basedir.Path.home', lambda: Path('/'))
    assert xdg_basedir.user_cache('jnrbase') == Path('/.cache/jnrbase')


def test_cache_macos(monkeypatch):
    monkeypatch.setattr('sys.platform', 'darwin')
    assert '/Caches' in str(xdg_basedir.user_cache('jnrbase'))


def test_config_no_args(monkeypatch):
    monkeypatch.setenv('XDG_CONFIG_HOME', '~/.xdg/config')
    assert '/.xdg/config/jnrbase' in str(xdg_basedir.user_config('jnrbase'))


def test_config_no_home(monkeypatch):
    monkeypatch.setattr('os.environ', {})
    monkeypatch.setattr('jnrbase.xdg_basedir.Path.home', lambda: Path('/'))
    assert xdg_basedir.user_config('jnrbase') == Path('/.config/jnrbase')


def test_data_no_args(monkeypatch):
    monkeypatch.setenv('XDG_DATA_HOME', '~/.xdg/local')
    assert '/.xdg/local/jnrbase' in str(xdg_basedir.user_data('jnrbase'))


def test_data_no_home(monkeypatch):
    monkeypatch.setattr('os.environ', {})
    monkeypatch.setattr('jnrbase.xdg_basedir.Path.home', lambda: Path('/'))
    assert xdg_basedir.user_data('jnrbase') == Path('/.local/share/jnrbase')


def test_macos_paths(monkeypatch):
    monkeypatch.setattr('sys.platform', 'darwin')
    assert '/Library/Application Support/jnrbase' \
        in str(xdg_basedir.user_data('jnrbase'))


@exists_result(False)
def test_get_configs_all_missing(path_exists_force):
    assert xdg_basedir.get_configs('jnrbase') == []


def test_get_configs(path_exists_force):
    assert len(xdg_basedir.get_configs('jnrbase')) == 2


def test_get_configs_custom_dirs(monkeypatch, path_exists_force):
    monkeypatch.setenv('XDG_CONFIG_DIRS', 'test1:test2')
    assert len(xdg_basedir.get_configs('jnrbase')) == 3


def test_get_configs_macos(monkeypatch, path_exists_force):
    monkeypatch.setattr('sys.platform', 'darwin')
    assert '/Library/' in str(xdg_basedir.get_configs('jnrbase')[-1])


@exists_result([True, False])
def test_get_data(monkeypatch, path_exists_force):
    monkeypatch.setattr('jnrbase.xdg_basedir.Path.is_dir', lambda _: True)
    monkeypatch.setenv('XDG_DATA_HOME', '~/.xdg/local')
    monkeypatch.setenv('XDG_DATA_DIRS', '/usr/share:test2')
    assert xdg_basedir.get_data('jnrbase', 'photo.jpg') \
        == Path('/usr/share/jnrbase/photo.jpg')


@exists_result(False)
def test_get_data_no_files(path_exists_force):
    with raises(FileNotFoundError, match='No data file'):
        raise ValueError(xdg_basedir.get_data('jnrbase', 'photo.jpg'))
