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

from expecter import expect
from nose2.tools import params

from jnrbase import colourise

# We only test forced styling output of blessings, as blessings handles the
# sys.stdout.isatty() flipping
colourise.TERMINAL = colourise.blessings.Terminal(force_styling=True)


@params(
    (colourise.info, u'\x1b[38;5;12mtest\x1b[m\x1b(B'),
    (colourise.fail, u'\x1b[38;5;9mtest\x1b[m\x1b(B'),
    (colourise.success, u'\x1b[38;5;10mtest\x1b[m\x1b(B'),
    (colourise.warn, u'\x1b[38;5;11mtest\x1b[m\x1b(B'),
)
def test_colouriser(f, result):
    expect(f('test')) == result
