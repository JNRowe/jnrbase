#
# coding=utf-8
"""test_debug - Test debug support"""
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

from mock import patch
from pytest import raises

from jnrbase.compat import StringIO
from jnrbase.debug import (DebugPrint, enter, exit, noisy_wrap)


@patch('sys.stdout', new_callable=StringIO)
def test_enter_no_arg(stdout):
    @enter
    def f(x, y):
        return x + y
    assert f(4, 3) == 7
    assert 'Entering <function f at ' in stdout.getvalue()


@patch('sys.stdout', new_callable=StringIO)
def test_enter_with_message(stdout):
    @enter('custom message')
    def f(x, y):
        return x + y
    assert f(4, 3) == 7
    assert 'custom message\n' in stdout.getvalue()


@patch('sys.stdout', new_callable=StringIO)
def test_exit_no_arg(stdout):
    @exit
    def f(x, y):
        return x + y
    assert f(4, 3) == 7
    assert 'Entering <function f at ' in stdout.getvalue()


@patch('sys.stdout', new_callable=StringIO)
def test_exit_with_message(stdout):
    @exit('custom message')
    def f(x, y):
        return x + y
    assert f(4, 3) == 7
    assert 'custom message\n' in stdout.getvalue()


@patch('sys.stdout', new_callable=StringIO)
def test_exit_with_failure(stdout):
    @exit('custom message')
    def f(x, y):
        raise ValueError('boom')
    with raises(ValueError):
        f(4, 3)
    assert stdout.getvalue() == 'custom message\n'


@patch('sys.stdout', new_callable=StringIO)
def test_DebugPrint(stdout):
    DebugPrint.enable()
    try:
        print "boom"
        result = stdout.getvalue()
        assert 'test_debug.py:' in result
        assert '] boom\n' in result
    finally:
        DebugPrint.disable()


@patch('sys.stdout', new_callable=StringIO)
def test_DebugPrint_decorator(stdout):
    @noisy_wrap
    def f(x):
        print "%x" % x
        print x
    f(20)
    result = stdout.getvalue()
    assert 'test_debug.py:' in result
    assert '] 14\n' in result
    assert '] 20\n' in result
