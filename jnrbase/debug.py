#
"""debug - Miscellaneous debugging support."""
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

import inspect
import os
import sys
from functools import wraps
from io import TextIOWrapper
from typing import Callable, Optional, TextIO, Union, cast

_orig_stdout = sys.stdout  # pylint: disable=invalid-name


class DebugPrint(TextIOWrapper):
    """Verbose print wrapper for debugging."""
    def __init__(self, __handle: TextIO) -> None:
        """Configure new DebugPrint handler.

        Args:
            __handle: File handle to override
        """
        self.handle = __handle

    def write(self, __text: str) -> int:
        """Write text to the debug stream.

        Args:
            __text: Text to write
        """
        if __text != os.linesep:
            frame = inspect.currentframe()
            if frame is None:
                filename = 'unknown'
                lineno = 0
            else:
                outer = frame.f_back
                filename = outer.f_code.co_filename.split(os.sep)[-1]
                lineno = outer.f_lineno
            __text = '[{:>15s}:{:03d}] {}'.format(
                filename[-15:], lineno, __text)
        self.handle.write(__text)
        return len(__text)

    @staticmethod
    def enable() -> None:
        """Patch ``sys.stdout`` to use ``DebugPrint``."""
        if not isinstance(sys.stdout, DebugPrint):
            sys.stdout = DebugPrint(sys.stdout)

    @staticmethod
    def disable() -> None:
        """Re-attach ``sys.stdout`` to its previous file handle."""
        sys.stdout = _orig_stdout


def noisy_wrap(__func: Callable) -> Callable:
    """Decorator to enable DebugPrint for a given function.

    Args:
        __func: Function to wrap
    Returns:
        Wrapped function
    """

    # pylint: disable=missing-docstring
    def wrapper(*args, **kwargs):
        DebugPrint.enable()
        try:
            __func(*args, **kwargs)
        finally:
            DebugPrint.disable()

    return wrapper


def __debug_decorator(__type: str, __msg: str) -> Callable:
    """Utility function to generate debug decorators.

    Args:
        __type: Decorator type for output
        __msg: Message to display
    Returns:
        Wrapped function
    """
    # pylint: disable=missing-docstring
    def decorator(__func):
        @wraps(__func)
        def wrapper(*args, **kwargs):
            try:
                return __func(*args, **kwargs)
            finally:
                if __msg:
                    print(__msg)
                else:
                    print(f'{__type}ing {__func.__name__!r}({__func!r})')
        return wrapper
    return decorator


def on_enter(__msg: Optional[Union[Callable, str]] = None) -> Callable:
    """Decorator to display a message when entering a function.

    See also: :func:`__debug_decorator`

    Args:
        __msg: Message to display
    Returns:
        Wrapped function
    """
    if callable(__msg):
        return on_enter()(__msg)
    return __debug_decorator('Enter', cast(str, __msg))


def on_exit(__msg: Optional[Union[Callable, str]] = None) -> Callable:
    """Decorator to display a message when exiting a function.

    See also: :func:`__debug_decorator`

    Args:
        __msg: Message to display
    Returns:
        Wrapped function
    """
    if callable(__msg):
        return on_exit()(__msg)
    return __debug_decorator('Exit', cast(str, __msg))
