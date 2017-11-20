#
"""pager - pager pipe support."""
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

import os

from subprocess import run
from warnings import warn


def pager(text, *, pager='less'):
    """Pass output through pager.

    .. deprecated:: 0.8.0

        Defaulting :envvar:`LESS` to ``FRSX`` is deprecated, and its support
        will be dropped in v0.9.0

    .. envvar:: LESS

        If unset, we use the value ``FRSX``.

        This behaviour tells less to quit if less than a single page is
        displayed, and causes the pager to display colours correctly for the
        most common setups.  See :manpage:`less(1)`, if you wish to understand
        the options fully.

    Args:
        text (str): Text to page
        pager (str): Pager to use
    """
    if pager:
        if 'less' in pager and 'LESS' not in os.environ:
            warn('Default value for $LESS has been deprecated; will be '
                 'removed in v0.9.0',
                 DeprecationWarning, 2)
            os.environ['LESS'] = 'FRSX'
        run([pager, ], input=text.encode())
    else:
        print(text)
