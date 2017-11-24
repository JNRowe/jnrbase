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
from functools import partial, singledispatch, wraps

from .iso_8601 import (format_datetime, format_delta, parse_datetime,
                       parse_delta)


encoder = json.JSONEncoder()


@singledispatch
def json_serialise(o):
    """Custom JSON serialiser.

    This simply falls through to :meth:`~json.JSONEncoder.default` when there
    isn't a custom dispatcher register for a type.

    Args:
        o: Object to encode
    Returns:
        str: JSON-encoded string
    """
    return encoder.default(o)


@json_serialise.register(datetime.datetime)
def datetime_serialise(o):
    """JSON serialiser for ``datetime`` objects"""
    return format_datetime(o)


@json_serialise.register(datetime.timedelta)
def timedelta_serialise(o):
    """JSON serialiser for ``timedelta`` objects"""
    return format_delta(o)


def json_using_iso8601(obj):
    """Parse ISO-8601 values from JSON databases.

    See :class:`json.JSONDecoder`

    Args:
        obj: Object to decode
    """
    for k, v in obj.items():
        with suppress(TypeError, ValueError):
            obj[k] = parse_datetime(v)
        with suppress(TypeError, ValueError):
            obj[k] = parse_delta(v)
    return obj


dump = wraps(json.dump)(partial(json.dump, indent=4, default=json_serialise))
dumps = wraps(json.dumps)(partial(json.dumps, indent=4,
                                  default=json_serialise))
load = wraps(json.load)(partial(json.load, object_hook=json_using_iso8601))
loads = wraps(json.loads)(partial(json.loads, object_hook=json_using_iso8601))
