#
"""conf - Sphinx configuration information"""
# Copyright © 2011-2016  James Rowe <jnrowe@gmail.com>
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

import os
import sys

from contextlib import suppress
from subprocess import (CalledProcessError, check_output)

root_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, root_dir)

import jnrbase  # NOQA

extensions = \
    ['sphinx.ext.%s' % ext for ext in ['autodoc', 'coverage', 'doctest',
                                       'extlinks', 'intersphinx', 'napoleon',
                                       'todo', 'viewcode']] \
    + ['sphinxcontrib.%s' % ext for ext in []]

# Only activate spelling if it is installed.  It is not required in the
# general case and we don't have the granularity to describe this in a clean
# way
try:
    from sphinxcontrib import spelling  # NOQA
except ImportError:
    pass
else:
    extensions.append('sphinxcontrib.spelling')

master_doc = 'index'
source_suffix = '.rst'

project = u'jnrbase'
copyright = jnrbase.__copyright__

version = '.'.join([str(s) for s in jnrbase._version.tuple[:2]])
release = jnrbase._version.dotted

pygments_style = 'sphinx'
with suppress(CalledProcessError):
    html_last_updated_fmt = check_output(
        ['git', 'log', "--pretty=format:'%ad [%h]'", '--date=short', '-n1'],
        encoding='ascii'
    )

# Autodoc extension settings
autoclass_content = 'init'
autodoc_default_flags = ['members', ]

# intersphinx extension settings
intersphinx_mapping = {
    k: (v, os.getenv('SPHINX_%s_OBJECTS' % k.upper()))
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
