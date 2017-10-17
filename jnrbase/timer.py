#
"""timer - Function timing support."""
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

import time


class Timing:

    """Timing context manager.

    Args:
        verbose (bool): Print elapsed time
    """

    def __init__(self, *, verbose=False):
        self.verbose = verbose
        self._start = None
        self.elapsed = None

    def __enter__(self):
        self._start = time.time()
        return self

    def __exit__(self, *args):
        end = time.time()
        self.elapsed = end - self._start
        if self.verbose:
            print('Elapsed: {} ms'.format(self.elapsed))
