#
# coding=utf-8
"""pager - pager pipe support."""
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

import os

from subprocess import (PIPE, Popen)

from jnrbase.compat import PY2


def pager(text, pager='less'):
    """Pass output through pager.

    Args:
        text (str): Text to page
        pager (bool): Pager to use
    """
    if pager:
        if 'less' in pager and 'LESS' not in os.environ:
            os.environ['LESS'] = 'FRSX'
        pager = Popen([pager, ], stdin=PIPE)
        if PY2:  # pragma: Python 2
            pager.communicate(text)
        else:  # pragma: Python 3
            pager.communicate(text.encode())
        pager.wait()
    else:
        print(text)
