#
# coding=utf-8
"""attrdict - Dictionary with attribute access"""
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


class AttrDict(dict):

    """Dictionary with attribute access.

    .. seealso:: :obj:`dict`
    """

    def __contains__(self, key):
        """Check for item membership

        :param object key: Key to test for
        :rtype: :obj:`bool`
        """
        return hasattr(self, key) or super(AttrDict, self).__contains__(key)

    def __getattr__(self, key):
        """Support item access via dot notation

        :param object key: Key to fetch
        """
        try:
            return self[key]
        except KeyError:
            raise AttributeError(key)

    def __setattr__(self, key, value):
        """Support item assignment via dot notation

        :param object key: Key to set value for
        :param object value: Value to set key to
        """
        try:
            self[key] = value
        except:
            raise AttributeError(key)

    def __delattr__(self, key):
        """Support item deletion via dot notation

        :param object key: Key to delete
        """
        try:
            del self[key]
        except KeyError:
            raise AttributeError(key)


class ROAttrDict(AttrDict):
    """Read-only dictionary with attribute access.

    .. seealso:: :obj:`AttrDict`
    """

    def __setitem__(self, *args):
        raise AttributeError('%r is read-only' % self.__class__.__name__)
    __delattr__ = __delitem__ = __setattr__ = __setitem__
