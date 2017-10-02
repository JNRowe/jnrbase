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

from os import getcwd
from re import escape

from pytest import raises

from jnrbase import context


def test_chdir():
    orig = getcwd()
    with context.chdir('tests'):
        assert getcwd != orig
    assert getcwd() == orig


def test_chdir_missing():
    with raises(FileNotFoundError, match=escape('[Errno 2]')), \
            context.chdir('missing_dir'):
        pass
