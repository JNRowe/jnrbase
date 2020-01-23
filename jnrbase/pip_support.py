#
"""pip_support - pip workarounds support."""
# Copyright © 2014-2018  James Rowe <jnrowe@gmail.com>
#                        Nathan McGregor <nathan.mcgregor@astrium.eads.net>
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

# pip, both as a tool and a package manager, are not available on many of the
# systems I use.  However, lots of Python users like to use it so we’ll need to
# support the workflow to some extent…

import re
from pathlib import Path
from sys import version_info
from typing import List


__eval_env = {
    '__builtins__': {},
    'python_version': '{}.{}'.format(*version_info[:2]),
}


def parse_requires(__fname: Path) -> List[str]:
    """Parse ``pip``-style requirements files.

    This is a *very* naïve parser, but very few packages make use of the more
    advanced features.  Support for other features will be added only when
    packages in the wild depend on them.

    Args:
        __fname: Base file to pass
    Returns:
        Parsed dependencies
    """
    deps = []
    with __fname.open() as req_file:
        entries = [s.split('#')[0].strip() for s in req_file.readlines()]
        for dep in entries:
            if not dep:
                continue
            elif dep.startswith('-r '):
                include = dep.split()[1]
                if '/' not in include:
                    include = __fname.parent / include
                else:
                    include = Path(include)
                deps.extend(parse_requires(include))
                continue
            elif ';' in dep:
                dep, marker = [s.strip() for s in dep.split(';')]
                # Support for other markers will be added when they’re actually
                # found in the wild
                match = re.fullmatch(
                    r"""
                        (?:python_version)  # Supported markers
                        \s*
                        (?:<=?|==|>=?)  # Supported comparisons
                        \s*
                        (?P<quote>(?:'|"))(?:[\d\.]+)(?P=quote)  # Test
                    """, marker, re.VERBOSE)
                if not match:
                    raise ValueError('Invalid marker {!r}'.format(marker))
                if not eval(marker, __eval_env):  # pylint: disable=eval-used
                    continue
            deps.append(dep)
    return deps
