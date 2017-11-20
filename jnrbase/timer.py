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

from .human_time import human_timestamp


class Timing:

    """Timing context manager.

    .. versionchanged:: 0.3.0

        Renamed from ``Timer``.

    Attributes:
        verbose (bool): Print elapsed time
        elapsed (datetime.timedelta): Duration of execution
    """

    def __init__(self, *, verbose=False):
        """Configure the timing Timing context manager.

        Args:
            verbose (bool): Print elapsed time
        """
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
            print('Started {}'.format(human_timestamp(self._start)))
