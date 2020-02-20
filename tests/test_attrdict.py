#
"""test_attrdict - Test AttrDict support"""
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

from inspect import signature
from random import choice
from typing import Dict, Union

from hypothesis import given
from hypothesis.strategies import dictionaries, text
from pytest import fixture, raises

from jnrbase.attrdict import AttrDict, ROAttrDict  # NOQA: F401


@fixture()
def base_obj(request) -> Union[AttrDict, ROAttrDict]:
    type_ = signature(request.function).parameters['base_obj'].annotation
    return type_(carrots=3, snacks=0)


def test_AttrDict_base(base_obj: AttrDict):  # NOQA: N802
    assert isinstance(base_obj, dict)

    assert base_obj['carrots'] == 3
    assert base_obj['snacks'] == 0

    assert sorted(base_obj.keys()) == ['carrots', 'snacks']


def test_AttrDict___contains__(base_obj: AttrDict):  # NOQA: N802
    assert 'carrots' in base_obj
    assert 'prizes' not in base_obj


def test_AttrDict___getattr__(base_obj: AttrDict):  # NOQA: N802
    assert base_obj.carrots == 3
    assert base_obj.snacks == 0


def test_AttrDict___setattr__(base_obj: AttrDict):  # NOQA: N802
    base_obj.carrots, base_obj.snacks = 0, 3
    assert base_obj.carrots == 0
    assert base_obj.snacks == 3


def test_AttrDict___delattr__(base_obj: AttrDict):  # NOQA: N802
    assert 'carrots' in base_obj
    del base_obj['carrots']
    assert 'carrots' not in base_obj


@given(dictionaries(text(), text(), dict_class=AttrDict, min_size=1))
def test_AttrDict___delattr___multi(d: Dict[str, str]):  # NOQA: N802
    k = choice(list(d))
    assert k in d
    del d[k]
    assert k not in d


def test_AttrDict_invalid_key_set(base_obj: AttrDict):  # NOQA: N802
    with raises(AttributeError, match='unhashable'):
        base_obj.__setattr__({True: False}, None)


def test_AttrDict_invalid_key_delete(base_obj: AttrDict):  # NOQA: N802
    with raises(AttributeError, match='unhashable'):
        base_obj.__delattr__({True: False})


def test_AttrDict_swallowed_exception(base_obj: AttrDict):  # NOQA: N802
    def raise_error():
        raise ValueError()

    base_obj.prop = property(raise_error)

    assert 'prop' in base_obj


def test_ROAttrDict___setattr__(base_obj: ROAttrDict):  # NOQA: N802
    with raises(AttributeError, match='is read-only'):
        base_obj.carrots = 1


def test_ROAttrDict___delattr__(base_obj: ROAttrDict):  # NOQA: N802
    with raises(AttributeError, match='is read-only'):
        del base_obj.carrots
