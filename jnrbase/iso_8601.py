#
# coding=utf-8
"""iso_8601 - ISO-8601 support"""
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
import re

from . import compat


@compat.mangle_repr_type
class UTC(datetime.tzinfo):

    """UTC timezone object."""

    def __repr__(self):
        return 'UTC()'

    # pylint: disable-msg=W0613
    def utcoffset(self, datetime_):
        return datetime.timedelta(0)

    def dst(self, datetime_):
        return datetime.timedelta(0)

    def tzname(self, datetime_):
        return 'UTC'
    # pylint: enable-msg=W0613

utc = UTC()


def parse_delta(string):
    """Parse ISO-8601 duration string.

    :param str string: Duration string to parse
    :rtype: :obj:`datetime.timedelta`
    :return: Parsed delta object
    """
    if not string:
        return datetime.timedelta(0)
    match = re.match("""
        P
        ((?P<days>\d+)D)?
        T?
        ((?P<hours>\d{1,2})H)?
        ((?P<minutes>\d{1,2})M)?
        ((?P<seconds>\d{1,2})?(\.(?P<microseconds>\d+)S)?)
    """, string, re.VERBOSE)
    match_dict = dict((k, int(v) if v else 0)
                      for k, v in match.groupdict().items())
    return datetime.timedelta(**match_dict)  # pylint: disable-msg=W0142


def format_delta(timedelta_):
    """Format ISO-8601 duration string.

    :param datetime.timedelta timedelta_: Duration to process
    :rtype: :obj:`str`
    :return: ISO-8601 representation of duration
    """
    if timedelta_ == datetime.timedelta(0):
        return ''
    days = '%dD' % timedelta_.days if timedelta_.days else ''
    hours, minutes = divmod(timedelta_.seconds, 3600)
    minutes, seconds = divmod(minutes, 60)
    hours = '%02dH' % hours if hours else ''
    minutes = '%02dM' % minutes if minutes else ''
    seconds = '%02dS' % seconds if seconds else ''
    return 'P%s%s%s%s%s' % (days, 'T' if hours or minutes or seconds else '',
                            hours, minutes, seconds)


def parse_datetime(string):
    """Parse ISO-8601 datetime string.

    :param str string: Datetime string to parse
    :rtype: :obj:`datetime.datetime`
    :return: Parsed datetime object
    """
    if not string:
        datetime_ = datetime.utcnow()
    else:
        datetime_ = datetime.datetime.strptime(string, '%Y-%m-%dT%H:%M:%SZ')
        datetime_ = datetime_.replace(tzinfo=utc)
    return datetime_


def format_datetime(datetime_):
    """Format ISO-8601 datetime string.

    :param datetime.datetime datetime_: Datetime to process
    :rtype: str
    :return: ISO-8601 compatible string
    """
    # Can't call isoformat method as it uses the +00:00 form
    return datetime_.strftime('%Y-%m-%dT%H:%M:%SZ')
