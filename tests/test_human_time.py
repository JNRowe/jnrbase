#
"""test_human_time - Test human readable time functions"""
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

from pytest import mark, raises

from jnrbase.human_time import human_timestamp, parse_timedelta


human_timestamp_examples = [
    ({'days': 365, }, 'last year'),
    ({'days': 70, }, 'about two months ago'),
    ({'days': 30, }, 'last month'),
    ({'days': 21, }, 'about three weeks ago'),
    ({'days': 4, }, 'about four days ago'),
    ({'days': 1, }, 'yesterday'),
    ({'hours': 5, }, 'about five hours ago'),
    ({'hours': 1, }, 'about an hour ago'),
    ({'minutes': 6, }, 'about six minutes ago'),
    ({'seconds': 12, }, 'about 12 seconds ago'),
    ({}, 'right now'),
]


@mark.parametrize('delta,result', human_timestamp_examples)
def test_human_timestamp(delta, result):
    now = datetime.utcnow().replace(tzinfo=timezone.utc)
    dt = now - timedelta(**delta)
    assert human_timestamp(dt) == result


@mark.parametrize('delta,result', human_timestamp_examples)
def test_human_timestamp_naive(delta, result):
    dt = datetime.utcnow() - timedelta(**delta)
    assert human_timestamp(dt) == result


@mark.parametrize('string,dt', [
    ('3h', timedelta(0, 10800)),
    ('1d', timedelta(1)),
    ('1 d', timedelta(1)),
    ('0.5 y', timedelta(182, 43200)),
    ('0.5 Y', timedelta(182, 43200)),
])
def test_parse_timedelta(string, dt):
    assert parse_timedelta(string) == dt


def test_parse_invalid_timedelta():
    with raises(ValueError, match='Invalid ‘frequency’ value'):
        parse_timedelta('1 k')
