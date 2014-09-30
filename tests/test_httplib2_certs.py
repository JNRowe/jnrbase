#
"""test_httplib2_certs - Test cert locating functions"""
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

import warnings

from pytest import mark, raises

from jnrbase import httplib2_certs


def test_upstream_import(monkeypatch):
    monkeypatch.setattr('os.path.exists', lambda s: True)
    import ca_certs_locater
    assert ca_certs_locater.get() == '/etc/ssl/certs/ca-certificates.crt'


def test_unbundled_package_import(monkeypatch):
    monkeypatch.setattr(httplib2_certs.httplib2, 'CA_CERTS',
                        '/fixed_by_distributor/certs.crt')
    assert httplib2_certs.find_certs() == '/fixed_by_distributor'


def test_bundled(monkeypatch):
    monkeypatch.setattr('os.path.exists', lambda s: False)
    with warnings.catch_warnings(record=True) as warns:
        warnings.simplefilter('always')
        httplib2_certs.find_certs()
        assert warns[0].category == RuntimeWarning
        assert 'falling back' in str(warns[0])


def test_bundled_fail(monkeypatch):
    monkeypatch.setattr('os.path.exists', lambda s: False)
    monkeypatch.setattr(httplib2_certs, 'ALLOW_FALLBACK', False)
    with raises(RuntimeError, message='No system certs detected!'):
        httplib2_certs.find_certs()


def test_freebsd_paths(monkeypatch):
    monkeypatch.setattr('os.path.exists', lambda s: True)
    monkeypatch.setattr('sys.platform', 'freebsd')
    assert httplib2_certs.find_certs() \
        == '/usr/local/share/certs/ca-root-nss.crt'


def test_freebsd_no_installed_certs(monkeypatch):
    monkeypatch.setattr('os.path.exists', lambda s: False)
    monkeypatch.setattr('sys.platform', 'freebsd')
    monkeypatch.setattr(httplib2_certs, 'ALLOW_FALLBACK', False)
    with raises(RuntimeError, message='No system certs detected!'):
        httplib2_certs.find_certs()


@mark.parametrize('file', [
    '/etc/ssl/certs/ca-certificates.crt',
    '/etc/pki/tls/certs/ca-bundle.crt',
])
def test_distros(file, monkeypatch):
    monkeypatch.setattr(httplib2_certs.path, 'exists', lambda s: s == file)
    assert httplib2_certs.find_certs() == file


def test_curl_bundle(monkeypatch):
    monkeypatch.setattr('os.path.exists', lambda s: s == 'silly_platform_user')
    monkeypatch.setenv('CURL_CA_BUNDLE', 'silly_platform_user')
    assert httplib2_certs.find_certs() == 'silly_platform_user'
