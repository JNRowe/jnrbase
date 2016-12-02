#
# coding=utf-8
"""test_iso_8601 - Test ISO-8601 handling functions"""
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

from datetime import (datetime, timedelta)
from unittest import TestCase

from expecter import expect
from nose2.tools import params

from jnrbase.iso_8601 import (format_datetime, format_delta, parse_datetime,
                              parse_delta, utc)


class UtcTest(TestCase):
    def test__repr__(self):
        expect(repr(utc)) == 'UTC()'

    def test_offset(self):
        expect(str(utc.utcoffset(None))) == '0:00:00'

    def test_name(self):
        expect(utc.tzname(None)) == 'UTC'


@params(
    ('2011-05-04T08:00:00Z', datetime(2011, 5, 4, 8, 0, tzinfo=utc)),
    ('2011-05-04T09:15:00Z', datetime(2011, 5, 4, 9, 15, tzinfo=utc)),
    ('', None),
)
def test_parse_datetime(string, expected):
    if expected is None:
        now = datetime.utcnow().replace(tzinfo=utc)
        # Ugly, but patching a built-in is uglier
        expect(parse_datetime(string) - now) < timedelta(seconds=3)
    else:
        expect(parse_datetime(string)) == expected


@params(
    (datetime(2011, 5, 4, 8, 0, tzinfo=utc), '2011-05-04T08:00:00Z'),
    (datetime(2011, 5, 4, 9, 15, tzinfo=utc), '2011-05-04T09:15:00Z'),
)
def test_format_datetime(dt, expected):
    expect(format_datetime(dt)) == expected


@params(
    ('PT04H30M21S', timedelta(hours=4, minutes=30, seconds=21)),
    ('PT00H12M01S', timedelta(minutes=12, seconds=1)),
    ('PT04H', timedelta(hours=4)),
    ('PT04H30M', timedelta(hours=4, minutes=30)),
    ('PT30M', timedelta(minutes=30)),
    ('PT04H21S', timedelta(hours=4, seconds=21)),
    ('PT4H', timedelta(hours=4)),
    ('P3DT04H', timedelta(days=3, hours=4)),
    ('P3D', timedelta(days=3)),
)
def test_parse_duration(string, expected):
    expect(parse_delta(string)) == expected


@params(
    (timedelta(hours=4, minutes=30, seconds=21), 'PT04H30M21S'),
    (timedelta(minutes=12, seconds=1), 'PT12M01S'),
    (timedelta(), ''),
    (timedelta(days=3, hours=4), 'P3DT04H'),
    (timedelta(days=3), 'P3D'),
    (timedelta(days=2, hours=22), 'P2DT22H'),
    (timedelta(hours=4), 'PT04H'),
    (timedelta(hours=4, minutes=30), 'PT04H30M'),
    (timedelta(minutes=30), 'PT30M'),
    (timedelta(hours=4, seconds=21), 'PT04H21S'),
)
def test_format_duration(delta, expected):
    expect(format_delta(delta)) == expected


def test_parse_null_duration():
    expect(parse_delta('')) == timedelta()
