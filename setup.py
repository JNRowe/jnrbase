#! /usr/bin/env python3
"""setup.py - Setuptools tasks and config for jnrbase."""
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

from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
from types import ModuleType

from setuptools import setup
from setuptools.command.test import test


class PytestTest(test):
    def finalize_options(self):
        test.finalize_options(self)
        self.test_args = [
            'tests/',
        ]
        self.test_suite = True

    def run_tests(self):
        from sys import exit
        from pytest import main
        exit(main(self.test_args))


def import_file(package: str, fname: str) -> ModuleType:
    """Import file directly.

    This is a hack to import files from packages without importing
    <package>/__init__.py, its purpose is to allow import without requiring
    all the dependencies at this point.

    Args:
        package: Package to import from
        fname: File to import
    Returns:
        Imported module
    """
    mod_name = fname.rstrip('.py')
    spec = spec_from_file_location(mod_name, '{}/{}'.format(package, fname))
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


pip_support = import_file('jnrbase', 'pip_support.py')

# Note: We can't use setuptool’s requirements support as it only a list
# and doesn’t support pip’s inclusion mechanism
extras_require = {}
for file in Path('extra').glob('requirements-*.txt'):
    suffix = file.stem.split('-')[1]
    if suffix not in ['dev', 'doc', 'test']:
        extras_require[suffix] = pip_support.parse_requires(file)

tests_require = pip_support.parse_requires(Path('extra/requirements-test.txt'))

setup(
    extras_require=extras_require,
    tests_require=tests_require,
    cmdclass={'test': PytestTest},
)
