#
"""test_debug - Test debug support"""
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

from operator import add

from pytest import mark, raises

from jnrbase.debug import DebugPrint, noisy_wrap, on_enter, on_exit, sys


@mark.parametrize('ftype', [
    on_enter,
    on_exit,
])
def test_decorator_no_message(ftype, capsys):
    @ftype
    def func(x, y):
        return x + y

    assert func(4, 3) == 7
    assert "{}ing 'func'({!r})".format(ftype.__name__[3:].capitalize(),
                                       func.__closure__[0].cell_contents) \
        in capsys.readouterr()[0]


@mark.parametrize('ftype', [
    on_enter,
    on_exit,
])
def test_decorator_with_message(ftype, capsys):
    assert ftype('custom message')(add)(4, 3) == 7
    assert 'custom message' in capsys.readouterr()[0]


@mark.parametrize('ftype', [
    on_enter,
    on_exit,
])
def test_decorator_with_failure(ftype, capsys):
    @ftype('custom message')
    def func(x, y):
        raise ValueError('boom')

    with raises(ValueError):
        func(4, 3)
    assert capsys.readouterr()[0] == 'custom message\n'


def test_DebugPrint(capsys):  # NOQA: N802
    DebugPrint.enable()
    try:
        print('boom')
        out, _ = capsys.readouterr()
        assert 'test_debug.py:' in out
        assert '] boom\n' in out
    finally:
        DebugPrint.disable()


def test_DebugPrint_no_stack_frame(capsys, monkeypatch):  # NOQA: N802
    monkeypatch.setattr('jnrbase.debug.inspect.currentframe', lambda: None)
    DebugPrint.enable()
    try:
        print('boom')
        assert 'unknown:000] boom\n' in capsys.readouterr()[0]
    finally:
        DebugPrint.disable()


def test_DebugPrint_double_toggle():  # NOQA: N802
    DebugPrint.enable()
    sys.stdout.first = True
    try:
        DebugPrint.enable()
        assert sys.stdout.first
    finally:
        DebugPrint.disable()
    assert not hasattr(sys.stdout, 'first')
    DebugPrint.disable()


def test_DebugPrint_decorator(capsys):  # NOQA: N802
    @noisy_wrap
    def func(x):
        print(hex(x))
        print(x)

    func(20)
    out, _ = capsys.readouterr()
    assert 'test_debug.py:' in out
    assert '] 0x14\n' in out
    assert '] 20\n' in out
