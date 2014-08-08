#
# coding=utf-8
"""test_context - Test path context handlers support"""
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

from time import sleep

from expecter import expect
from mock import patch

from jnrbase.compat import StringIO
from jnrbase.timer import Timer


def test_timer():
    with Timer() as t:
        sleep(1)
    expect(t.elapsed) > 1


@patch('sys.stdout', new_callable=StringIO)
def test_verbose_timer(stdout):
    with Timer(verbose=True) as t:
        sleep(0.2)
    expect(t.elapsed) > 0.2
    expect(stdout.getvalue()).contains('Elapsed: ')
