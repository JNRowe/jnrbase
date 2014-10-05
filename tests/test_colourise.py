#
# coding=utf-8
"""test_colourise - Test colourisation functions"""
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

from pytest import mark

from jnrbase import colourise


@mark.parametrize('f,expected', [
    (colourise.info, u'\x1b[34m\x1b[1m'),
    (colourise.fail, u'\x1b[31m\x1b[1m'),
    (colourise.success, u'\x1b[32m\x1b[1m'),
    (colourise.warn, u'\x1b[33m\x1b[1m'),
])
def test_colouriser(f, expected):
    assert expected in f('test')


def test_disabled_colouriser(monkeypatch):
    monkeypatch.setattr(colourise, 'COLOUR', False)
    assert colourise.info('test') == 'test'
