#
"""colourise - Output colourisation support."""
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

# The colouring we use here is hopefully quite self-explanatory, and is in
# common use in, for example, git

from click import echo, style


#: Global flag to disable *all* colourisation
COLOUR = True


def _colourise(text, colour):
    """Colour text, if possible.

    Args:
        text (str): Text to colourise
        colour (str): Colour to display text in
    Returns:
        str: Colourised text, if possible
    """
    if COLOUR:
        return style(text, fg=colour, bold=True)
    else:
        return text


def fail(text):
    """Format a failure message.

    Args:
        text (str): Text to format
    Returns:
        str: Bright red text, if possible
    """
    return _colourise(text, 'red')


def info(text):
    """Format an informational message.

    Args:
        text (str): Text to format
    Returns:
        str: Bright blue text, if possible
    """
    return _colourise(text, 'blue')


def success(text):
    """Format a success message.

    Args:
        text (str): Text to format
    Returns:
        str: Bright green text, if possible
    """
    return _colourise(text, 'green')


def warn(text):
    """Format a warning message.

    Args:
        text (str): Text to format
    Returns:
        str: Bright yellow text, if possible
    """
    return _colourise(text, 'yellow')


def pfail(text):  # pragma: no cover
    """Pretty print a failure message to ``stdout``.

    Args:
        text (str): Text to print
    """
    echo(fail(text))


def pinfo(text):  # pragma: no cover
    """Pretty print an informational message to ``stdout``.

    Args:
        text (str): Text to print
    """
    echo(info(text))


def psuccess(text):  # pragma: no cover
    """Pretty print a success message to ``stdout``.

    Args:
        text (str): Text to print
    """
    echo(success(text))


def pwarn(text):  # pragma: no cover
    """Pretty print a warning message to ``stdout``.

    Args:
        text (str): Text to print
    """
    echo(warn(text))
