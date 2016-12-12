#
# coding=utf-8
"""timer - Function timing support."""
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

import time


class Timer(object):

    """Timing context manager.

    Args:
        verbose (bool): Print elapsed time
    """

    def __init__(self, verbose=False):
        self.verbose = verbose

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        end = time.time()
        self.elapsed = end - self.start
        if self.verbose:
            print('Elapsed: %f ms' % self.elapsed)
