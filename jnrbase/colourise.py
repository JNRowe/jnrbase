#
"""colourise - Output colourisation support."""
# Copyright © 2014-2018  James Rowe <jnrowe@gmail.com>
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

# The colouring we use here is hopefully quite self-explanatory, and is in
# common use in, for example, git

from click import echo, style

#: Global flag to disable *all* colourisation
COLOUR = True


def _colourise(text: str, colour: str) -> str:
    """Colour text, if possible.

    Args:
        text: Text to colourise
        colour: Colour to display text in
    Returns:
        Colourised text, if possible
    """
    if COLOUR:
        text = style(text, fg=colour, bold=True)
    return text


def fail(__text: str) -> str:
    """Format a failure message.

    Args:
        __text: Text to format
    Returns:
        Bright red text, if possible
    """
    return _colourise(__text, 'red')


def info(__text: str) -> str:
    """Format an informational message.

    Args:
        __text: Text to format
    Returns:
        Bright blue text, if possible
    """
    return _colourise(__text, 'blue')


def success(__text: str) -> str:
    """Format a success message.

    Args:
        __text: Text to format
    Returns:
        Bright green text, if possible
    """
    return _colourise(__text, 'green')


def warn(__text: str) -> str:
    """Format a warning message.

    Args:
        __text: Text to format
    Returns:
        Bright yellow text, if possible
    """
    return _colourise(__text, 'yellow')


def pfail(__text: str) -> None:
    """Pretty print a failure message to ``stderr``.

    Args:
        __text: Text to print
    """
    echo(fail(__text), err=True)


def pinfo(__text: str) -> None:
    """Pretty print an informational message to ``stdout``.

    Args:
        __text: Text to print
    """
    echo(info(__text))


def psuccess(__text: str) -> None:
    """Pretty print a success message to ``stdout``.

    Args:
        __text: Text to print
    """
    echo(success(__text))


def pwarn(__text: str) -> None:
    """Pretty print a warning message to ``stderr``.

    Args:
        __text: Text to print
    """
    echo(warn(__text), err=True)
