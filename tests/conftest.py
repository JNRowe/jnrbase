#
"""conftest - Configuration for tests."""
# Copyright © 2014-2020  James Rowe <jnrowe@gmail.com>
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

from pytest import fixture


def _get_module(request):
    modbase = request.module.__name__.replace('tests.test_', '')
    return f'jnrbase.{modbase}'


@fixture
def path_exists_force(request, monkeypatch):
    """Force result of module's ``Path.exists`` method.

    This fixture returns ``True`` by default, but a custom value can be
    specified by setting the ``exists_result`` attribute on a test function.
    If the ``exists_result`` attribute is a list it returns items in
    :abbr:`LIFO (Last In First Out)` order on each call.
    """
    result = getattr(request.function, 'exists_result', True)
    if isinstance(result, list):
        func = lambda _: result.pop()  # NOQA: E731
    else:
        func = lambda _: result  # NOQA: E731
    monkeypatch.setattr('.'.join([_get_module(request), 'Path', 'exists']),
                        func)
