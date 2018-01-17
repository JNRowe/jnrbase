#
"""colourise - Output colourisation support."""
# Copyright © 2014-2018  James Rowe <jnrowe@gmail.com>
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
        return style(text, fg=colour, bold=True)
    else:
        return text


def fail(text: str) -> str:
    """Format a failure message.

    Args:
        text: Text to format
    Returns:
        Bright red text, if possible
    """
    return _colourise(text, 'red')


def info(text: str) -> str:
    """Format an informational message.

    Args:
        text: Text to format
    Returns:
        Bright blue text, if possible
    """
    return _colourise(text, 'blue')


def success(text: str) -> str:
    """Format a success message.

    Args:
        text: Text to format
    Returns:
        Bright green text, if possible
    """
    return _colourise(text, 'green')


def warn(text: str) -> str:
    """Format a warning message.

    Args:
        text: Text to format
    Returns:
        Bright yellow text, if possible
    """
    return _colourise(text, 'yellow')


def pfail(text: str) -> None:  # pragma: no cover
    """Pretty print a failure message to ``stdout``.

    Args:
        text: Text to print
    """
    echo(fail(text))


def pinfo(text: str) -> None:  # pragma: no cover
    """Pretty print an informational message to ``stdout``.

    Args:
        text: Text to print
    """
    echo(info(text))


def psuccess(text: str) -> None:  # pragma: no cover
    """Pretty print a success message to ``stdout``.

    Args:
        text: Text to print
    """
    echo(success(text))


def pwarn(text: str) -> None:  # pragma: no cover
    """Pretty print a warning message to ``stdout``.

    Args:
        text: Text to print
    """
    echo(warn(text))
