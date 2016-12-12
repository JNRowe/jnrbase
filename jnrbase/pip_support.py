#
# coding=utf-8
"""pip_support - pip workarounds support."""
# Copyright © 2014-2016  James Rowe <jnrowe@gmail.com>
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

# pip, both as a tool and a package manager, are not available on many of the
# systems I use.  However, lots of Python users like to use it so we'll need to
# support the workflow to some extent…

from os import path


def parse_requires(file):
    """Parse pip-style requirements files.

    This is a *very* naïve parser, but very few packages make any use of the
    more advanced features.  Support for other features will only be added when
    packages in the wild depend on them.

    Args:
        file (str): Base file to pass
    Returns:
        list: Parsed dependencies
    """
    deps = []
    with open(file) as req_file:
        entries = map(lambda s: s.split('#')[0].strip(), req_file.readlines())
        for dep in entries:
            if not dep:
                continue
            dep = dep
            if dep.startswith('-r '):
                include = dep.split()[1]
                if '/' not in include:
                    include = path.join(path.dirname(file), include)
                deps.extend(parse_requires(include))
            else:
                deps.append(dep)
    return deps
