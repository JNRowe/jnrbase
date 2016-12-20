#
# coding=utf-8
"""test_httplib2_certs - Test cert locating functions"""
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

import warnings

from expecter import expect
from nose2.tools import params

from jnrbase import httplib2_certs

from .utils import (mock_path_exists, mock_platform, patch, patch_env)


@mock_path_exists()
def test_upstream_import():
    import ca_certs_locater
    expect(ca_certs_locater.get()) == '/etc/ssl/certs/ca-certificates.crt'


def test_unbundled_package_import():
    with patch.object(httplib2_certs.httplib2, 'CA_CERTS',
                      '/fixed_by_distributor/certs.crt'):
        expect(httplib2_certs.find_certs()) == '/fixed_by_distributor'


@mock_path_exists(False)
def test_bundled():
    with warnings.catch_warnings(record=True) as warns:
        warnings.simplefilter("always")
        httplib2_certs.find_certs()
        expect(warns[0].category) == RuntimeWarning
        expect(str(warns[0])).contains('falling back')


@mock_path_exists(False)
def test_bundled_fail():
    with patch.object(httplib2_certs, 'ALLOW_FALLBACK', False), \
         expect.raises(RuntimeError):
        httplib2_certs.find_certs()


@mock_platform('freebsd')
@mock_path_exists()
def test_freebsd_paths():
    expect(httplib2_certs.find_certs()) \
        == '/usr/local/share/certs/ca-root-nss.crt'


@mock_platform('freebsd')
@mock_path_exists(False)
def test_freebsd_no_installed_certs():
    with patch.object(httplib2_certs, 'ALLOW_FALLBACK', False), \
         expect.raises(RuntimeError):
        httplib2_certs.find_certs()


@params(
    '/etc/ssl/certs/ca-certificates.crt',
    '/etc/pki/tls/certs/ca-bundle.crt',
)
def test_distros(file):
    with patch.object(httplib2_certs.path, 'exists', lambda s: s == file):
        expect(httplib2_certs.find_certs()) == file


@mock_path_exists({'silly_platform_user': True})
def test_curl_bundle():
    with patch_env({'CURL_CA_BUNDLE': 'silly_platform_user'}):
        expect(httplib2_certs.find_certs()) == 'silly_platform_user'
