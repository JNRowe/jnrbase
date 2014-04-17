#
# coding=utf-8
"""colourise - Output colourisation support"""
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

# The colouring we use here is hopefully quite self-explanatory, and is in
# common use in for example git

import blessings

TERMINAL = blessings.Terminal()


def _colourise(text, colour):
    """Colour text, if possible.

    :param str text: Text to colourise
    :param str colour: Colour to display text in
    :rtype: :obj:`str`
    :return str: Colourised text, if possible
    """
    return getattr(TERMINAL, colour.replace(' ', '_'))(text)


def info(text):
    """Pretty print an informational message.

    :param str text: Text to format
    :rtype: ``str``
    :return: Bright blue text, if possible
    """
    return _colourise(text, 'bright blue')


def fail(text):
    """Pretty print a failure message.

    :param str text: Text to format
    :rtype: :obj:`str`
    :return: Bright red text, if possible
    """
    return _colourise(text, 'bright red')


def success(text):
    """Pretty print a success message.

    :param str text: Text to format
    :rtype: :obj:`str`
    :return: Bright green text, if possible
    """
    return _colourise(text, 'bright green')


def warn(text):
    """Pretty print a warning message.

    :param str text: Text to format
    :rtype: ``str``
    :return: Bright yellow text, if possible
    """
    return _colourise(text, 'bright yellow')
