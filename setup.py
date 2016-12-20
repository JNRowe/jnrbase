#! /usr/bin/env python
# coding=utf-8
"""setup.py - Setuptools tasks and config for jnrbase"""
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

import imp
import glob
import os

from setuptools import setup


# Hack to import _version file without importing jnrbase/__init__.py, its
# purpose is to allow import without requiring dependencies at this point.
ver_file = open('jnrbase/_version.py')
_version = imp.load_module('_version', ver_file, ver_file.name,
                           ('.py', ver_file.mode, imp.PY_SOURCE))

# Hack to import pip_support file without importing jnrbase/__init__.py, its
# purpose is to allow import without requiring dependencies at this point.
pip_file = open('jnrbase/pip_support.py')
pip_support = imp.load_module('pip_support', pip_file, pip_file.name,
                              ('.py', pip_file.mode, imp.PY_SOURCE))


install_requires = []  # extra/requirements-base.txt

extras_require = {}
for file in glob.glob('extra/requirements-*.txt'):
    suffix = os.path.splitext(file)[0].split('-')[1]
    if suffix not in ['doc', 'test']:
        extras_require[suffix] = pip_support.parse_requires(file)

setup(
    name='jnrbase',
    version=_version.dotted,
    description='Common utility functionality',
    long_description=open('README.rst').read(),
    author='James Rowe',
    author_email='jnrowe@gmail.com',
    url='https://github.com/JNRowe/jnrbase',
    license='GPL-3',
    keywords='library support utility',
    py_modules=['ca_certs_locater', ],
    packages=['jnrbase', ],
    install_requires=install_requires,
    extras_require=extras_require,
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
