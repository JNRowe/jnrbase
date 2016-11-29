#
# coding=utf-8
"""test_pager - Test pager piping support"""
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

from os import getenv

from expecter import expect

from jnrbase.pager import pager


def test_pager(capfd):
    pager('paging through cat', 'cat')
    out, _ = capfd.readouterr()
    expect(out) == 'paging through cat'


def test_default_less_config(monkeypatch):
    monkeypatch.delenv('LESS', False)

    class FakePopen:
        def __init__(self, *args, **kwargs):
            pass

        def communicate(self, *args):
            pass

        def wait(self):
            pass

    monkeypatch.setattr('jnrbase.pager.Popen', FakePopen)
    pager('pager forcibly disabled')
    expect(getenv('LESS')) == 'FRSX'


def test_disable_pager(capsys):
    pager('pager forcibly disabled', None)
    out, _ = capsys.readouterr()
    expect(out) == 'pager forcibly disabled\n'
