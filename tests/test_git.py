#
# coding=utf-8
"""test_git - Test git repository support"""
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

from contextlib import (closing, contextmanager)
from os import path
from shutil import rmtree
from subprocess import CalledProcessError
from tarfile import open as open_tar
from tempfile import mkdtemp

from expecter import expect

from jnrbase.git import find_tag

from .utils import requires_exec

requires_git = requires_exec('git')


@contextmanager
def tarball_data(tar_name):
    """Extract a tarball for test usage

    This fixture extracts a tarball, and returns the path to the extracted
    files.

    :see: `tar_name`
    """
    data_dir = path.join(path.dirname(path.abspath(__file__)), 'data', 'git')
    with closing(open_tar(path.join(data_dir, tar_name + '.tar'))) as tar:
        try:
            temp_dir = mkdtemp()
            tar.extractall(temp_dir)
            yield str(path.join(temp_dir, tar_name))
        finally:
            rmtree(temp_dir)


@requires_git
def test_empty_repo():
    with tarball_data('empty') as tree, expect.raises(CalledProcessError):
        find_tag(git_dir=tree)


@requires_git
def test_semver_repo():
    with tarball_data('semver') as tree:
        expect(find_tag(git_dir=tree)) == 'v2.3.4'


@requires_git
def test_non_strict():
    with tarball_data('empty') as tree:
        expect(find_tag(strict=None, git_dir=tree)) == 'db3ed35e8734'


@requires_git
def test_custom_match():
    with tarball_data('funky_names') as tree:
        expect(find_tag('prefix[0-9]*', git_dir=tree)) == 'prefix9.8.7.6'
