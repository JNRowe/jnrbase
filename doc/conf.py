#
"""conf - Sphinx configuration information."""
# Copyright © 2014-2020  James Rowe <jnrowe@gmail.com>
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

import os
import sys

from contextlib import suppress
from pathlib import Path
from subprocess import PIPE, CalledProcessError, run

root_dir = Path(__file__).parent.parents[2]
sys.path.insert(0, str(root_dir))

import jnrbase  # NOQA: E402

on_rtd = os.getenv('READTHEDOCS')
if not on_rtd:
    import sphinx_rtd_theme

# General configuration {{{
extensions = \
    ['sphinx.ext.{}'.format(ext)
     for ext in ['autodoc', 'coverage', 'doctest', 'extlinks', 'intersphinx',
                 'napoleon', 'todo', 'viewcode']] \
    + ['sphinxcontrib.{}'.format(ext) for ext in []] \
    + ['sphinx_autodoc_typehints', 'sphinx_click.ext']

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

rst_epilog = """
.. |PyPI| replace:: :abbr:`PyPI (Python Package Index)`
.. |modref| replace:: :mod:`jnrbase`
"""

default_role = 'any'

needs_sphinx = '2.0'

nitpicky = True
# }}}

# Project information {{{
project = 'jnrbase'
author = 'James Rowe'
copyright = f'2014-2020  {author}'

version = '{major}.{minor}'.format_map(jnrbase._version.dict)
release = jnrbase._version.dotted

rst_prolog = """
.. |ISO| replace:: :abbr:`ISO (International Organization for Standardization)`
"""

modindex_common_prefix = [
    'jnrbase.',
]

trim_footnote_reference_space = True
# }}}

# Options for HTML output {{{
# readthedocs.org handles this setup for their builds, but it is nice to see
# approximately correct builds on the local system too
if not on_rtd:
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [
        sphinx_rtd_theme.get_html_theme_path(),
    ]

with suppress(CalledProcessError):
    proc = run(
        ['git', 'log', '--pretty=format:%ad [%h]', '--date=short', '-n1'],
        stdout=PIPE)
    html_last_updated_fmt = proc.stdout.decode()

html_baseurl = 'https://jnrbase.readthedocs.io/'

html_copy_source = False
# }}}

# Options for manual page output {{{
man_pages = [('jnrbase.1', 'jnrbase', 'jnrbase Documentation', [
    'James Rowe',
], 1)]
# }}}

# autodoc extension settings {{{
autoclass_content = 'both'
autodoc_default_options = {
    'members': None,
}
# }}}

# coverage extension settings {{{
coverage_write_headline = False
# }}}

# extlinks extension settings {{{
github_base = 'https://github.com/JNRowe/{}/'.format(project)
extlinks = {
    'issue': ('{}issues/%s'.format(github_base), 'issue #'),
    'pr': ('{}pull/%s'.format(github_base), 'pull request #'),
    'pypi': ('https://pypi.org/project/%s/', ''),
}
# }}}

# graphviz extension settings {{{
graphviz_output_format = 'svg'
# }}}

# intersphinx extension settings {{{
intersphinx_mapping = {
    k: (v, os.getenv('SPHINX_{}_OBJECTS'.format(k.upper())))
    for k, v in {
        'click': 'https://click.palletsprojects.com/en/7.x/',
        'jinja': 'https://jinja.palletsprojects.com/en/2.10.x/',
        'pygments': 'https://pygments.org/',
        'python': 'https://docs.python.org/3/',
    }.items()
}
# }}}

# napoleon extension settings {{{
napoleon_numpy_docstring = False
# }}}

# spelling extension settings {{{
spelling_ignore_acronyms = False
spelling_lang = 'en_GB'
spelling_word_list_filename = 'wordlist.txt'
spelling_ignore_python_builtins = False
spelling_ignore_importable_modules = False
# }}}

# todo extension settings {{{
todo_include_todos = True
# }}}
