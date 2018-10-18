#
"""cmdline - Command line functionality for jnrbase."""
# Copyright © 2017-2018  James Rowe <jnrowe@gmail.com>
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
#
# SPDX-License-Identifier: GPL-3.0+

from configparser import NoOptionError, NoSectionError
from contextlib import suppress
from datetime import datetime, timezone
from inspect import signature
from io import TextIOBase
from subprocess import CalledProcessError, run
from typing import Callable, Optional

from click import (Context, File, argument, echo, group, option, pass_context,
                   version_option)

import jnrbase
from jnrbase import (_version, colourise, config, git, httplib2_certs,
                     human_time, iso_8601, json_datetime, pip_support,
                     template, timer, xdg_basedir)


def get_default(__func: Callable, __arg: str) -> str:
    """Fetch default value for a function argument

    Args:
        __func: Function to inspect
        __arg: Argument to extract default value for
    """
    return signature(__func).parameters[__arg].default


# pylint: disable=missing-docstring


@group(help='Possibly useful cli functionality.',
       epilog='Please report bugs at https://github.com/JNRowe/jnrbase/issues',
       context_settings={'help_option_names': ['-h', '--help']})
@version_option(_version.dotted)
def cli():
    pass


@cli.group(help='Format messages for users.')
def messages():
    pass


def text_arg(__f: Callable) -> Callable:
    return argument('text')(__f)


@messages.command(help=colourise.fail.__doc__.splitlines()[0])
@text_arg
@pass_context
def fail(ctx: Context, text: str):
    colourise.pfail(text)
    ctx.exit(1)


@messages.command(help=colourise.info.__doc__.splitlines()[0])
@text_arg
def info(text: str):
    colourise.pinfo(text)


@messages.command(help=colourise.success.__doc__.splitlines()[0])
@text_arg
def success(text: str):
    colourise.psuccess(text)


@messages.command(help=colourise.warn.__doc__.splitlines()[0])
@text_arg
def warn(text: str):
    colourise.pwarn(text)


@cli.command(name='config', help='Extract or list values from config.')
@option('-n', '--name', default=get_default(config.read_configs, '__name'),
        help='Config file to read from.')
@option('-l', '--local / --no-local', help='Read local .<package>rc files.')
@argument('package')
@argument('section')
@argument('key', required=False)
def config_(name: str, local: bool, package: str, section: str,
            key: Optional[str]):
    cfg = config.read_configs(package, name, local=local)
    if key:
        with suppress(NoOptionError, NoSectionError):
            echo(cfg.get(section, key))
    else:
        with suppress(NoSectionError):
            for opt in cfg.options(section):
                colourise.pinfo(opt)
                echo('    {}'.format(cfg.get(section, opt)))


@cli.command(help='Find tag for git repository.')
@option('-m', '--match', default=get_default(git.find_tag, '__matcher'),
        help='Limit the selection of matches with glob.')
@option('-s', '--strict / --no-strict', help='Always generate a result.')
@option('-d', '--directory', default=get_default(git.find_tag, 'git_dir'),
        help='Git repository to operate on.')
def find_tag(match: str, strict: bool, directory: str):
    with suppress(CalledProcessError):
        echo(git.find_tag(match, strict=strict, git_dir=directory))


@cli.command(help='Find location of system certificates.')
def certs():
    echo(httplib2_certs.find_certs())


@cli.command(help='Format timestamp for human consumption.')
@argument('timestamp')
def pretty_time(timestamp: str):
    try:
        parsed = iso_8601.parse_datetime(timestamp)
    except ValueError:
        now = datetime.utcnow().replace(tzinfo=timezone.utc)
        try:
            delta = iso_8601.parse_delta(timestamp)
        except ValueError:
            delta = human_time.parse_timedelta(timestamp)
        parsed = now - delta

    echo(human_time.human_timestamp(parsed))


@cli.command(help='Parse pip requirements file.')
@argument('name')
def pip_requires(name: str):
    requires = pip_support.parse_requires(name)
    for req in requires:
        echo(req)


@cli.command(help='Create output from Jinja template.')
@option('-e', '--env', type=File(),
        help='JSON data to generate output with.')
@argument('package')
@argument('tmpl')
def gen_text(env: TextIOBase, package: str, tmpl: str):
    if env:
        env_args = json_datetime.load(env)
    else:
        env_args = {}
    jinja_env = template.setup(package)
    echo(jinja_env.get_template(tmpl).render(**env_args))


@cli.command(help='Time the output of a command.')
@argument('command')
@pass_context
def time(ctx: Context, command: str):
    with timer.Timing(verbose=True):
        proc = run(command, shell=True)
    ctx.exit(proc.returncode)


@cli.group(help='Query package directories.')
def dirs():
    pass


for k in ['cache', 'config', 'data']:
    @dirs.command(name=k,
                  help='Display {} dir honouring XDG basedir.'.format(k))
    @argument('package')
    @pass_context
    def func(ctx: Context, package: str):
        echo(getattr(xdg_basedir, 'user_{}'.format(ctx.command.name))(package))


if __name__ == '__main__':
    cli()
