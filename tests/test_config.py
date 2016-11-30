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
from os import path

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

from expecter import expect
from nose2.tools import params

from jnrbase.compat import text
from jnrbase.context import chdir
from jnrbase import config


@params(
    (True, 4),
    (False, 3),
)
@patch.object(path, 'exists', lambda s: True)
@patch.object(config, 'open', lambda s, encoding: StringIO(text('')))
def test_config_loading(local, count):
    with patch.dict('os.environ', {'XDG_CONFIG_DIRS': 'test1:test2'}):
        cfg = config.read_configs('jnrbase', local=local)
    expect(len(cfg.configs)) == count
    if local:
        expect(cfg.configs[-1]).contains('/.jnrbaserc')
    else:
        expect(cfg.configs).does_not_contain('/.jnrbaserc')


@patch.object(path, 'exists', lambda s: False)
def test_config_loading_missing_files():
    expect(config.read_configs('jnrbase').configs) == []


def test_no_colour_from_env():
    with patch.dict('os.environ', {'NO_COLOUR': 'set'}):
        cfg = config.read_configs('jnrbase')
    expect(cfg.colour) is False


def test_colour_default():
    with patch.dict('os.environ', clear=True):
        cfg = config.read_configs('jnrbase')
    expect(cfg.colour) is True


def test_colour_from_config():
    with chdir('tests/data/config'):
        with patch.dict('os.environ', clear=True):
            cfg = config.read_configs('jnrbase', local=True)
    expect(cfg.colour) is False
