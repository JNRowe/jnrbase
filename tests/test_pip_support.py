#
# coding=utf-8
"""test_pip_support - Test pip workarounds support"""
# Copyright © 2014-2016  James Rowe <jnrowe@gmail.com>
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

from os import path

from expecter import expect

from jnrbase.pip_support import parse_requires


DATA_DIR = path.join(path.dirname(path.abspath(__file__)), 'data', 'pip')


def data_file(fname):
    return path.join(DATA_DIR, fname)


def test_empty_parse():
    expect(parse_requires(data_file('empty.txt'))) == []


def test_comment_skipping():
    expect(parse_requires(data_file('comments.txt'))) == ['httplib2', 'lxml']


def test_include():
    expect(parse_requires(data_file('base.txt'))) == ['httplib2', 'lxml']


def test_abs_include():
    expect(parse_requires(data_file('base_abs.txt'))) == ['httplib2', 'lxml']
