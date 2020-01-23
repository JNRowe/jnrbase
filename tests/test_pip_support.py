#
"""test_pip_support - Test pip workarounds support"""
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

from pytest import mark, raises

from jnrbase.pip_support import __eval_env, parse_requires

DATA_DIR = Path(__file__).parent / 'data' / 'pip'


def data_file(fname):
    return DATA_DIR / fname


def test_empty_parse():
    assert parse_requires(data_file('empty.txt')) == []


def test_comment_skipping():
    assert parse_requires(data_file('comments.txt')) == ['httplib2', 'lxml']


def test_include():
    assert parse_requires(data_file('base.txt')) == ['httplib2', 'lxml']


def test_abs_include():
    assert parse_requires(data_file('base_abs.txt')) == ['httplib2', 'lxml']


@mark.parametrize('version,expected', [
    ('3.3', ['contextlib2>=0.5.4', ]),
    ('3.5', []),
])
def test_parse_markers(version, expected, monkeypatch):
    monkeypatch.setitem(__eval_env, 'python_version', version)
    assert parse_requires(data_file('markers.txt')) == expected


def test_invalid_markers():
    with raises(ValueError, match='Invalid marker'):
        parse_requires(data_file('invalid_markers.txt'))
