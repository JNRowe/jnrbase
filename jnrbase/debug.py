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
