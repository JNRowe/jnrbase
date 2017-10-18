#
"""test_iso_8601 - Test ISO-8601 handling functions"""
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

from datetime import datetime, timedelta, timezone

from pytest import deprecated_call, mark, raises

from jnrbase.iso_8601 import (format_datetime, format_delta, parse_datetime,
                              parse_delta)
from jnrbase._version import tuple as v_tuple


@mark.parametrize('string,expected', [
    ('2011-05-04T08:00:00Z', datetime(2011, 5, 4, 8, 0, tzinfo=timezone.utc)),
    ('2011-05-04T09:15:00Z', datetime(2011, 5, 4, 9, 15, tzinfo=timezone.utc)),
    ('2011-05-04T09:15:00', datetime(2011, 5, 4, 9, 15, tzinfo=timezone.utc)),
    ('', None),
])
def test_parse_datetime(string, expected):
    if expected is None:
        now = datetime.now(timezone.utc)
        # Ugly, but patching a built-in is uglier
        assert (parse_datetime(string) - now) < timedelta(seconds=3)
    else:
        assert parse_datetime(string) == expected


@mark.parametrize('string,expected', [
    ('2011-05-04T07:00:00-01:00', datetime(2011, 5, 4, 8, 0)),
    ('2011-05-04T12:15:00+03:00', datetime(2011, 5, 4, 9, 15)),
    ('', None),
])
def test_parse_datetime_naive(string, expected):
    with deprecated_call():
        if expected is None:
            now = datetime.utcnow()
            # Ugly, but patching a built-in is uglier
            assert (parse_datetime(string, naive=True) - now) \
                < timedelta(seconds=3)
        else:
            assert parse_datetime(string, naive=True) == expected


@mark.skipif(v_tuple < (0, 7, 0), reason='Deprecations')
def test_parse_datetime_naive_deprecation():
    parse_datetime('2011-05-04T07:00:00-01:00', naive=True)


@mark.parametrize('dt,expected', [
    (datetime(2011, 5, 4, 8, 0, tzinfo=timezone.utc), '2011-05-04T08:00:00Z'),
    (datetime(2011, 5, 4, 9, 15, tzinfo=timezone.utc), '2011-05-04T09:15:00Z'),
])
def test_format_datetime(dt, expected):
    assert format_datetime(dt) == expected


@mark.parametrize('string,expected', [
    ('PT04H30M21S', timedelta(hours=4, minutes=30, seconds=21)),
    ('PT00H12M01S', timedelta(minutes=12, seconds=1)),
    ('PT00H12M01.45S', timedelta(minutes=12, seconds=1, microseconds=45)),
    ('PT04H', timedelta(hours=4)),
    ('PT04H30M', timedelta(hours=4, minutes=30)),
    ('PT30M', timedelta(minutes=30)),
    ('PT04H21S', timedelta(hours=4, seconds=21)),
    ('PT4H', timedelta(hours=4)),
    ('P3DT04H', timedelta(days=3, hours=4)),
    ('P3D', timedelta(days=3)),
])
def test_parse_duration(string, expected):
    assert parse_delta(string) == expected


@mark.parametrize('delta,expected', [
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
])
def test_format_duration(delta, expected):
    assert format_delta(delta) == expected


def test_parse_null_duration():
    assert parse_delta('') == timedelta()


def test_parse_invalid_duration():
    with raises(ValueError, match='Unable to parse delta '):
        parse_delta('P3Dwhoops')
