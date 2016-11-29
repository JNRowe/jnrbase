#
# coding=utf-8
"""test_httplib2_certs - Test cert locating functions"""
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

import warnings

from functools import partial

from expecter import expect
from pytest import mark

from jnrbase import httplib2_certs

from .utils import func_attr


exists_result = partial(func_attr, 'exists_result')


def test_upstream_import(path_exists_force):
    import ca_certs_locater
    expect(ca_certs_locater.get()) == '/etc/ssl/certs/ca-certificates.crt'


def test_unbundled_package_import(monkeypatch):
    monkeypatch.setattr('httplib2.CA_CERTS', '/fixed_by_distributor/certs.crt')
    expect(httplib2_certs.find_certs()) == '/fixed_by_distributor'


@exists_result(False)
def test_bundled(path_exists_force):
    with warnings.catch_warnings(record=True) as warns:
        warnings.simplefilter("always")
        httplib2_certs.find_certs()
        expect(warns[0].category) == RuntimeWarning
        expect(str(warns[0].message)).contains('falling back')


@exists_result(False)
def test_bundled_fail(path_exists_force, monkeypatch):
    monkeypatch.setattr(httplib2_certs, 'ALLOW_FALLBACK', False)
    with expect.raises(RuntimeError):
        httplib2_certs.find_certs()


def test_freebsd_paths(monkeypatch, path_exists_force):
    monkeypatch.setattr('sys.platform', 'freebsd')
    expect(httplib2_certs.find_certs()) \
        == '/usr/local/share/certs/ca-root-nss.crt'


@exists_result(False)
def test_freebsd_no_installed_certs(monkeypatch, path_exists_force):
    monkeypatch.setattr(httplib2_certs, 'ALLOW_FALLBACK', False)
    monkeypatch.setattr('sys.platform', 'freebsd')
    with expect.raises(RuntimeError):
        httplib2_certs.find_certs()


@mark.parametrize('file', [
    '/etc/ssl/certs/ca-certificates.crt',
    '/etc/pki/tls/certs/ca-bundle.crt',
])
def test_distros(monkeypatch, file):
    monkeypatch.setattr(httplib2_certs.path, 'exists', lambda s: s == file)
    expect(httplib2_certs.find_certs()) == file


def test_curl_bundle(monkeypatch):
    monkeypatch.setattr(httplib2_certs.path, 'exists',
                        lambda s: s == 'silly_platform_user')
    monkeypatch.setenv('CURL_CA_BUNDLE', 'silly_platform_user')
    expect(httplib2_certs.find_certs()) == 'silly_platform_user'
