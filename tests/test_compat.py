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

from subprocess import CalledProcessError
from sys import version_info

from expecter import expect

from jnrbase import compat

from .utils import patch


def test_mangle_repr_type():
    @compat.mangle_repr_type
    class Test(object):
        def __repr__(self):
            return compat.text("test")
    # This works on Python 2 or 3 by design
    expect(repr(Test())).isinstance(str)


def test_check_output():
    expect(compat.check_output(['echo', 'hello'])) == 'hello\n'


def test_check_output_py26_compat():
    if version_info[:2] == (2, 6):
        expect(compat.check_output(['echo', 'hello'])) == 'hello\n'
    else:
        with patch('subprocess.check_output', side_effect=AttributeError):
            expect(compat.check_output(['echo', 'hello'])) == 'hello\n'


def test_check_output_py26_compat_fail():
    if version_info[:2] == (2, 6):
        with expect.raises(CalledProcessError):
            compat.check_output(['false', ])
    else:
        with patch('subprocess.check_output', side_effect=AttributeError):
            with expect.raises(CalledProcessError):
                compat.check_output(['false', ])
