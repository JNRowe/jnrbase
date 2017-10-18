#! /usr/bin/env python
"""setup.py - Setuptools tasks and config for jnrbase"""
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

import glob
import os

from configparser import ConfigParser
from importlib.util import module_from_spec, spec_from_file_location

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


conf = ConfigParser()
conf.read('setup.cfg')
metadata = dict(conf['metadata'])

pip_support = import_file(metadata['name'], 'pip_support.py')


install_requires = []

extras_require = {}
for file in glob.glob('extra/requirements-*.txt'):
    suffix = os.path.splitext(file)[0].split('-')[1]
    if suffix not in ['doc', 'test']:
        extras_require[suffix] = pip_support.parse_requires(file)

with open('README.rst') as readme:
    long_description = readme.read()

_version = import_file(metadata['name'], '_version.py')

setup(
    name='jnrbase',
    version=_version.dotted,
    description='Common utility functionality',
    long_description=long_description,
    author='James Rowe',
    author_email='jnrowe@gmail.com',
    url='https://github.com/JNRowe/jnrbase',
    license='GPL-3',
    keywords='library support utility',
    py_modules=['ca_certs_locater', ],
    packages=['jnrbase', ],
    install_requires=install_requires,
    extras_require=extras_require,
    tests_require=['pytest'],
    cmdclass={'test': PytestTest},
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
