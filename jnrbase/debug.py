#
# coding=utf-8
"""debug - Miscellaneous debugging support"""
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


import inspect
import os
import sys

_orig_stdout = sys.stdout


class DebugPrint(object):
    """Verbose print wrapper for debugging"""
    def __init__(self, fh):
        self.fh = fh

    def write(self, text):
        if text == os.linesep:
            self.fh.write(text)
        else:
            outer = inspect.currentframe().f_back
            filename = outer.f_code.co_filename.split(os.sep)[-1]
            lineno = outer.f_lineno
            self.fh.write("[%15s:%03d] %s" % (filename[-15:], lineno, text))

    @staticmethod
    def enable():
        if not isinstance(sys.stdout, DebugPrint):
            sys.stdout = DebugPrint(sys.stdout)

    @staticmethod
    def disable():
        sys.stdout = _orig_stdout


def noisy_wrap(f):
    """Decorator to enable DebugPrint for a given function"""
    def wrapper(*args, **kwargs):
        DebugPrint.enable()
        try:
            f(*args, **kwargs)
        finally:
            DebugPrint.disable()
    return wrapper


def enter(msg=None):
    """Decorator to display a message when entering a function

    :param str msg: Message to display
    :rtype: `function`
    """
    def decorator(f):
        def wrapper(*args, **kwargs):
            if msg:
                print(msg)
            else:
                print("Entering %r" % f)
            return f(*args, **kwargs)
        return wrapper
    if callable(msg):
        return enter()(msg)
    return decorator


def exit(msg=None):
    """Decorator to display a message when exiting a function

    :param str msg: Message to display
    :rtype: `function`
    """
    def decorator(f):
        def wrapper(*args, **kwargs):
            try:
                return f(*args, **kwargs)
            finally:
                if msg:
                    print(msg)
                else:
                    print("Entering %r" % f)
        return wrapper
    if callable(msg):
        return exit()(msg)
    return decorator
