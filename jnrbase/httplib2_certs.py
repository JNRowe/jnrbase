#
"""httplib2_certs - httplib2 system certs finder."""
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

import sys
import warnings
from os import getenv
from pathlib import Path

import httplib2
from deprecation import deprecated

#: Allow fallback to bundled httplib2 certs.
#:
#: *Packagers*: Patch this to ``False``
ALLOW_FALLBACK = True

#: Default certificate locations for platforms
PLATFORM_FILES = {
    'linux': [
        Path('/etc/ssl/certs/ca-certificates.crt'),
        Path('/etc/pki/tls/certs/ca-bundle.crt')
    ],
    'freebsd': [
        Path('/usr/local/share/certs/ca-root-nss.crt'),
    ],
}


@deprecated(deprecated_in='1.2', removed_in='1.3',
            details='httplib2 support is being removed')
def find_certs() -> Path:
    """Find suitable certificates for ``httplib2``.

    Warning:
        The default behaviour is to fall back to the bundled certificates when
        no system certificates can be found.  If you're packaging ``jnrbase``
        *please* set ``ALLOW_FALLBACK`` to ``False`` to disable this very much
        unwanted behaviour, but please maintain the option so that downstream
        users can inspect the configuration easily.

    See also: :pypi:`httplib2`

    Returns:
        Path to SSL certificates
    Raises:
        RuntimeError: When no suitable certificates are found
    """
    bundle = Path(httplib2.CA_CERTS).parent.absolute()
    # Some distros symlink the bundled path location to the system certs
    if bundle.is_symlink():
        return bundle
    for platform, files in PLATFORM_FILES.items():
        if sys.platform.startswith(platform):
            for cert_file in files:
                if cert_file.exists():
                    return cert_file
    # An apparently common environment setting for macOS users to workaround
    # the lack of “standard” certs installation
    curl_bundle = getenv('CURL_CA_BUNDLE')
    if curl_bundle:
        return Path(curl_bundle)
    if ALLOW_FALLBACK:
        warnings.warn('No system certs detected, falling back to bundled',
                      RuntimeWarning)
        return Path(httplib2.CA_CERTS)
    else:
        raise RuntimeError('No system certs detected!')
