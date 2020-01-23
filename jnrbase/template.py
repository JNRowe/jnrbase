#
"""template - Jinja templating support."""
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

import re
import sys
from datetime import datetime
from os import path
from typing import Callable, Union

import html2text as html2
import jinja2
from click import style
from pygments import highlight as pyg_highlight
from pygments.formatters import get_formatter_by_name
from pygments.lexers import get_lexer_by_name

from . import xdg_basedir
from .human_time import human_timestamp

#: Collection of custom filters to add to Jinja environment
FILTERS = {}  # type: Dict[str, Callable]


def jinja_filter(__func: Callable) -> Callable:
    """Simple decorator to add a new filter to Jinja environment.

    See also: :obj:`FILTERS`

    Args:
        __func: Function to add to Jinja environment
    Returns:
        Unmodified function
    """
    FILTERS[__func.__name__] = __func

    return __func


@jinja_filter
def colourise(__text: str, *args, **kwargs) -> str:
    """Colourise text using click’s style function.

    Returns text untouched if colour output is not enabled, or ``stdout`` is
    not a tty.

    See :func:`click.style` for parameters

    Args:
        __text: Text to colourise
    Returns:
        Colourised text, when possible
    """
    if sys.stdout.isatty():
        __text = style(__text, *args, **kwargs)
    return __text


@jinja_filter
def highlight(__text: str, *, lexer: str = 'diff',
              formatter: str = 'terminal') -> str:
    """Highlight text highlighted using ``pygments``.

    Returns text untouched if colour output is not enabled.

    See also: :pypi:`Pygments`

    Args:
        __text: Text to highlight
        lexer: Jinja lexer to use
        formatter: Jinja formatter to use
    Returns:
        Syntax highlighted output, when possible
    """
    if sys.stdout.isatty():
        lexer = get_lexer_by_name(lexer)
        formatter = get_formatter_by_name(formatter)
        __text = pyg_highlight(__text, lexer, formatter)
    return __text


@jinja_filter
def html2text(__html: str,
              *,
              width: int = 80,
              ascii_replacements: bool = False) -> str:
    """HTML to plain text renderer.

    See also: :pypi:`html2text`

    Args:
        __html: Text to process
        width: Paragraph width
        ascii_replacements: Use pseudo-ASCII replacements for Unicode
    Returns:
        Rendered text
    """
    html2.BODY_WIDTH = width
    html2.UNICODE_SNOB = ascii_replacements
    return html2.html2text(__html).strip()


@jinja_filter
def regexp(__string: str,
           __pattern: str,
           __repl: Union[Callable, str],
           *,
           count: int = 0,
           flags: int = 0) -> str:
    """Jinja filter for regexp replacements.

    See :func:`re.sub` for documentation.

    Returns:
        Text with substitutions applied
    """
    return re.sub(__pattern, __repl, __string, count, flags)


@jinja_filter
def relative_time(__timestamp: datetime) -> str:
    """Format a relative time.

    See :func:`~jnrbase.human_time.human_timestamp`

    Args:
        __timestamp: Event to generate relative timestamp against
    Returns:
        Human readable date and time offset
    """
    return human_timestamp(__timestamp)


def setup(__pkg: str) -> jinja2.Environment:
    """Configure a new Jinja environment with our filters.

    Args:
        __pkg: Package name to use as base for templates searches
    Returns:
        Configured Jinja environment
    """
    dirs = [
        path.join(d, 'templates') for d in xdg_basedir.get_data_dirs(__pkg)
    ]

    env = jinja2.Environment(
        autoescape=jinja2.select_autoescape(['html', 'xml']),
        loader=jinja2.ChoiceLoader([jinja2.FileSystemLoader(s) for s in dirs]))
    env.loader.loaders.append(jinja2.PackageLoader(__pkg, 'templates'))
    env.filters.update(FILTERS)

    return env
