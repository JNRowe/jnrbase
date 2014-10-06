#
# coding=utf-8
"""json_datetime - JSON datetime support."""
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

import datetime
import json

from functools import partial

from jnrbase.iso_8601 import (format_datetime, parse_datetime)


class DatetimeEncoder(json.JSONEncoder):

    """Custom JSON encoding for supporting ``datetime`` objects."""

    def default(self, obj):
        """Handle ``datetime`` objects when encoding as JSON.

        This simply falls through to :meth:`~json.JSONEncoder.default` if
        ``obj`` is not a ``datetime`` instance.

        :param obj: Object to encode
        """
        if isinstance(obj, datetime.datetime):
            return format_datetime(obj)
        else:
            return super(DatetimeEncoder, self).default(obj)


def json_to_datetime(obj):
    """Parse ISO-8601 values from JSON databases.

    :see: `json.JSONDecoder`

    :param obj: Object to decode
    """
    for k, v in obj.items():
        try:
            obj[k] = parse_datetime(v)
        except ValueError:
            pass
    return obj


dump = partial(json.dump, indent=4, cls=DatetimeEncoder)
dumps = partial(json.dumps, indent=4, cls=DatetimeEncoder)
load = partial(json.load, object_hook=json_to_datetime)
loads = partial(json.loads, object_hook=json_to_datetime)
