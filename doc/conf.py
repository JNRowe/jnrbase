#
"""conf - Sphinx configuration information."""
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

import os
import sys

from contextlib import suppress
from subprocess import CalledProcessError, PIPE, run

root_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, root_dir)

import jnrbase  # NOQA: E402

on_rtd = os.getenv('READTHEDOCS')
if not on_rtd:
    import sphinx_rtd_theme

extensions = \
    ['sphinx.ext.{}'.format(ext)
     for ext in ['autodoc', 'coverage', 'doctest', 'extlinks', 'intersphinx',
                 'napoleon', 'todo', 'viewcode']] \
    + ['sphinxcontrib.{}'.format(ext) for ext in []]

if not on_rtd:
    # Only activate spelling if it is installed.  It is not required in the
    # general case and we don’t have the granularity to describe this in a
    # clean way
    try:
        from sphinxcontrib import spelling  # NOQA: F401
    except ImportError:
        pass
    else:
        extensions.append('sphinxcontrib.spelling')

master_doc = 'index'
source_suffix = '.rst'

project = u'jnrbase'
copyright = '2014-2017  James Rowe'

version = '.'.join([str(s) for s in jnrbase._version.tuple[:2]])
release = jnrbase._version.dotted

html_experimental_html5_writer = True

# readthedocs.org handles this setup for their builds, but it is nice to see
# approximately correct builds on the local system too
if not on_rtd:
    html_theme = "sphinx_rtd_theme"
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path(), ]

pygments_style = 'sphinx'
with suppress(CalledProcessError):
    proc = run(['git', 'log', "--pretty=format:'%ad [%h]'", '--date=short',
                '-n1'],
               stdout=PIPE)
    html_last_updated_fmt = proc.stdout.decode()

# Autodoc extension settings
autoclass_content = 'init'
autodoc_default_flags = ['members', ]

# intersphinx extension settings
intersphinx_mapping = {
    k: (v, os.getenv('SPHINX_{}_OBJECTS'.format(k.upper())))
    for k, v in {
        'click': 'http://click.pocoo.org/6/',
        'pygments': 'http://pygments.org/',
        'python': 'http://docs.python.org/3/',
    }.items()
}

# extlinks extension settings
extlinks = {
    'pypi': ('http://pypi.python.org/pypi/%s', ''),
}

# spelling extension settings
spelling_lang = 'en_GB'
spelling_word_list_filename = 'wordlist.txt'

# napoleon extension settings
napoleon_numpy_docstring = False

# todo extension settings
todo_include_todos = True
