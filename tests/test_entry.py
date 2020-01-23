#
"""test_entry - Test entry point support"""
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

from pytest import raises

from jnrbase.entry import entry_point


def test_entrypoint():
    def f():
        return 42

    f.__module__ = '__main__'
    with raises(SystemExit, match='42'):
        entry_point(f)


def test_fallthrough():
    @entry_point
    def f():
        return 42

    assert f() == 42
