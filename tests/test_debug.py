#
"""test_debug - Test debug support"""
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

from contextlib import redirect_stdout
from expecter import expect
from io import StringIO

from jnrbase.debug import (DebugPrint, enter, exit, noisy_wrap, sys)
from jnrbase import debug as debug_mod

from .utils import patch


def test_enter_no_arg():
    @enter
    def func(x, y):
        return x + y
    with StringIO() as f, redirect_stdout(f):
        expect(func(4, 3)) == 7
        expect(f.getvalue()).contains(
            "Entering 'func'({!r})".format(func.__closure__[0].cell_contents))


def test_enter_with_message():
    @enter('custom message')
    def func(x, y):
        return x + y
    with StringIO() as f, redirect_stdout(f):
        expect(func(4, 3)) == 7
        expect(f.getvalue()).contains('custom message\n')


def test_exit_no_arg():
    @exit
    def func(x, y):
        return x + y
    with StringIO() as f, redirect_stdout(f):
        expect(func(4, 3)) == 7
        expect(f.getvalue()).contains(
            "Exiting 'func'({!r})".format(func.__closure__[0].cell_contents))


def test_exit_with_message():
    @exit('custom message')
    def func(x, y):
        return x + y
    with StringIO() as f, redirect_stdout(f):
        expect(func(4, 3)) == 7
        expect(f.getvalue()).contains('custom message\n')


def test_exit_with_failure():
    @exit('custom message')
    def func(x, y):
        raise ValueError('boom')
    with StringIO() as f, redirect_stdout(f):
        with expect.raises(ValueError):
            func(4, 3)
        expect(f.getvalue()) == 'custom message\n'


def test_DebugPrint():
    with StringIO() as f, redirect_stdout(f):
        DebugPrint.enable()
        try:
            print("boom")
            out = f.getvalue()
            expect(out).contains('test_debug.py:')
            expect(out).contains('] boom\n')
        finally:
            DebugPrint.disable()


@patch.object(debug_mod.inspect, 'currentframe', lambda: None)
def test_DebugPrint_no_stack_frame():
    with StringIO() as f, redirect_stdout(f):
        DebugPrint.enable()
        try:
            print("boom")
            expect(f.getvalue()).contains('unknown:000] boom\n')
        finally:
            DebugPrint.disable()


def test_DebugPrint_double_enable():
    with StringIO() as f, redirect_stdout(f):
        DebugPrint.enable()
        sys.stdout.first = True
        try:
            DebugPrint.enable()
            expect(sys.stdout.first) is True
        finally:
            DebugPrint.disable()


def test_DebugPrint_decorator():
    @noisy_wrap
    def func(x):
        print(hex(x))
        print(x)
    with StringIO() as f, redirect_stdout(f):
        func(20)
        out = f.getvalue()
    expect(out).contains('test_debug.py:')
    expect(out).contains('] 0x14\n')
    expect(out).contains('] 20\n')
