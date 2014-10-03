#
# coding=utf-8
"""conftest - Configuration for tests"""
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

from inspect import getargspec

from pytest import fixture


@fixture
def getenv_give_default(request, monkeypatch, scope='session'):
    """Force result of module's ``getenv`` function

    This fixture returns the ``getenv`` fallback by default, but a custom value
    can be specified by setting the ``getenv_result`` kwarg for a test.
    """
    args = getargspec(request.function)
    result = None
    if args.defaults:
        defs = {k: v for k, v in zip(reversed(args.args),
                                     reversed(args.defaults))}
        result = lambda k, d: defs.get('getenv_result')
    if not result:
        result = lambda k, d: d
    tmod = 'jnrbase.%s' % request.module.__name__.replace('tests.test_', '')
    monkeypatch.setattr('.'.join([tmod, 'getenv']), result)


@fixture
def path_exists_force(request, monkeypatch, scope='session'):
    """Force result of module's ``path.exists`` function

    This fixture returns ``True`` by default, but a custom value can be
    specified by setting the ``exists_result`` kwarg for a test.
    """
    args = getargspec(request.function)
    result = True
    if args.defaults:
        defs = {k: v for k, v in zip(reversed(args.args),
                                     reversed(args.defaults))}
        result = defs.get('exists_result', result)
    tmod = 'jnrbase.%s' % request.module.__name__.replace('tests.test_', '')
    monkeypatch.setattr('.'.join([tmod, 'path', 'exists']), lambda s: result)
