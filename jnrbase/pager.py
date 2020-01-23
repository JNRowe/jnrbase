#
"""pager - pager pipe support."""
# Copyright © 2014-2018  James Rowe <jnrowe@gmail.com>
#
# SPDX-License-Identifier: GPL-3.0-or-later
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

from subprocess import run
from typing import Optional


# pylint: disable=redefined-outer-name
def pager(__text: str, *, pager: Optional[str] = 'less'):
    """Pass output through pager.

    See :manpage:`less(1)`, if you wish to configure the default pager.  For
    example, you may wish to check ``FRSX`` options.

    Args:
        __text: Text to page
        pager: Pager to use
    """
    if pager:
        run([
            pager,
        ], input=__text.encode())
    else:
        print(__text)
