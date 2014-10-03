#
# coding=utf-8
"""test_git - Test git repository support"""
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
from os import path
from subprocess import CalledProcessError
from tarfile import open as open_tar

from pytest import (fixture, raises)

from jnrbase.git import find_tag


DATA_DIR = path.join(path.dirname(path.abspath(__file__)), 'data', 'git')


@fixture
def tarball_data(request, tmpdir, scope='session'):
    """Extract a tarball for test usage

    This fixture extracts a tarball using the basename from a ``tar__name``
    kwarg, and returns the path to the extracted files.
    """
    args = getargspec(request.function)
    defs = {k: v for k, v in zip(reversed(args.args), reversed(args.defaults))}
    fname = defs['tar_name']
    tar = open_tar(path.join(DATA_DIR, fname + '.tar'))
    tar.extractall(str(tmpdir))
    return str(tmpdir.join(fname))


def test_empty_repo(tarball_data, tar_name='empty'):
    with raises(CalledProcessError):
        find_tag(git_dir=tarball_data)


def test_semver_repo(tarball_data, tar_name='semver'):
    assert find_tag(git_dir=tarball_data) == 'v2.3.4'


def test_non_strict(tarball_data, tar_name='empty'):
    assert find_tag(strict=None, git_dir=tarball_data) == 'db3ed35e'


def test_custom_match(tarball_data, tar_name='funky_names'):
    assert find_tag('prefix[0-9]*', git_dir=tarball_data) == 'prefix9.8.7.6'
