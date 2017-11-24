#
"""cli - Command line functionality for jnrbase."""
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

from inspect import signature

from click import argument, group, pass_context, version_option

import jnrbase
from jnrbase import _version, colourise, i18n


_, N_ = i18n.setup(jnrbase)


def get_default(func, arg):
    return signature(func).parameters[arg].default


@group(help=_('Possibly useful cli functionality.'),
       epilog=_('Please report bugs at '
                'https://github.com/JNRowe/jnrbase/issues'),
       context_settings={'help_option_names': ['-h', '--help']})
@version_option(_version.dotted)
def cli():
    pass


@cli.group(help=_('Format messages for users.'))
def messages():
    pass


def text_arg(f):
    return argument('text')(f)


@messages.command(help=_(colourise.fail.__doc__.splitlines()[0]))
@text_arg
@pass_context
def fail(ctx, text):
    colourise.pfail(text)
    ctx.exit(1)


for k in ['info', 'success', 'warn']:
    fn = getattr(colourise, 'p{}'.format(k))
    help = _(getattr(colourise, k).__doc__.splitlines()[0])
    messages.command(name=k, help=help)(text_arg(fn))


if __name__ == '__main__':
    cli()
