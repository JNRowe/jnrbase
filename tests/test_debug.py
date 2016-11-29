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

from jnrbase.debug import (DebugPrint, enter, exit, noisy_wrap, sys)


def test_enter_no_arg(capsys):
    @enter
    def f(x, y):
        return x + y
    expect(f(4, 3)) == 7
    out, _ = capsys.readouterr()
    expect(out).contains('Entering <function f at ')


def test_enter_with_message(capsys):
    @enter('custom message')
    def f(x, y):
        return x + y
    expect(f(4, 3)) == 7
    out, _ = capsys.readouterr()
    expect(out).contains('custom message\n')


def test_exit_no_arg(capsys):
    @exit
    def f(x, y):
        return x + y
    expect(f(4, 3)) == 7
    out, _ = capsys.readouterr()
    expect(out).contains('Entering <function f at ')


def test_exit_with_message(capsys):
    @exit('custom message')
    def f(x, y):
        return x + y
    expect(f(4, 3)) == 7
    out, _ = capsys.readouterr()
    expect(out).contains('custom message\n')


def test_exit_with_failure(capsys):
    @exit('custom message')
    def f(x, y):
        raise ValueError('boom')
    with expect.raises(ValueError):
        f(4, 3)
    out, _ = capsys.readouterr()
    expect(out) == 'custom message\n'


def test_DebugPrint(capsys):
    DebugPrint.enable()
    try:
        print "boom"
        out, _ = capsys.readouterr()
        expect(out).contains('test_debug.py:')
        expect(out).contains('] boom\n')
    finally:
        DebugPrint.disable()


def test_DebugPrint_double_enable():
    DebugPrint.enable()
    sys.stdout.first = True
    try:
        DebugPrint.enable()
        expect(sys.stdout.first) is True
    finally:
        DebugPrint.disable()



def test_DebugPrint_decorator(capsys):
    @noisy_wrap
    def f(x):
        print "%x" % x
        print x
    f(20)
    out, _ = capsys.readouterr()
    expect(out).contains('test_debug.py:')
    expect(out).contains('] 14\n')
    expect(out).contains('] 20\n')
