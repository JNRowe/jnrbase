#
"""test_timer - Test timer support"""
# Copyright © 2014-2017  James Rowe <jnrowe@gmail.com>
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

from contextlib import redirect_stdout
from io import StringIO

from expecter import expect
from hiro import Timeline

from jnrbase.timer import Timing


@Timeline()
def test_timing(timeline):
    with Timing() as t:
        timeline.forward(3600)
    expect(t.elapsed) >= 3600


def test_verbose_timing():
    with StringIO() as f, redirect_stdout(f):
        with Timeline() as timeline, Timing(verbose=True) as t:
            timeline.forward(3600)
        expect(t.elapsed) >= 3600
        expect(f.getvalue()).contains('Elapsed: 36')
