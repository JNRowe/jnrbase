#
# coding=utf-8
"""test_timer - Test timer support"""
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

from hiro import Timeline

from jnrbase.timer import Timer


@Timeline()
def test_timer(timeline):
    with Timer() as t:
        timeline.forward(3600)
    assert t.elapsed >= 3600


def test_verbose_timer(capsys):
    with Timeline() as timeline:
        with Timer(verbose=True) as t:
            timeline.forward(3600)
    assert t.elapsed >= 3600
    out, _ = capsys.readouterr()
    assert 'Elapsed: 36' in out
