#
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

from contextlib import redirect_stdout
from io import StringIO
from os import getenv
from subprocess import run
from tempfile import TemporaryFile

from expecter import expect

from jnrbase import pager as pager_mod
from jnrbase.pager import pager

from .utils import patch, patch_env, requires_exec


def stored_run(f):
    return lambda *args, **kwargs: run(*args, stdout=f, **kwargs)


@requires_exec('cat')
def test_pager():
    with TemporaryFile() as f:
        with patch.object(pager_mod, 'run', new=stored_run(f)):
            pager('paging through cat', pager='cat')
        f.seek(0)
        data = f.read()
        data = data.decode()
    expect(data) == 'paging through cat'


@requires_exec('less')
def test_default_less_config():
    with TemporaryFile() as f:
        with patch.object(pager_mod, 'run', new=stored_run(f)), \
             patch_env(clear=True):
            pager('pager forcibly disabled')
            expect(getenv('LESS')) == 'FRSX'


def test_disable_pager():
    with StringIO() as f, redirect_stdout(f):
        pager('pager forcibly disabled', pager=None)
        expect(f.getvalue()) == 'pager forcibly disabled\n'
