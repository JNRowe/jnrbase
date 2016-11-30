#
# coding=utf-8
"""test_context - Test path context handlers support"""
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

from os import getcwd

from expecter import expect

from jnrbase import context


def test_chdir():
    orig = getcwd()
    with context.chdir('tests'):
        expect(getcwd) != orig
    expect(getcwd()) == orig


def test_chdir_missing():
    with expect.raises(OSError):
        with context.chdir('missing_dir'):
            pass
