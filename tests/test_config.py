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

from expecter import expect
from pytest import mark

from jnrbase import config
from jnrbase.context import chdir

from .utils import mock_path_exists, patch, patch_env

@mark.parametrize('local,count', [
    (True, 4),
    (False, 3),
])
@mock_path_exists()
@patch.object(config, 'open', lambda s, encoding: StringIO(''))
def test_config_loading(local, count):
    with patch_env({'XDG_CONFIG_DIRS': 'test1:test2'}):
        cfg = config.read_configs('jnrbase', local=local)
    expect(len(cfg.configs)) == count
    if local:
        expect(cfg.configs[-1]).contains('/.jnrbaserc')
    else:
        expect(cfg.configs).does_not_contain('/.jnrbaserc')


@mock_path_exists(False)
def test_config_loading_missing_files():
    expect(config.read_configs('jnrbase').configs) == []


def test_no_colour_from_env():
    with patch_env({'NO_COLOUR': 'set'}):
        cfg = config.read_configs('jnrbase')
    expect(cfg.colour) == False  # NOQA: E712


def test_colour_default():
    with patch_env(clear=True):
        cfg = config.read_configs('jnrbase')
    expect(cfg.colour) == True  # NOQA: E712


def test_colour_from_config():
    with chdir('tests/data/config'), patch_env(clear=True):
        cfg = config.read_configs('jnrbase', local=True)
    expect(cfg.colour) == False  # NOQA: E712
