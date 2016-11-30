#
# coding=utf-8
"""i18n - Configure internationalisation support."""
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

import gettext

from os import path


def setup(pkg):
    """Configure gettext for given package.

    Args:
        pkg (module): Package to use as location for gettext files
    Returns:
        2-tuple of functions: Gettext functions for singular and plural
            translations
    """
    package_locale = path.join(path.realpath(path.dirname(pkg.__file__)),
                               'locale')
    gettext.install(pkg, package_locale)

    return gettext.gettext, gettext.ngettext
