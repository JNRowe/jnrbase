#
"""test_git - Test git repository support"""
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

from contextlib import contextmanager
from os import path
from shutil import which
from subprocess import CalledProcessError
from tarfile import open as open_tar
from tempfile import TemporaryDirectory

from pytest import mark, raises

from jnrbase.git import find_tag

pytestmark = mark.skipif(not which('git'), reason='Requires git')


@contextmanager
def tarball_data(tar_name):
    """Extract a tarball for test usage

    This fixture extracts a tarball, and returns the path to the extracted
    files.

    :see: `tar_name`
    """
    data_dir = path.join(path.dirname(__file__), 'data', 'git')
    with open_tar(path.join(data_dir, tar_name + '.tar'), 'r:') as tar:
        with TemporaryDirectory() as temp_dir:
            tar.extractall(temp_dir)
            yield str(path.join(temp_dir, tar_name))


def test_empty_repo():
    with tarball_data('empty') as tree, \
            raises(CalledProcessError, match='status 128'):
        find_tag(git_dir=tree)


def test_semver_repo():
    with tarball_data('semver') as tree:
        assert find_tag(git_dir=tree) == 'v2.3.4'


def test_non_strict():
    with tarball_data('empty') as tree:
        assert find_tag(strict=None, git_dir=tree) == 'db3ed35e8734'


def test_custom_match():
    with tarball_data('funky_names') as tree:
        assert find_tag('prefix[0-9]*', git_dir=tree) == 'prefix9.8.7.6'
