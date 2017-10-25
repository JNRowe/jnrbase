#
"""template - Jinja templating support."""
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

import re
import sys

from os import path

import html2text as html2
import jinja2

from click import style
from pygments import highlight as pyg_highlight
from pygments.formatters import get_formatter_by_name
from pygments.lexers import get_lexer_by_name

from . import xdg_basedir
from .human_time import human_timestamp


#: Collection of custom filters to add to Jinja environment
FILTERS = {}


def jinja_filter(fun):
    """Simple decorator to add a new filter to Jinja environment.

    See also: :obj:`FILTERS`

    Args:
        func (types.FunctionType): Function to add to Jinja environment
    Returns:
        types.FunctionType: Unmodified function
    """
    FILTERS[fun.__name__] = fun

    return fun


@jinja_filter
def colourise(text, *args, **kwargs):
    """Colourise text using click’s style function.

    Returns text untouched if colour output is not enabled, or ``stdout`` is
    not a tty.

    See :func:`click.style` for parameters

    Args:
        text (str): Text to colourise
    Returns:
        str: Colourised text, when possible
    """
    if sys.stdout.isatty():
        return style(text, *args, **kwargs)
    else:
        return text


@jinja_filter
def highlight(text, *, lexer='diff', formatter='terminal'):
    """Highlight text highlighted using ``pygments``.

    Returns text untouched if colour output is not enabled.

    See also: :pypi:`Pygments`

    Args:
        text (str): Text to highlight
        lexer (str): Jinja lexer to use
        formatter (str): Jinja formatter to use
    Returns:
        str: Syntax highlighted output, when possible
    """
    if sys.stdout.isatty():
        lexer = get_lexer_by_name(lexer)
        formatter = get_formatter_by_name(formatter)
        return pyg_highlight(text, lexer, formatter)
    else:
        return text


@jinja_filter
def html2text(html, *, width=80, ascii_replacements=False):
    """HTML to plain text renderer.

    See also: :pypi:`html2text`

    Args:
        text (str): Text to process
        width (int): Paragraph width
        ascii_replacements (bool): Use pseudo-ASCII replacements for Unicode
    Returns:
        str: Rendered text
    """
    html2.BODY_WIDTH = width
    html2.UNICODE_SNOB = ascii_replacements
    return html2.html2text(html).strip()


@jinja_filter
def regexp(string, pattern, repl, *, count=0, flags=0):
    """Jinja filter for regexp replacements.

    See :func:`re.sub` for documentation.

    Returns:
        str: Text with substitutions applied
    """
    return re.sub(pattern, repl, string, count, flags)


@jinja_filter
def relative_time(timestamp):
    """Format a relative time.

    See :func:`~jnrbase.human_time.human_timestamp`

    Args:
        timestamp (datetime.datetime): Event to generate relative timestamp
            against
    Returns:
        str: Human readable date and time offset
    """
    return human_timestamp(timestamp)


def setup(pkg):
    """Configure a new Jinja environment with our filters.

    Args:
        pkg (str): Package name to use as base for templates searches
    Returns:
        jinja2.Environment: Configured Jinja environment
    """
    dirs = [path.join(d, 'templates') for d in xdg_basedir.get_data_dirs(pkg)]

    env = jinja2.Environment(
        autoescape=jinja2.select_autoescape(['html', 'xml']),
        loader=jinja2.ChoiceLoader([jinja2.FileSystemLoader(s) for s in dirs]))
    env.loader.loaders.append(jinja2.PackageLoader(pkg, 'templates'))
    env.filters.update(FILTERS)

    return env
