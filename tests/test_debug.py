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

from expecter import expect
from mock import patch

from jnrbase.compat import StringIO
from jnrbase.debug import (DebugPrint, enter, exit, noisy_wrap)


@patch('sys.stdout', new_callable=StringIO)
def test_enter_no_arg(stdout):
    @enter
    def f(x, y):
        return x + y
    expect(f(4, 3)) == 7
    expect(stdout.getvalue()).contains('Entering <function f at ')


@patch('sys.stdout', new_callable=StringIO)
def test_enter_with_message(stdout):
    @enter('custom message')
    def f(x, y):
        return x + y
    expect(f(4, 3)) == 7
    expect(stdout.getvalue()) == 'custom message\n'


@patch('sys.stdout', new_callable=StringIO)
def test_exit_no_arg(stdout):
    @exit
    def f(x, y):
        return x + y
    expect(f(4, 3)) == 7
    expect(stdout.getvalue()).contains('Entering <function f at ')


@patch('sys.stdout', new_callable=StringIO)
def test_exit_with_message(stdout):
    @exit('custom message')
    def f(x, y):
        return x + y
    expect(f(4, 3)) == 7
    expect(stdout.getvalue()) == 'custom message\n'


@patch('sys.stdout', new_callable=StringIO)
def test_exit_with_failure(stdout):
    @exit('custom message')
    def f(x, y):
        raise ValueError('boom')
    with expect.raises(ValueError):
        f(4, 3)
    expect(stdout.getvalue()) == 'custom message\n'


@patch('sys.stdout', new_callable=StringIO)
def test_DebugPrint(stdout):
    DebugPrint.enable()
    try:
        print "boom"
        result = stdout.getvalue()
        expect(result).contains('test_debug.py:')
        expect(result).contains('] boom\n')
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
    expect(result).contains('test_debug.py:')
    expect(result).contains('] 14\n')
    expect(result).contains('] 20\n')
