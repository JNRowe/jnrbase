#
"""test_json_datetime - Test JSON datetime functions"""
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

from datetime import datetime, timezone

from pytest import raises

from jnrbase import json_datetime


def test_json_no_datetime():
    class Test:
        pass
    data = {'test': Test()}
    with raises(TypeError, match='not JSON serializable'):
        json_datetime.dumps(data, indent=None)


def test_json_datetime():
    data = {'test': datetime(2014, 2, 3, 18, 12, tzinfo=timezone.utc)}
    assert json_datetime.dumps(data, indent=None) == \
        '{"test": "2014-02-03T18:12:00Z"}'


def test_deep_json_datetime():
    data = {'test': [{'test2': datetime(2014, 2, 3, 18, 12,
                                        tzinfo=timezone.utc)}, ]}
    assert json_datetime.dumps(data, indent=None) == \
        '{"test": [{"test2": "2014-02-03T18:12:00Z"}]}'


def test_json_load_no_datetime():
    data = '{"test": "not a datetime"}'
    assert json_datetime.loads(data) == {'test': 'not a datetime'}


def test_roundtrip():
    data = {'test': datetime(2014, 2, 3, 18, 12, tzinfo=timezone.utc)}
    json = json_datetime.dumps(data, indent=None)
    assert json_datetime.loads(json) == data
