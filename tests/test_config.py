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

from functools import partial
from io import StringIO

from expecter import expect
from pytest import mark

from jnrbase.compat import text
from jnrbase.context import chdir
from jnrbase import config

from .utils import func_attr

exists_result = partial(func_attr, 'exists_result')


@mark.parametrize('local, count', [
    (True, 4),
    (False, 3),
])
@exists_result(True)
def test_config_loading(local, count, monkeypatch):
    monkeypatch.setattr('jnrbase.xdg_basedir.path.exists', lambda s: True)
    monkeypatch.setattr(config, 'open', lambda s, encoding: StringIO(text('')))
    monkeypatch.setenv('XDG_CONFIG_DIRS', 'test1:test2')
    cfg = config.read_configs('jnrbase', local=local)
    expect(len(cfg.configs)) == count
    if local:
        expect(cfg.configs[-1]).contains('/.jnrbaserc')
    else:
        expect(cfg.configs).does_not_contain('/.jnrbaserc')


@exists_result(False)
def test_config_loading_missing_files(monkeypatch):
    expect(config.read_configs('jnrbase').configs) == []


def test_no_colour_from_env(monkeypatch):
    monkeypatch.setenv('NO_COLOUR', 'set')
    cfg = config.read_configs('jnrbase')
    expect(cfg.colour) is False


def test_colour_default(monkeypatch):
    monkeypatch.setattr('os.environ', {})
    cfg = config.read_configs('jnrbase')
    expect(cfg.colour) is True


def test_colour_from_config(monkeypatch):
    with chdir('tests/data/config'):
        monkeypatch.setattr('os.environ', {})
        cfg = config.read_configs('jnrbase', local=True)
        expect(cfg.colour) is False
