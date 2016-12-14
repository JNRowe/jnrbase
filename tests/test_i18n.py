#
# coding=utf-8
"""test_i18n - Test i18n setup functions"""
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

from expecter import expect

from jnrbase import i18n

# This needs a *real* test suite, but its usage necessitates bundling a heap of
# test data and patching practically everything to make it work.


def test_translation_config():
    _, N_ = i18n.setup(i18n)
    expect(_.__name__) == 'gettext'
    expect(N_.__name__) == 'ngettext'
