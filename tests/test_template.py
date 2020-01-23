#
"""test_template - Test Jinja template support"""
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

from datetime import datetime, timedelta

from pytest import mark

from jnrbase import template


def test_setup():
    env = template.setup('jnrbase')
    assert 'safe' in env.filters


def test_filter_decorator():
    @template.jinja_filter
    def test():
        return ''

    assert template.FILTERS['test'] == test


@mark.parametrize('filter_,args,kwargs,expected', [
    ('colourise', ('test', 'green'), {}, '\x1b[32mtest\x1b[0m'),
    ('regexp', ('test', 't', 'T'), {}, 'TesT'),
    ('highlight', ('f = lambda: True', ), {
        'lexer': 'python'
    }, 'f = \x1b[34mlambda\x1b[39;49;00m: \x1b[36mTrue\x1b[39;49;00m\n'),
    ('html2text', ('<b>test</b>', ), {}, '**test**'),
    ('relative_time',
     (datetime.utcnow() - timedelta(days=1), ), {}, 'yesterday'),
])
def test_custom_filter(filter_, args, kwargs, expected, monkeypatch):
    monkeypatch.setattr('sys.stdout.isatty', lambda: True)
    env = template.setup('jnrbase')
    assert env.filters[filter_](*args, **kwargs) == expected


@mark.parametrize('filter_,args,kwargs,expected', [
    ('colourise', ('test', 'green'), {}, 'test'),
    ('highlight', ('f = lambda: True', ), {
        'lexer': 'python'
    }, 'f = lambda: True'),
])
def test_custom_filter_fallthrough(filter_, args, kwargs, expected):
    env = template.setup('jnrbase')
    assert env.filters[filter_](*args, **kwargs) == expected
