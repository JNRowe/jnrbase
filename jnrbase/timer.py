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

from datetime import datetime

from jnrbase.human_time import human_timestamp


class Timing:

    """Timing context manager.

    Args:
        human_format (bool): Use humanised output
        verbose (bool): Print elapsed time
    """

    def __init__(self, *, human_format=True, verbose=False):
        self.human_format = human_format
        self.verbose = verbose
        self._start = None
        self.elapsed = None

    def __enter__(self):
        self._start = datetime.utcnow()
        return self

    def __exit__(self, *args):
        now = datetime.utcnow()
        self.elapsed = now - self._start
        if self.verbose:
            if self.human_format:
                print('Started {}'.format(human_timestamp(self._start)))
            else:
                print('Elapsed: {}'.format(self.elapsed))
