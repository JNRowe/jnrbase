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

from expecter import expect
from mock import patch
from pytest import mark

from jnrbase import httplib2_certs


@patch('jnrbase.httplib2_certs.path.exists')
def test_upstream_import(exists):
    exists.return_value = True
    import ca_certs_locater
    expect(ca_certs_locater.get()) == '/etc/ssl/certs/ca-certificates.crt'


@patch('jnrbase.httplib2_certs.path.exists')
def test_bundled(exists):
    exists.return_value = False
    with warnings.catch_warnings(record=True) as warns:
        warnings.simplefilter("always")
        httplib2_certs.find_certs()
        expect(warns[0].category) == RuntimeWarning
        expect(str(warns[0].message)).contains('falling back')


@patch('jnrbase.httplib2_certs.path.exists')
def test_bundled_fail(exists):
    httplib2_certs.ALLOW_FALLBACK = False
    exists.return_value = False
    with expect.raises(RuntimeError):
        httplib2_certs.find_certs()
    httplib2_certs.ALLOW_FALLBACK = True


@mark.parametrize('file', [
    '/etc/ssl/certs/ca-certificates.crt',
    '/etc/pki/tls/certs/ca-bundle.crt',
])
@patch('jnrbase.httplib2_certs.path.exists')
def test_distros(file, exists):
    exists.side_effect = lambda s: s == file
    expect(httplib2_certs.find_certs()) == file


@patch('jnrbase.httplib2_certs.path.exists')
def test_curl_bundle(exists):
    exists.side_effect = lambda s: s == 'silly_platform_user'
    with patch.dict('os.environ', {'CURL_CA_BUNDLE': 'silly_platform_user'}):
        expect(httplib2_certs.find_certs()) == 'silly_platform_user'
