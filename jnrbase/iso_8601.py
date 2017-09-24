#
"""iso_8601 - ISO-8601 support."""
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

import datetime
import re

import ciso8601


def parse_delta(string):
    """Parse ISO-8601 duration string.

    Args:
        string (str): Duration string to parse
    Returns:
        datetime.timedelta: Parsed delta object
    """
    if not string:
        return datetime.timedelta(0)
    match = re.fullmatch(r"""
        P
        ((?P<days>\d+)D)?
        T?
        ((?P<hours>\d{1,2})H)?
        ((?P<minutes>\d{1,2})M)?
        ((?P<seconds>\d{1,2})?((?:\.(?P<microseconds>\d+))?S)?)
    """, string, re.VERBOSE)
    match_dict = dict((k, int(v) if v else 0)
                      for k, v in match.groupdict().items())
    return datetime.timedelta(**match_dict)


def format_delta(timedelta_):
    """Format ISO-8601 duration string.

    Args:
        timedelta_ (datetime.timedelta): Duration to process
    Returns:
        str: ISO-8601 representation of duration
    """
    if timedelta_ == datetime.timedelta(0):
        return ''
    days = '{}D'.format(timedelta_.days) if timedelta_.days else ''
    hours, minutes = divmod(timedelta_.seconds, 3600)
    minutes, seconds = divmod(minutes, 60)
    hours = '{:02d}H'.format(hours) if hours else ''
    minutes = '{:02d}M'.format(minutes) if minutes else ''
    seconds = '{:02d}S'.format(seconds) if seconds else ''
    return 'P{}{}{}{}{}'.format(days,
                                'T' if hours or minutes or seconds else '',
                                hours, minutes, seconds)


def parse_datetime(string, *, naive=False):
    """Parse ISO-8601 datetime string.

    Args:
        string (str): Datetime string to parse
        naive (bool): Use naïve datetimes
    Returns:
        datetime.datetime: Parsed datetime object
    """
    if not string:
        datetime_ = datetime.datetime.now(datetime.timezone.utc)
    else:
        datetime_ = ciso8601.parse_datetime(string)
        if not datetime_:
            raise ValueError('Unable to parse timestamp {!r}'.format(string))
    if naive is True and datetime_.tzinfo:
        datetime_ = datetime_.astimezone(datetime.timezone.utc)
        datetime_ = datetime_.replace(tzinfo=None)
    elif naive is False and datetime_.tzinfo is None:
        datetime_ = datetime_.replace(tzinfo=datetime.timezone.utc)
    return datetime_


def format_datetime(datetime_):
    """Format ISO-8601 datetime string.

    Args:
        datetime_ (datetime.datetime): Datetime to process
    Returns:
        str: ISO-8601 compatible string
    """
    # Can't call isoformat method as it uses the +00:00 form
    return datetime_.strftime('%FT%TZ')
