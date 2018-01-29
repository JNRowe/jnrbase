#
"""test_cmdline - Test command line functionality support"""
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
#
# SPDX-License-Identifier: GPL-3.0+

from shutil import which

from click.testing import CliRunner
from pytest import mark

from jnrbase.cmdline import cli


pytestmark = mark.skipif(not which('git'), reason='Requires git')


@mark.parametrize('type_', ['fail', 'info', 'success', 'warn'])
def test_messages(type_):
    runner = CliRunner()
    result = runner.invoke(cli, ['messages', type_, 'test str'])
    if type_ == 'fail':
        assert result.exit_code == 1
    else:
        assert result.exit_code == 0
    assert 'test str' in result.output
