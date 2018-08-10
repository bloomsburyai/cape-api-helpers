# Copyright 2018 BLEMUNDSBURY AI LIMITED
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pytest
from cape_api_helpers.input import required_parameter, optional_parameter
from cape_api_helpers.exceptions import UserException


def test_required_parameter():
    request = {'args': {'test' : 'testing'}}
    test = required_parameter(request, 'test')
    assert test == 'testing'


def test_case_insensitive():
    request = {'args': {'test' : 'testing'}}
    test = required_parameter(request, 'TEST')
    assert test == 'testing'
    

def test_missing_required_parameter():
    with pytest.raises(UserException):
        request = {'args': {'test' : 'testing'}}
        test = required_parameter(request, 'missing')


def test_optional_parameter():
    request = {'args': {'test': 'testing'}}
    test = optional_parameter(request, 'test', 'hello')
    assert test == 'testing'


def test_missing_optional_parameter():
    request = {'args': {'test': 'testing'}}
    test = optional_parameter(request, 'missing', 'hello')
    assert test == 'hello'
