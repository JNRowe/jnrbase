#
"""test_config - Test configuration support"""
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

from io import StringIO

from pytest import mark

from jnrbase import config
from jnrbase.context import chdir

from .utils import func_attr


@mark.parametrize('local,count', [
    (True, 4),
    (False, 3),
])
def test_config_loading(local, count, monkeypatch, path_exists_force):
    monkeypatch.setattr('builtins.open', lambda s, encoding: StringIO(''))
    monkeypatch.setenv('XDG_CONFIG_DIRS', 'test1:test2')
    cfg = config.read_configs('jnrbase', local=local)
    assert len(cfg.configs) == count
    if local:
        assert '/.jnrbaserc' in cfg.configs[-1]
    else:
        assert '/.jnrbaserc' not in cfg.configs


@func_attr('exists_result', False)
def test_config_loading_missing_files(path_exists_force):
    assert config.read_configs('jnrbase').configs == []


def test_no_colour_from_env(monkeypatch):
    monkeypatch.setenv('NO_COLOUR', 'set')
    cfg = config.read_configs('jnrbase')
    assert not cfg.colour


def test_colour_default(monkeypatch):
    monkeypatch.setattr('os.environ', {})
    cfg = config.read_configs('jnrbase')
    assert cfg.colour


def test_colour_from_config(monkeypatch):
    monkeypatch.setattr('os.environ', {})
    with chdir('tests/data/config'):
        cfg = config.read_configs('jnrbase', local=True)
    assert not cfg.colour
