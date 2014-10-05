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

from os import getenv

from pytest import mark

from jnrbase import colourise

# We only test forced styling output of blessings, as blessings handles the
# sys.stdout.isatty() flipping
colourise.TERMINAL = colourise.blessings.Terminal(force_styling=True)


TERM = getenv('TERM')


@mark.skipif(TERM != 'linux' and not TERM.startswith('rxvt'),
             reason='Unsupported terminal type for tests')
@mark.parametrize('f, linux_result, rxvt_result', [
    (colourise.info, u'\x1b[312m', u'\x1b[38;5;12m'),
    (colourise.fail, u'\x1b[39m', u'\x1b[38;5;9m'),
    (colourise.success, u'\x1b[310m', u'\x1b[38;5;10m'),
    (colourise.warn, u'\x1b[311m', u'\x1b[38;5;11m'),
])
def test_colouriser(f, linux_result, rxvt_result):
    if TERM == 'linux':
        assert linux_result in f('test')
    elif TERM.startswith('rxvt'):
        assert rxvt_result in f('test')
