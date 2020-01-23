#
"""cmdline - Command line functionality for jnrbase."""
# Copyright © 2017-2018  James Rowe <jnrowe@gmail.com>
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

from configparser import NoOptionError, NoSectionError
from contextlib import suppress
from datetime import datetime, timezone
from inspect import signature
from io import TextIOBase
from pathlib import Path
from subprocess import CalledProcessError, run
from typing import Callable, Optional

from click import (Context, File, argument, echo, group, option, pass_context,
                   version_option)

import jnrbase
from jnrbase import (_version, colourise, config, git, httplib2_certs,
                     human_time, iso_8601, json_datetime, pip_support,
                     template, timer, xdg_basedir)


def get_default(__func: Callable, __arg: str) -> str:
    """Fetch default value for a function argument.

    Args:
        __func: Function to inspect
        __arg: Argument to extract default value for
    """
    return signature(__func).parameters[__arg].default


# pylint: disable=missing-docstring


@group(epilog='Please report bugs at https://github.com/JNRowe/jnrbase/issues',
       context_settings={'help_option_names': ['-h', '--help']})
@version_option(_version.dotted)
def cli():
    """Possibly useful cli functionality."""


@cli.group()
def messages():
    """Format messages for users."""


def text_arg(__func: Callable) -> Callable:
    """Add task selection click commands.

    Note:
        This is only here to reduce duplication in command setup.

    Args:
        __func: Function to add options to

    Returns:
        Function with additional options

    """
    return argument('text')(__func)


for k in ['fail', 'info', 'success', 'warn']:

    @messages.command(name=k,
                      help=getattr(colourise, k).__doc__.splitlines()[0])
    @text_arg
    @pass_context
    def func(ctx: Context, text: str):
        getattr(colourise, 'p{}'.format(ctx.command.name))(text)
        if ctx.command.name == 'fail':
            ctx.exit(1)


@cli.command(name='config')
@option('-n',
        '--name',
        default=get_default(config.read_configs, '__name'),
        help='Config file to read from.')
@option('-l', '--local / --no-local', help='Read local .<package>rc files.')
@argument('package')
@argument('section')
@argument('key', required=False)
def config_(name: str, local: bool, package: str, section: str,
            key: Optional[str]):
    """Extract or list values from config."""
    cfg = config.read_configs(package, name, local=local)
    if key:
        with suppress(NoOptionError, NoSectionError):
            echo(cfg.get(section, key))
    else:
        with suppress(NoSectionError):
            for opt in cfg.options(section):
                colourise.pinfo(opt)
                echo('    {}'.format(cfg.get(section, opt)))


@cli.command()
@option('-m',
        '--match',
        default=get_default(git.find_tag, '__matcher'),
        help='Limit the selection of matches with glob.')
@option('-s', '--strict / --no-strict', help='Always generate a result.')
@option('-d',
        '--directory',
        type=Path,
        default=get_default(git.find_tag, 'git_dir'),
        help='Git repository to operate on.')
def find_tag(match: str, strict: bool, directory: Path):
    with suppress(CalledProcessError):
        echo(git.find_tag(match, strict=strict, git_dir=directory))


@cli.command()
def certs():
    """Find location of system certificates."""
    echo(httplib2_certs.find_certs())


@cli.command()
@argument('timestamp')
def pretty_time(timestamp: str):
    """Format timestamp for human consumption."""
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


@cli.command()
@argument('name')
def pip_requires(name: str):
    """Parse pip requirements file."""
    requires = pip_support.parse_requires(name)
    for req in requires:
        echo(req)


@cli.command()
@option('-e', '--env', type=File(), help='JSON data to generate output with.')
@argument('package')
@argument('tmpl')
def gen_text(env: TextIOBase, package: str, tmpl: str):
    """Create output from Jinja template."""
    if env:
        env_args = json_datetime.load(env)
    else:
        env_args = {}
    jinja_env = template.setup(package)
    echo(jinja_env.get_template(tmpl).render(**env_args))


@cli.command()
@argument('command')
@pass_context
def time(ctx: Context, command: str):
    """Time the output of a command."""
    with timer.Timing(verbose=True):
        proc = run(command, shell=True)
    ctx.exit(proc.returncode)


@cli.group()
def dirs():
    """Query package directories."""


for k in ['cache', 'config', 'data']:

    @dirs.command(name=k,
                  help='Display {} dir honouring XDG basedir.'.format(k))
    @argument('package')
    @pass_context
    def func(ctx: Context, package: str):
        echo(getattr(xdg_basedir, 'user_{}'.format(ctx.command.name))(package))


if __name__ == '__main__':
    cli()
