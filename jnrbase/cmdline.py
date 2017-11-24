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

from contextlib import suppress
from configparser import NoOptionError, NoSectionError
from datetime import datetime, timezone
from inspect import signature
from subprocess import CalledProcessError

from click import argument, echo, group, option, pass_context, version_option

import jnrbase
from jnrbase import (_version, colourise, config, git, httplib2_certs,
                     human_time, i18n, iso_8601, pip_support)


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


@cli.command(name='config', help=_('Extract or list values from config.'))
@option('-n', '--name', default=get_default(config.read_configs, 'name'),
        help=_('Config file to read from.'))
@option('-l', '--local / --no-local', help=_('Read local .<package>rc files.'))
@argument('package')
@argument('section')
@argument('key', required=False)
def config_(name, local, package, section, key):
    cfg = config.read_configs(package, name, local=local)
    if key:
        with suppress(NoOptionError, NoSectionError):
            echo(cfg.get(section, key))
    else:
        with suppress(NoSectionError):
            for k in cfg.options(section):
                colourise.pinfo(k)
                echo('    {}'.format(cfg.get(section, k)))


@cli.command('find-tag', help=_('Find tag for git repository.'))
@option('-m', '--match', default=get_default(git.find_tag, 'matcher'),
        help=_('Limit the selection of matches with glob.'))
@option('-s', '--strict / --no-strict', help=_('Always generate a result.'))
@option('-d', '--directory', default=get_default(git.find_tag, 'git_dir'),
        help=_('Git repository to operate on.'))
def find_tag(match, strict, directory):
    with suppress(CalledProcessError):
        echo(git.find_tag(match, strict=strict, git_dir=directory))


@cli.command(help=_('Find location of system certificates.'))
def certs():
    echo(httplib2_certs.find_certs())


@cli.command('pretty-time', help=_('Format timestamp for human consumption.'))
@argument('time')
def pretty_time(time):
    try:
        dt = iso_8601.parse_datetime(time)
    except ValueError:
        now = datetime.utcnow().replace(tzinfo=timezone.utc)
        try:
            delta = iso_8601.parse_delta(time)
        except:
            delta = human_time.parse_timedelta(time)
        dt = now - delta

    echo(human_time.human_timestamp(dt))


@cli.command('pip-requires', help=_('Parse pip requirements file.'))
@argument('name')
def pip_requires(name):
    requires = pip_support.parse_requires(name)
    for l in requires:
        echo(l)


if __name__ == '__main__':
    cli()
