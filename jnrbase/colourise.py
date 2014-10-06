#
# coding=utf-8
"""colourise - Output colourisation support."""
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
# common use in, for example, git

from click import (echo, style)


#: Global flag to disable *all* colourisation
COLOUR = True


def _colourise(text, colour):
    """Colour text, if possible.

    :param str text: Text to colourise
    :param str colour: Colour to display text in
    :rtype: :obj:`str`
    :return str: Colourised text, if possible
    """
    if COLOUR:
        return style(text, fg=colour, bold=True)
    else:
        return text


def info(text):
    """Format an informational message.

    :param str text: Text to format
    :rtype: ``str``
    :return: Bright blue text, if possible
    """
    return _colourise(text, 'blue')


def fail(text):
    """Format a failure message.

    :param str text: Text to format
    :rtype: :obj:`str`
    :return: Bright red text, if possible
    """
    return _colourise(text, 'red')


def success(text):
    """Format a success message.

    :param str text: Text to format
    :rtype: :obj:`str`
    :return: Bright green text, if possible
    """
    return _colourise(text, 'green')


def warn(text):
    """Format a warning message.

    :param str text: Text to format
    :rtype: ``str``
    :return: Bright yellow text, if possible
    """
    return _colourise(text, 'yellow')


def pinfo(text):  # pragma: no cover
    """Pretty print an inprintional message.

    :param str text: Text to print
    :rtype: ``str``
    :return: Bright blue text, if possible
    """
    echo(info(text))


def pfail(text):  # pragma: no cover
    """Pretty print a failure message.

    :param str text: Text to print
    :rtype: :obj:`str`
    :return: Bright red text, if possible
    """
    echo(fail(text))


def psuccess(text):  # pragma: no cover
    """Pretty print a success message.

    :param str text: Text to print
    :rtype: :obj:`str`
    :return: Bright green text, if possible
    """
    echo(success(text))


def pwarn(text):  # pragma: no cover
    """Pretty print a warning message.

    :param str text: Text to print
    :rtype: ``str``
    :return: Bright yellow text, if possible
    """
    echo(warn(text))
