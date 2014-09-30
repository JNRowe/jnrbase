#
# coding=utf-8
"""test_template - Test Jinja template support"""
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

from datetime import (datetime, timedelta)
from os import getenv

from blessings import Terminal
from pytest import mark

from jnrbase import template

# We only test forced styling output of blessings, as blessings handles the
# sys.stdout.isatty() flipping
template.TERMINAL = Terminal(force_styling=True)
template.TERMINAL.is_a_tty = True


def test_setup():
    env = template.setup('jnrbase')
    assert 'safe' in env.filters


def test_filter_decorator():
    @template.jinja_filter
    def test():
        return ''
    assert template.FILTERS['test'] == test


@mark.parametrize('filter,args,kwargs,expected', [
    ('regexp', ('test', 't', 'T'), {}, 'TesT'),
    ('highlight', ('f = lambda: True', ), {'lexer': 'python'},
     u'f\x1b[39;49;00m \x1b[39;49;00m=\x1b[39;49;00m '
     u'\x1b[39;49;00m\x1b[34mlambda\x1b[39;49;00m:\x1b[39;49;00m '
     u'\x1b[39;49;00m\x1b[36mTrue\x1b[39;49;00m\n'),
    ('html2text', ('<b>test</b>', ), {}, '**test**'),
    ('relative_time', (datetime.utcnow() - timedelta(days=1), ), {},
     'yesterday'),
])
def test_custom_filter(filter, args, kwargs, expected):
    env = template.setup('jnrbase')
    assert env.filters[filter](*args, **kwargs) == expected


TERM = getenv('TERM')


@mark.skipif(TERM != 'linux' and not TERM.startswith('rxvt'),
             reason='Unsupported terminal type for tests')
@mark.parametrize('filter,args,kwargs,linux_result,rxvt_result', [
    ('colourise', ('test', 'green'), {}, u'\x1b[32m', u'\x1b[38;5;2m'),
])
def test_custom_filter_term_dependent(filter, args, kwargs, linux_result,
                                      rxvt_result):
    env = template.setup('jnrbase')
    output = env.filters[filter](*args, **kwargs)
    if TERM == 'linux':
        assert linux_result in output
    elif TERM.startswith('rxvt'):
        assert rxvt_result in output
