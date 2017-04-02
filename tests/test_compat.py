#
# coding=utf-8
"""test_compat - Test Python 2/3 compatibility support"""
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
from nose2.tools import params

from jnrbase.compat import (PY2, mangle_repr_type, safe_hasattr, text)


def test_mangle_repr_type():
    @mangle_repr_type
    class Test(object):
        def __repr__(self):
            return text("test")
    # This works on Python 2 or 3 by design
    expect(repr(Test())).isinstance(str)


@params(
    (tuple(), 'count', True),
    (tuple(), 'no_exist', False),
)
def test_safe_hasattr(obj, attr, expected):
    expect(safe_hasattr(obj, attr)) == expected


def test_break_hasattr():
    class Funky:
        @property
        def break_hasattr(self):
            raise ValueError()

    with expect.raises(ValueError):
        safe_hasattr(Funky(), 'break_hasattr')
    if PY2:  # pragma: Python 2
        expect(hasattr(Funky(), 'break_hasattr')) == False
    else:  # pragma: Python 3
        with expect.raises(ValueError):
            hasattr(Funky(), 'break_hasattr')
