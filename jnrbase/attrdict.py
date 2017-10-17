#
"""attrdict - Dictionary with attribute access."""
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


class AttrDict(dict):

    """Dictionary with attribute access.

    See also: :obj:`dict`
    """

    def __contains__(self, key):
        """Check for item membership.

        Args:
            key (object): Key to test for
        Returns:
            bool: ``True``, if item in AttrDict
        """
        return hasattr(self, key)

    def __getattr__(self, key):
        """Support item access via dot notation.

        Args:
            key (object): Key to fetch
        """
        try:
            return self[key]
        except KeyError:
            raise AttributeError(key)

    def __setattr__(self, key, value):
        """Support item assignment via dot notation.

        Args:
            key (object): Key to set value for
            value (object): Value to set key to
        """
        try:
            self[key] = value
        except Exception as err:
            raise AttributeError(str(err))

    def __delattr__(self, key):
        """Support item deletion via dot notation.

        Args:
            key (object): Key to delete
        """
        try:
            del self[key]
        except TypeError as err:
            raise AttributeError(str(err))


class ROAttrDict(AttrDict):

    """Read-only dictionary with attribute access.

    See also: :obj:`AttrDict`
    """

    def __setitem__(self, *args):
        """Handle attempt to modify read-only dictionary.

        Raises:
            AttributeError: On modification attempt
        """
        raise AttributeError('{!r} is read-only'.format(self.__class__))
    __delattr__ = __delitem__ = __setattr__ = __setitem__
