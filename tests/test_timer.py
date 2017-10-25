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

from datetime import timedelta

from hiro import Timeline

from jnrbase.timer import Timing


def test_timing():
    with Timeline() as timeline, Timing() as t:
        timeline.forward(3600)
    assert t.elapsed >= timedelta(hours=1)


def test_verbose_timing(capsys):
    with Timeline() as timeline, Timing(verbose=True) as t:
        timeline.forward(3600)
    assert t.elapsed >= timedelta(hours=1)
    assert 'Started about an hour ago' in capsys.readouterr()[0]
