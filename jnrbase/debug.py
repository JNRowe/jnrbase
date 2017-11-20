#
"""debug - Miscellaneous debugging support."""
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

import inspect
import os
import sys

from functools import wraps

_orig_stdout = sys.stdout


class DebugPrint:

    """Verbose print wrapper for debugging."""

    def __init__(self, fh):
        """Configure new DebugPrint handler.

        Args:
            fh (io.TextIOWrapper): File handle to override
        """
        self.fh = fh

    def write(self, text):
        """Write text to the debug stream.

        Args:
            text (str): Text to write
        """
        if text == os.linesep:
            self.fh.write(text)
        else:
            frame = inspect.currentframe()
            if frame is None:
                filename = 'unknown'
                lineno = 0
            else:
                outer = frame.f_back
                filename = outer.f_code.co_filename.split(os.sep)[-1]
                lineno = outer.f_lineno
            self.fh.write('[{:>15s}:{:03d}] {}'.format(filename[-15:], lineno,
                                                       text))

    @staticmethod
    def enable():
        """Patch ``sys.stdout`` to use ``DebugPrint``."""
        if not isinstance(sys.stdout, DebugPrint):
            sys.stdout = DebugPrint(sys.stdout)

    @staticmethod
    def disable():
        """Re-attach ``sys.stdout`` to its previous file handle."""
        sys.stdout = _orig_stdout


def noisy_wrap(fun):
    """Decorator to enable DebugPrint for a given function.

    Args:
        fun (types.FunctionType): Function to wrap
    Returns:
        types.FunctionType: Wrapped function

    """
    def wrapper(*args, **kwargs):
        DebugPrint.enable()
        try:
            fun(*args, **kwargs)
        finally:
            DebugPrint.disable()
    return wrapper


def on_enter(msg=None):
    """Decorator to display a message when entering a function.

    Args:
        msg (str): Message to display
    Returns:
        types.FunctionType: Wrapped function

    """
    def decorator(fun):
        @wraps(fun)
        def wrapper(*args, **kwargs):
            if msg:
                print(msg)
            else:
                print('Entering {!r}({!r})'.format(fun.__name__, fun))
            return fun(*args, **kwargs)
        return wrapper
    if callable(msg):
        return on_enter()(msg)
    return decorator


def on_exit(msg=None):
    """Decorator to display a message when exiting a function.

    Args:
        msg (str): Message to display
    Returns:
        types.FunctionType: Wrapped function

    """
    def decorator(fun):
        @wraps(fun)
        def wrapper(*args, **kwargs):
            try:
                return fun(*args, **kwargs)
            finally:
                if msg:
                    print(msg)
                else:
                    print('Exiting {!r}({!r})'.format(fun.__name__, fun))
        return wrapper
    if callable(msg):
        return on_exit()(msg)
    return decorator
