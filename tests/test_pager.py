#
# coding=utf-8
"""test_pager - Test pager piping support"""
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

from os import getenv
from subprocess import Popen
from tempfile import TemporaryFile

from expecter import expect

from jnrbase.compat import PY2
from jnrbase.pager import pager
from jnrbase import pager as pager_mod

from .utils import (mock_stdout, patch, patch_env, requires_exec)


def stored_popen(f):
    return lambda *args, **kwargs: Popen(*args, stdout=f, **kwargs)


@requires_exec('cat')
def test_pager():
    with TemporaryFile() as f:
        with patch.object(pager_mod, 'Popen', new=stored_popen(f)):
            pager('paging through cat', 'cat')
        f.seek(0)
        data = f.read()
    if not PY2:  # pragma: Python 3
        data = data.decode()
    expect(data) == 'paging through cat'


@requires_exec('less')
def test_default_less_config():
    with TemporaryFile() as f:
        with patch.object(pager_mod, 'Popen', new=stored_popen(f)):
            with patch_env(clear=True):
                pager('pager forcibly disabled')
                expect(getenv('LESS')) == 'FRSX'


@mock_stdout
def test_disable_pager(stdout):
    pager('pager forcibly disabled', None)
    expect(stdout.getvalue()) == 'pager forcibly disabled\n'
