#
"""i18n - Configure internationalisation support."""
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

import gettext

from os import path


def setup(pkg):
    """Configure gettext for given package.

    Args:
        pkg (types.ModuleType): Package to use as location for
            :program:`gettext` files
    Returns:
        tuple: 2-tuple of :program:`gettext` functions for singular and plural
            translations

    """
    package_locale = path.join(path.dirname(pkg.__file__), 'locale')
    gettext.install(pkg.__name__, package_locale)

    return gettext.gettext, gettext.ngettext
