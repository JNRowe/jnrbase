#
"""json_datetime - JSON datetime support."""
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

import datetime
import json
from contextlib import suppress
from functools import partial, singledispatch, wraps
from typing import Any, Dict

from .iso_8601 import (format_datetime, format_delta, parse_datetime,
                       parse_delta)

encoder = json.JSONEncoder()  # pylint: disable=invalid-name


@singledispatch
def json_serialise(__o: Any) -> str:
    """Custom JSON serialiser.

    This simply falls through to :meth:`~json.JSONEncoder.default` when there
    isn't a custom dispatcher register for a type.

    Args:
        __o: Object to encode
    Returns:
        JSON-encoded string
    """
    return encoder.default(__o)


@json_serialise.register(datetime.datetime)
def datetime_serialise(__o: datetime.datetime) -> str:
    """JSON serialiser for ``datetime`` objects."""
    return format_datetime(__o)


@json_serialise.register(datetime.timedelta)
def timedelta_serialise(__o: datetime.timedelta) -> str:
    """JSON serialiser for ``timedelta`` objects."""
    return format_delta(__o)


def json_using_iso8601(__obj: Dict) -> Dict:
    """Parse ISO-8601 values from JSON databases.

    See :class:`json.JSONDecoder`

    Args:
        __obj: Object to decode
    """
    for key, value in __obj.items():
        with suppress(TypeError, ValueError):
            __obj[key] = parse_datetime(value)
        with suppress(TypeError, ValueError):
            __obj[key] = parse_delta(value)
    return __obj


# pylint: disable=invalid-name
dump = wraps(json.dump)(partial(json.dump, indent=4, default=json_serialise))
dumps = wraps(json.dumps)(partial(json.dumps, indent=4,
                                  default=json_serialise))
load = wraps(json.load)(partial(json.load, object_hook=json_using_iso8601))
loads = wraps(json.loads)(partial(json.loads, object_hook=json_using_iso8601))
