#
"""test_context - Test path context handlers support"""
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

from os import getcwd, getenv
from re import escape
from subprocess import PIPE, run

from pytest import raises

from jnrbase import context


def test_chdir(tmpdir):
    orig = getcwd()
    dir_ = tmpdir.join('new').mkdir()
    with context.chdir(dir_):
        assert getcwd() == dir_
    assert getcwd() == orig


def test_chdir_missing(tmpdir):
    with raises(FileNotFoundError, match=escape('[Errno 2]')), \
            context.chdir(tmpdir.join('missing_dir').strpath):
        pass


def test_env_override():
    assert getenv('SHELL') != 'hello'
    with context.env(SHELL='hello'):
        assert getenv('SHELL') == 'hello'
    assert getenv('SHELL') != 'hello'


def test_env_unset():
    assert getenv('SHELL')
    with context.env(SHELL=None):
        assert getenv('SHELL') is None
    assert getenv('SHELL')


def test_env_subshell_support():
    assert getenv('NOT_SET') is None
    with context.env(NOT_SET='hello'):
        out = run(['printenv', ], stdout=PIPE, encoding='utf-8').stdout
        assert 'NOT_SET=hello' in out.splitlines()
    assert getenv('NOT_SET') is None
