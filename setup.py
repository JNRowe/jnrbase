#! /usr/bin/env python
"""setup.py - Setuptools tasks and config for jnrbase."""
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

from configparser import ConfigParser
from glob import glob
from importlib.util import module_from_spec, spec_from_file_location
from os import path

from setuptools import setup
from setuptools.command.test import test


class PytestTest(test):
    def finalize_options(self):
        test.finalize_options(self)
        self.test_args = ['tests/', ]
        self.test_suite = True

    def run_tests(self):
        from sys import exit
        from pytest import main
        exit(main(self.test_args))


def import_file(package, fname):
    """Import file directly.

    This is a hack to import files from packages without importing
    <package>/__init__.py, its purpose is to allow import without requiring
    all the dependencies at this point.

    Args:
        package (str): Package to import from
        fname (str): File to import
    Returns:
        types.ModuleType: Imported module
    """
    mod_name = fname.rstrip('.py')
    spec = spec_from_file_location(mod_name, '{}/{}'.format(package, fname))
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def make_list(s):
    return s.strip().splitlines()


conf = ConfigParser()
conf.read('setup.cfg')
metadata = dict(conf['metadata'])

pip_support = import_file(metadata['name'], 'pip_support.py')

extras_require = {}
for file in glob('extra/requirements-*.txt'):
    suffix = path.splitext(file)[0].split('-')[1]
    if suffix not in ['doc', 'test']:
        extras_require[suffix] = pip_support.parse_requires(file)

tests_require = pip_support.parse_requires('extra/requirements-test.txt')

metadata = dict(conf['metadata'])
for k in ['classifiers', 'packages', 'py_modules']:
    if k in metadata:
        metadata[k] = make_list(metadata[k])

for k in ['entry_points', 'package_data']:
    if k in metadata:
        metadata[k] = eval(metadata[k], {'__builtins__': {}})

with open('README.rst') as readme:
    metadata['long_description'] = readme.read()

_version = import_file(metadata['name'], '_version.py')

setup(
    version=_version.dotted,
    extras_require=extras_require,
    tests_require=tests_require,
    cmdclass={'test': PytestTest},
    zip_safe=False,
    **metadata,
)
