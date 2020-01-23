#
"""test_httplib2_certs - Test cert locating functions"""
# Copyright © 2014-2019  James Rowe <jnrowe@gmail.com>
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

from pathlib import Path

from pytest import mark, raises, warns

from jnrbase._version import tuple as vtuple
from jnrbase import httplib2_certs

from .utils import func_attr

exists_result = lambda x: func_attr('exists_result', x)  # NOQA: E731


def test_upstream_import(path_exists_force):
    import ca_certs_locater
    assert ca_certs_locater.get() == Path('/etc/ssl/certs/ca-certificates.crt')


def test_unbundled_package_import(monkeypatch):
    monkeypatch.setattr(
        'jnrbase.httplib2_certs.Path.is_symlink', lambda p: True)
    monkeypatch.setattr('jnrbase.httplib2_certs.httplib2.CA_CERTS',
                        Path('/fixed_by_distributor/certs.crt'))
    assert httplib2_certs.find_certs() == Path('/fixed_by_distributor')


@exists_result(False)
def test_bundled(path_exists_force):
    with warns(RuntimeWarning) as record:
        httplib2_certs.find_certs()
    assert 'falling back' in record[1].message.args[0]


@exists_result(False)
def test_bundled_fail(monkeypatch, path_exists_force):
    monkeypatch.setattr('jnrbase.httplib2_certs.ALLOW_FALLBACK', False)
    with raises(RuntimeError, match='No system certs detected!'):
        httplib2_certs.find_certs()


def test_freebsd_paths(monkeypatch, path_exists_force):
    monkeypatch.setattr('sys.platform', 'freebsd')
    assert httplib2_certs.find_certs() \
        == Path('/usr/local/share/certs/ca-root-nss.crt')


@exists_result(False)
def test_freebsd_no_installed_certs(monkeypatch, path_exists_force):
    monkeypatch.setattr('sys.platform', 'freebsd')
    monkeypatch.setattr('jnrbase.httplib2_certs.ALLOW_FALLBACK', False)
    with raises(RuntimeError, match='No system certs detected!'):
        httplib2_certs.find_certs()


@mark.parametrize('file', [
    Path('/etc/ssl/certs/ca-certificates.crt'),
    Path('/etc/pki/tls/certs/ca-bundle.crt'),
])
def test_distros(file, monkeypatch):
    monkeypatch.setattr(
        'jnrbase.httplib2_certs.Path.exists', lambda p: p == file)
    assert httplib2_certs.find_certs() == file


def test_curl_bundle(monkeypatch):
    monkeypatch.setattr('jnrbase.httplib2_certs.Path.exists',
                        lambda s: s == 'silly_platform_user')
    monkeypatch.setattr('jnrbase.httplib2_certs.Path.exists', lambda p: False)
    monkeypatch.setenv('CURL_CA_BUNDLE', 'silly_platform_user')
    assert httplib2_certs.find_certs() == Path('silly_platform_user')


def test_removed():
    assert vtuple < (1, 3), 'httplib2 support should have been removed!'
