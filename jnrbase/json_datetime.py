#
"""json_datetime - JSON datetime support."""
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

import datetime
import json

from contextlib import suppress
from functools import partial, wraps

from .iso_8601 import format_datetime, parse_datetime


class DatetimeEncoder(json.JSONEncoder):

    """Custom JSON encoding for supporting ``datetime`` objects."""

    def default(self, o):
        """Handle ``datetime`` objects when encoding as JSON.

        This simply falls through to :meth:`~json.JSONEncoder.default` if
        ``obj`` is not a ``datetime`` instance.

        Args:
            obj: Object to encode
        """
        if isinstance(o, datetime.datetime):
            return format_datetime(o)
        else:
            return super(DatetimeEncoder, self).default(o)


def json_to_datetime(obj):
    """Parse ISO-8601 values from JSON databases.

    See :class:`json.JSONDecoder`

    Args:
        obj: Object to decode
    """
    for k, v in obj.items():
        with suppress(ValueError):
            obj[k] = parse_datetime(v)
    return obj


dump = wraps(json.dump)(partial(json.dump, indent=4, cls=DatetimeEncoder))
dumps = wraps(json.dumps)(partial(json.dumps, indent=4, cls=DatetimeEncoder))
load = wraps(json.load)(partial(json.load, object_hook=json_to_datetime))
loads = wraps(json.loads)(partial(json.loads, object_hook=json_to_datetime))
