#
# coding=utf-8
"""httplib2_certs - httplib2 system certs finder."""
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

import sys
import warnings

from os import (getenv, path)

import httplib2


#: Allow fallback to bundled httplib2 certs.
#:
#: *Packagers*: Set this to ``False``
ALLOW_FALLBACK = True

#: Default certificate locations for platforms
PLATFORM_FILES = {
    'linux': ['/etc/ssl/certs/ca-certificates.crt',
              '/etc/pki/tls/certs/ca-bundle.crt'],
    'freebsd': ['/usr/local/share/certs/ca-root-nss.crt', ],
}


def find_certs():
    """Find suitable certificates for ``httplib2``.

    .. warning::

        The default behaviour is to fall back to the bundled certificates when
        no system certificates can be found.  If you're packaging ``jnrbase``
        *please* set ``ALLOW_FALLBACK`` to ``False`` to disable this very much
        unwanted behaviour, but please maintain the option so that downstream
        users can inspect the configuration easily.

    See: :pypi:`httplib2`

    Returns:
        str: Path to SSL certificates
    Raises:
        RuntimeError: When no suitable certificates are found
    """
    bundle = path.realpath(path.dirname(httplib2.CA_CERTS))
    # Some distros symlink the bundled path location to the system certs
    if not bundle.startswith(path.realpath(path.dirname(httplib2.__file__))):
        return bundle
    for platform, files in PLATFORM_FILES.items():
        if sys.platform.startswith(platform):
            for cert_file in files:
                if path.exists(cert_file):
                    return cert_file
    # An apparently common environment setting for macOS users to workaround
    # the lack of "standard" certs installation
    if path.exists(getenv('CURL_CA_BUNDLE', '')):
        return getenv('CURL_CA_BUNDLE')
    if ALLOW_FALLBACK:
        warnings.warn('No system certs detected, falling back to bundled',
                      RuntimeWarning)
        return httplib2.CA_CERTS
    else:
        raise RuntimeError('No system certs detected!')
