#
# coding=utf-8
"""template - Jinja templating support."""
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


FILTERS = {}


def jinja_filter(func):
    """Simple decorator to add a new filter to Jinja environment.

    :param func func: Function to add to Jinja environment
    :rtype: ``func``
    :returns: Unmodified function
    """
    FILTERS[func.__name__] = func

    return func


@jinja_filter
def regexp(string, pattern, repl, count=0, flags=0):
    """Jinja filter for regexp replacements.

    See :func:`re.sub` for documentation.

    :rtype: `str`
    :return: Text with substitutions applied
    """
    if sys.version_info[:2] >= (2, 7):
        return re.sub(pattern, repl, string, count, flags)
    else:
        # regexps are cached, so this uglier path is no better than the 2.7
        # one.  Once 2.6 support disappears, so can this
        match = re.compile(pattern, flags=flags)
        return match.sub(repl, string, count)


@jinja_filter
def colourise(text, *args, **kwargs):
    """Colourise text using click's style function.

    Returns text untouched if colour output is not enabled

    :see: ``click.style`` for parameters

    :param str text: Text to colourise
    :rtype: ``str``
    :return: Colourised text, when possible
    """
    if sys.stdout.isatty():
        return style(text, *args, **kwargs)
    else:
        return text


@jinja_filter
def highlight(text, lexer='diff', formatter='terminal'):
    """Highlight text highlighted using pygments.

    Returns text untouched if colour output is not enabled

    :param str text: Text to highlight
    :param str lexer: Jinja lexer to use
    :param str formatter: Jinja formatter to use
    :rtype: ``str``
    :return: Syntax highlighted output, when possible
    """
    if sys.stdout.isatty():
        lexer = get_lexer_by_name(lexer)
        formatter = get_formatter_by_name(formatter)
        return pyg_highlight(text, lexer, formatter)
    else:
        return text


@jinja_filter
def html2text(html, width=80, ascii_replacements=False):
    """HTML to plain text renderer.

    :param str text: Text to process
    :param int width: Paragraph width
    :param bool ascii_replacements: Use psuedo-ascii replacements for Unicode
    :rtype: ``str``
    :return: Rendered text
    """
    html2.BODY_WIDTH = width
    html2.UNICODE_SNOB = ascii_replacements
    return html2.html2text(html).strip()


@jinja_filter
def relative_time(timestamp):
    """Format a relative time.

    :see: `human_time.human_timestamp`

    :param datetime.datetime timestamp: Event to generate relative timestamp
        against
    :rtype: ``str``
    :return: Human readable date and time offset
    """
    return human_timestamp(timestamp)


def setup(pkg):
    """Configure Jinja environment.

    :param str pkg: Package name to use as base for templates searches
    :rtype: ``jinja2.Environment
    :returns: Jinja environment
    """
    dirs = [path.join(dir, 'templates')
            for dir in xdg_basedir.get_data_dirs(pkg)]

    env = jinja2.Environment(loader=jinja2.ChoiceLoader(
        list(jinja2.FileSystemLoader(s) for s in dirs)))
    env.loader.loaders.append(jinja2.PackageLoader(pkg, 'templates'))
    env.filters.update(FILTERS)

    return env
