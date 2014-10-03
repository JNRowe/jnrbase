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

from io import StringIO

from jnrbase.compat import text
from jnrbase import config


def test_config_loading(monkeypatch):
    monkeypatch.setattr('jnrbase.xdg_basedir.path.exists', lambda s: True)
    monkeypatch.setattr(config.path, 'exists', lambda s: True)
    monkeypatch.setattr(config, 'open', lambda s, encoding: StringIO(text('')))
    monkeypatch.setenv('XDG_CONFIG_DIRS', 'test1:test2')
    cfg = config.read_configs('jnrbase')
    assert len(cfg.configs) == 4
    assert '/.jnrbaserc' in cfg.configs[-1]


def test_config_loading_missing_files(monkeypatch):
    monkeypatch.setattr(config.path, 'exists', lambda s: False)
    assert config.read_configs('jnrbase').configs == []


def test_no_colour_from_env(monkeypatch):
    monkeypatch.setenv('NO_COLOUR', 'set')
    cfg = config.read_configs('jnrbase')
    assert cfg.colour is False


def test_colour_default(monkeypatch):
    monkeypatch.setattr('os.environ', {})
    cfg = config.read_configs('jnrbase')
    assert cfg.colour is True
